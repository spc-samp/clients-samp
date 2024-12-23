using System.Diagnostics;

namespace Client_DL_R1_SPC.Services
{
    public class Social_Networks
    {
        public void OpenSocial_Network(string Network_Name)
        {
            string Network_Url = Network_Name switch
            {
                "Discord SPC" => "https://discord.gg/3fApZh66Tf",
                "YouTube" => "https://youtube.com/@spc-samp",
                "Instagram" => "https://instagram.com/spc.samp/",
                "TikTok" => "https://tiktok.com/@spc.samp",
                "GitHub" => "https://github.com/spc-samp",
                _ => ""
            };

            if (!string.IsNullOrEmpty(Network_Url))
            {
                Process.Start(new ProcessStartInfo
                {
                    FileName = Network_Url,
                    UseShellExecute = true
                });
            }
        }
    }
}