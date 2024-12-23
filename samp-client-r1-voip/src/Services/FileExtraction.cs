using System;
using System.Collections.Generic;
using System.IO;
using System.IO.Compression;
using System.Reflection;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Linq;

namespace Client_R1_Voip_SPC.Services
{
    public class File_Extraction
    {
        public async Task<List<string>> ExtractClient_Files(string Target_Path, IProgress<(int progress, string fileName)> progress)
        {
            var Current_Assembly = Assembly.GetExecutingAssembly();
            var Zip_Resource = Current_Assembly.GetManifestResourceNames().FirstOrDefault(Res => Res.Contains("archives") && Res.EndsWith("samp-client-r1-voip.zip"));

            if (Zip_Resource == null)
            {
                MessageBox.Show("Error: ZIP file not found.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                Application.Exit();
                return new List<string>();
            }

            using var Zip_Stream = Current_Assembly.GetManifestResourceStream(Zip_Resource);
            using var Temp_Buffer = new MemoryStream();
            await Zip_Stream.CopyToAsync(Temp_Buffer);
            Temp_Buffer.Position = 0;

            using var Zip_Archive = new ZipArchive(Temp_Buffer, ZipArchiveMode.Read);
            var Total_Files = Zip_Archive.Entries.Count;
            var Processed_Files = new List<string>();

            int delayPerFile = 5000 / Total_Files;

            for (int File_Index = 0; File_Index < Total_Files; File_Index++)
            {
                var Current_Entry = Zip_Archive.Entries[File_Index];
                var File_Target_Path = Path.Combine(Target_Path, Current_Entry.FullName);

                if (string.IsNullOrEmpty(Current_Entry.Name))
                    Directory.CreateDirectory(File_Target_Path);
                else
                {
                    Directory.CreateDirectory(Path.GetDirectoryName(File_Target_Path));
                    Current_Entry.ExtractToFile(File_Target_Path, true);
                    Processed_Files.Add(Current_Entry.FullName);
                }

                int Completion_Percent = (int)((File_Index + 1) * 100.0 / Total_Files);
                progress.Report((Completion_Percent, Current_Entry.FullName));
                
                await Task.Delay(delayPerFile);
            }

            return Processed_Files;
        }
    }
}