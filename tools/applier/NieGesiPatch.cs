// Aplikator łatek Nie gęsi — jeden plik obok łatki, bez instalacji.
//
// Nakłada łatkę formatu 2 z tools/patch.py: nagłówek tekstowy z sumami kontrolnymi,
// potem lista operacji „skopiuj z oryginału" / „wstaw bajty" spakowana DEFLATE.
// Wszystko z .NET Framework 4, który jest na każdym Windowsie od lat — żadnej biblioteki.
//
// Użycie:
//   NieGesiPatch.exe                          szuka łatki obok siebie, gra = katalog programu
//   NieGesiPatch.exe <katalog gry> [łatka]
//   NieGesiPatch.exe --przywroc [katalog gry] [łatka]
//
// Kod celowo w C# 5, żeby kompilował go także csc.exe dołączony do samego Windowsa.

using System;
using System.Collections.Generic;
using System.IO;
using System.IO.Compression;
using System.Security.Cryptography;
using System.Text;
using System.Windows.Forms;

static class NieGesiPatch
{
    const string Magic = "NIEGESI-PATCH";
    const string Format = "2";
    const string BackupSuffix = ".przed-spolszczeniem";

    class Failure : Exception
    {
        public Failure(string message) : base(message) { }
    }

    [STAThread]
    static int Main(string[] args)
    {
        try { Console.OutputEncoding = Encoding.UTF8; } catch (IOException) { }
        Console.WriteLine("Nie gęsi — nakładanie spolszczenia");
        Console.WriteLine();

        int code;
        try
        {
            code = Run(new List<string>(args));
        }
        catch (Failure failure)
        {
            Console.WriteLine("BŁĄD: " + failure.Message);
            Console.WriteLine();
            Console.WriteLine("Nic nie zostało zmienione.");
            code = 1;
        }
        catch (Exception error)
        {
            Console.WriteLine("Nieoczekiwany błąd: " + error);
            code = 2;
        }

        // Po dwukliku okno zamknęłoby się, zanim gracz przeczyta wynik.
        if (!Console.IsInputRedirected)
        {
            Console.WriteLine();
            Console.Write("Naciśnij Enter, aby zamknąć.");
            Console.ReadLine();
        }
        return code;
    }

    static int Run(List<string> args)
    {
        bool restore = args.Remove("--przywroc");
        string here = AppDomain.CurrentDomain.BaseDirectory;

        string patchPath = args.Count > 1 ? args[1] : FindPatch(here);
        Dictionary<string, string> header;
        byte[] payload;
        ReadPatch(File.ReadAllBytes(patchPath), out header, out payload);
        Console.WriteLine("Łatka:  " + Path.GetFileName(patchPath));

        string gameDir = args.Count > 0 ? args[0] : here;
        string relative = header["file"].Replace('/', Path.DirectorySeparatorChar);
        string target = Path.Combine(gameDir, relative);
        if (!File.Exists(target) && args.Count == 0)
        {
            Console.WriteLine("Nie widzę " + relative + " obok programu. Wskaż katalog gry.");
            gameDir = AskForFolder(header["file"]);
            target = Path.Combine(gameDir, relative);
        }
        if (!File.Exists(target))
            throw new Failure("Nie znalazłem pliku gry: " + target +
                              "\nWypakuj paczkę do katalogu gry albo podaj go jako parametr.");
        Console.WriteLine("Plik:   " + target);
        Console.WriteLine();

        string backup = target + BackupSuffix;
        if (restore)
            return Restore(target, backup, header);

        Console.WriteLine("Sprawdzam sumę kontrolną…");
        byte[] source = File.ReadAllBytes(target);
        string digest = Sha256(source);
        if (digest == header["target-sha256"])
        {
            Console.WriteLine("Spolszczenie jest już wgrane.");
            if (Console.IsInputRedirected || !File.Exists(backup))
                return 0;
            Console.Write("Przywrócić oryginał gry? [t/N] ");
            string answer = (Console.ReadLine() ?? "").Trim().ToLowerInvariant();
            return answer == "t" || answer == "tak" ? Restore(target, backup, header) : 0;
        }
        if (digest != header["source-sha256"])
            throw new Failure("Ten plik gry nie jest tym, pod który zrobiono łatkę.\n" +
                              "  oczekiwano " + header["source-sha256"] + "\n" +
                              "  jest       " + digest + "\n" +
                              "Jeśli gra dostała aktualizację, potrzebna jest nowa łatka.");

        Console.WriteLine("Nakładam łatkę…");
        byte[] result = Apply(source, Inflate(payload), long.Parse(header["target-size"]));
        if (Sha256(result) != header["target-sha256"])
            throw new Failure("Odtworzony plik ma inną sumę kontrolną niż powinien.");

        // Najpierw kopia oryginału, potem zapis do pliku tymczasowego i dopiero podmiana —
        // przerwanie w połowie nie zostawia w grze uszkodzonego pliku.
        if (!File.Exists(backup))
            File.Copy(target, backup);
        string temporary = target + ".niegesi-tmp";
        File.WriteAllBytes(temporary, result);
        File.Delete(target);
        File.Move(temporary, target);

        Console.WriteLine();
        Console.WriteLine("Gotowe. Spolszczenie wgrane.");
        Console.WriteLine("Kopia oryginału: " + backup);
        return 0;
    }

