// Not Geese — punkt wejścia dla gier z okrajanym kodem zarządzanym.
//
// Preloader BepInEksa woła w PlatformUtils.SetPlatform metodę Module.GetPEKind
// wyłącznie po to, żeby wykryć procesor ARM. Gry budowane z managed strippingiem
// nie mają jej w mscorlib, więc loader wywraca się, zanim cokolwiek się wczyta.
// Objaw: brak BepInEx/LogOutput.log i plik preloader_*.log w katalogu gry.
//
// Ta biblioteka zastępuje punkt wejścia BepInEksa: robi dokładnie to samo,
// co jego PreloaderRunner.PreloaderPreMain, tylko platformę ustala sama,
// bez tego jednego wywołania. Potem oddaje sterowanie BepInEksowi i znika.
//
// Wszystko idzie przez refleksję, więc ta biblioteka nie kompiluje się przeciw
// BepInEksowi i nie zawiera ani linijki jego kodu — wywołuje go tylko tak,
// jak każda inna biblioteka wywołuje bibliotekę.

using System;
using System.IO;
using System.Reflection;

namespace Doorstop
{
    public static class Entrypoint
    {
        /// Te same biblioteki, które BepInEx ładuje wcześnie, żeby gra nie podstawiła swoich.
        private static readonly string[] CriticalAssemblies =
        {
            "Mono.Cecil.dll",
            "Mono.Cecil.Mdb.dll",
            "Mono.Cecil.Pdb.dll",
            "Mono.Cecil.Rocks.dll",
            "MonoMod.Utils.dll",
            "MonoMod.RuntimeDetour.dll",
            "0Harmony.dll",
        };

        private static string _coreDirectory;

        public static void Start()
        {
            var report = "notgeese_loader_" + DateTime.Now.ToString("yyyyMMdd_HHmmss_fff") + ".log";

            try
            {
                var invokePath = Environment.GetEnvironmentVariable("DOORSTOP_INVOKE_DLL_PATH");
                var processPath = Environment.GetEnvironmentVariable("DOORSTOP_PROCESS_PATH");
                report = Path.Combine(Path.GetDirectoryName(processPath) ?? ".", report);

                _coreDirectory = Path.GetDirectoryName(Path.GetFullPath(invokePath));
                AppDomain.CurrentDomain.AssemblyResolve += ResolveFromCore;

                var preloader = Load("BepInEx.Preloader.dll");
                var bepinex = Load("BepInEx.dll");
                var monoMod = Load("MonoMod.Utils.dll");

                SetPlatform(monoMod);
                LoadEnvironment(preloader);
                SetPaths(bepinex, invokePath, processPath);
                LoadCriticalAssemblies();

                var runner = preloader.GetType("BepInEx.Preloader.PreloaderRunner", true);
                var localResolve = runner.GetMethod("LocalResolve", BindingFlags.NonPublic | BindingFlags.Static);
                if (localResolve == null) throw new MissingMethodException("PreloaderRunner.LocalResolve");
                AppDomain.CurrentDomain.AssemblyResolve +=
                    (ResolveEventHandler) Delegate.CreateDelegate(typeof(ResolveEventHandler), localResolve);

                // Nasz zastępczy resolver ustępuje miejsca temu z BepInEksa, tak jak w oryginale.
                AppDomain.CurrentDomain.AssemblyResolve -= ResolveFromCore;

                var main = runner.GetMethod("PreloaderMain", BindingFlags.NonPublic | BindingFlags.Static);
                if (main == null) throw new MissingMethodException("PreloaderRunner.PreloaderMain");
                main.Invoke(null, null);
            }
            catch (Exception error)
            {
                try
                {
                    File.WriteAllText(report, "Not Geese — punkt wejścia nie wystartował.\n\n" + error);
                }
                catch
                {
                    // Nie mamy gdzie tego zapisać; gra rusza po angielsku i tyle.
                }
                AppDomain.CurrentDomain.AssemblyResolve -= ResolveFromCore;
            }
        }

        private static Assembly Load(string name)
        {
            return Assembly.LoadFile(Path.Combine(_coreDirectory, name));
        }

