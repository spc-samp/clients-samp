﻿using System;
using System.Windows.Forms;
using Client_R2_SPC.Core;

namespace Client_R2_SPC
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