    static int Restore(string target, string backup, Dictionary<string, string> header)
    {
        if (!File.Exists(backup))
            throw new Failure("Nie ma kopii oryginału (" + backup + ").\n" +
                              "Zweryfikuj pliki gry w Steamie albo GOG Galaxy.");
        if (Sha256(File.ReadAllBytes(backup)) != header["source-sha256"])
            throw new Failure("Kopia " + backup + " nie jest oryginałem, pod który zrobiono łatkę.");
        File.Copy(backup, target, true);
        File.Delete(backup);
        Console.WriteLine("Przywrócono oryginał.");
        return 0;
    }

    static string FindPatch(string directory)
    {
        string[] found = Directory.GetFiles(directory, "*.patch");
        if (found.Length == 1)
            return found[0];
        if (found.Length == 0)
            throw new Failure("Nie ma pliku .patch obok programu. Wypakuj całą paczkę razem.");
        throw new Failure("Obok programu jest kilka plików .patch — zostaw jeden albo podaj go jako parametr.");
    }

    static string AskForFolder(string relative)
    {
        using (FolderBrowserDialog dialog = new FolderBrowserDialog())
        {
            dialog.Description = "Wskaż katalog gry — ten, w którym leży " + relative.Split('/')[0];
            dialog.ShowNewFolderButton = false;
            if (dialog.ShowDialog() != DialogResult.OK)
                throw new Failure("Nie wybrano katalogu gry.");
            return dialog.SelectedPath;
        }
    }

    static void ReadPatch(byte[] raw, out Dictionary<string, string> header, out byte[] payload)
    {
        int split = -1;
        for (int i = 0; i + 1 < raw.Length; i++)
            if (raw[i] == '\n' && raw[i + 1] == '\n') { split = i; break; }
        if (split <= 0)
            throw new Failure("To nie jest łatka Nie gęsi.");

        string[] lines = Encoding.UTF8.GetString(raw, 0, split).Split('\n');
        if (lines[0] != Magic)
            throw new Failure("To nie jest łatka Nie gęsi.");

        header = new Dictionary<string, string>();
        for (int i = 1; i < lines.Length; i++)
        {
            int space = lines[i].IndexOf(' ');
            if (space > 0)
                header[lines[i].Substring(0, space)] = lines[i].Substring(space + 1);
        }
        string format;
        if (!header.TryGetValue("format", out format) || format != Format)
            throw new Failure("Nieznana wersja formatu łatki: " + format + ". Pobierz nowszy aplikator.");

        payload = new byte[raw.Length - split - 2];
        Buffer.BlockCopy(raw, split + 2, payload, 0, payload.Length);
    }

    static byte[] Inflate(byte[] data)
    {
        using (DeflateStream inflater = new DeflateStream(new MemoryStream(data), CompressionMode.Decompress))
        using (MemoryStream output = new MemoryStream())
        {
            inflater.CopyTo(output);
            return output.ToArray();
        }
    }

    static long ReadVarint(byte[] data, ref int at)
    {
        long value = 0;
        int shift = 0;
        while (true)
        {
            byte current = data[at++];
            value |= (long)(current & 0x7F) << shift;
            shift += 7;
            if ((current & 0x80) == 0)
                return value;
        }
    }

    static byte[] Apply(byte[] source, byte[] ops, long size)
    {
        byte[] output = new byte[size];
        long written = 0, cursor = 0;
        int at = 0;
        while (true)
        {
            byte op = ops[at++];
            if (op == 0)
                break;
            long length = ReadVarint(ops, ref at);
            if (written + length > size)
                throw new Failure("Łatka daje za duży plik.");
            if (op == 1)
            {
                long delta = ReadVarint(ops, ref at);
                long origin = cursor + ((delta >> 1) ^ -(delta & 1));
                if (origin < 0 || origin + length > source.Length)
                    throw new Failure("Łatka sięga poza oryginał.");
                Array.Copy(source, origin, output, written, length);
                cursor = origin + length;
            }
            else if (op == 2)
            {
                Array.Copy(ops, at, output, written, length);
                at += (int)length;
            }
            else
            {
                throw new Failure("Nieznana operacja w łatce: " + op);
            }
            written += length;
        }
        if (written != size)
            throw new Failure("Łatka dała plik innej długości niż powinna.");
        return output;
    }

    static string Sha256(byte[] data)
    {
        using (SHA256 hasher = SHA256.Create())
        {
            byte[] hash = hasher.ComputeHash(data);
            StringBuilder text = new StringBuilder(hash.Length * 2);
            foreach (byte b in hash)
                text.Append(b.ToString("x2"));
            return text.ToString();
        }
    }
}
