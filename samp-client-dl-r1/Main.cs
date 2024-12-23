using System;
using System.Windows.Forms;
using Client_DL_R1_SPC.Core;

namespace Client_DL_R1_SPC
{
    internal static class Program
    {
        [STAThread]
        static void Main() 
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new Installer_Client());
        }
    }
}