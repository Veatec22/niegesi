// Zrzut literałów tekstowych z Assembly-CSharp.dll: "Typ::metoda<TAB>literał" w każdej linii.
// Klucze strings.txt w Rain World to angielskie teksty wpisane w kod, więc to mówi,
// gdzie w grze dany wpis się pojawia (menu opcji, HUD, samouczek...).
// Kompiluje i uruchamia extract.py; Mono.Cecil.dll bierze z katalogu Managed gry.
using System;
using System.IO;
using System.Text;
using Mono.Cecil;
using Mono.Cecil.Cil;

static class StrMap
{
    static string Escape(string s)
    {
        return s.Replace("\\", "\\\\").Replace("\t", "\\t").Replace("\r", "\\r").Replace("\n", "\\n");
    }

    static void Main(string[] args)
    {
        var resolver = new DefaultAssemblyResolver();
        resolver.AddSearchDirectory(Path.GetDirectoryName(args[0]));
        var assembly = AssemblyDefinition.ReadAssembly(args[0], new ReaderParameters { AssemblyResolver = resolver });
        using (var output = new StreamWriter(args[1], false, new UTF8Encoding(false)))
        {
            foreach (var type in assembly.MainModule.GetTypes())
                foreach (var method in type.Methods)
                {
                    if (!method.HasBody) continue;
                    foreach (var instruction in method.Body.Instructions)
                        if (instruction.OpCode == OpCodes.Ldstr)
                            output.WriteLine(type.FullName + "::" + method.Name + "\t" + Escape((string)instruction.Operand));
                }
        }
    }
}