        /// Odpowiednik PlatformUtils.SetPlatform bez pytania o procesor ARM.
        /// Paczki składamy pod Windows, więc tylko tę gałąź trzeba odwzorować.
        private static void SetPlatform(Assembly monoMod)
        {
            var platformType = monoMod.GetType("MonoMod.Utils.Platform", true);
            var helperType = monoMod.GetType("MonoMod.Utils.PlatformHelper", true);

            var identifier = Environment.OSVersion.Platform.ToString().ToLowerInvariant();
            var name = "Unknown";
            if (identifier.Contains("win")) name = "Windows";
            else if (identifier.Contains("mac") || identifier.Contains("osx")) name = "MacOS";
            else if (identifier.Contains("lin") || identifier.Contains("unix")) name = "Linux";

            // Przez IConvertible, bo okrojony mscorlib nie musi mieć Convert.ToInt64(object).
            var value = ((IConvertible) Enum.Parse(platformType, name)).ToInt64(null);
            if (IntPtr.Size >= 8)
            {
                value |= ((IConvertible) Enum.Parse(platformType, "Bits64")).ToInt64(null);
            }

            var platform = Enum.ToObject(platformType, value);
            var current = helperType.GetProperty("Current", BindingFlags.Public | BindingFlags.Static);
            if (current != null && current.CanWrite)
            {
                current.SetValue(null, platform, null);
                return;
            }

            // W niektórych wydaniach MonoModa właściwość jest tylko do odczytu,
            // a wartość siedzi w polu obok niej.
            var field = helperType.GetField("_current", BindingFlags.NonPublic | BindingFlags.Static)
                        ?? helperType.GetField("current", BindingFlags.NonPublic | BindingFlags.Static);
            if (field == null) throw new MissingFieldException("PlatformHelper.Current");
            field.SetValue(null, platform);
        }

        private static void LoadEnvironment(Assembly preloader)
        {
            var envVars = preloader.GetType("BepInEx.Preloader.EnvVars", true);
            var load = envVars.GetMethod("LoadVars", BindingFlags.NonPublic | BindingFlags.Static)
                       ?? envVars.GetMethod("LoadVars", BindingFlags.Public | BindingFlags.Static);
            if (load == null) throw new MissingMethodException("EnvVars.LoadVars");
            load.Invoke(null, null);
        }

        private static void SetPaths(Assembly bepinex, string invokePath, string processPath)
        {
            var utility = bepinex.GetType("BepInEx.Utility", true);
            var parent = utility.GetMethod("ParentDirectory", BindingFlags.Public | BindingFlags.Static);
            if (parent == null) throw new MissingMethodException("Utility.ParentDirectory");
            var rootPath = (string) parent.Invoke(null, new object[] { Path.GetFullPath(invokePath), 2 });

            var searchDirs = Environment.GetEnvironmentVariable("DOORSTOP_DLL_SEARCH_DIRS");
            var paths = bepinex.GetType("BepInEx.Paths", true);
            var setter = paths.GetMethod("SetExecutablePath",
                BindingFlags.NonPublic | BindingFlags.Public | BindingFlags.Static);
            if (setter == null) throw new MissingMethodException("Paths.SetExecutablePath");

            setter.Invoke(null, new object[]
            {
                processPath,
                rootPath,
                Environment.GetEnvironmentVariable("DOORSTOP_MANAGED_FOLDER_DIR"),
                string.IsNullOrEmpty(searchDirs) ? new string[0] : searchDirs.Split(Path.PathSeparator),
            });
        }

        private static void LoadCriticalAssemblies()
        {
            foreach (var name in CriticalAssemblies)
            {
                try
                {
                    Load(name);
                }
                catch (Exception)
                {
                    // Tak samo jak BepInEx: brak jednej z nich nie powinien przerwać startu.
                }
            }
        }

        private static Assembly ResolveFromCore(object sender, ResolveEventArgs args)
        {
            try
            {
                var name = new AssemblyName(args.Name);
                return Assembly.LoadFile(Path.Combine(_coreDirectory, name.Name + ".dll"));
            }
            catch (Exception)
            {
                return null;
            }
        }
    }
}
