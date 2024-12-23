using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;
using System.IO;
using System.Threading;
using System.Threading.Tasks;
using System.Reflection;
using System.Linq;
using Client_R3_Voip_SPC.Models;
using Client_R3_Voip_SPC.Services;
using Client_R3_Voip_SPC.UI;

namespace Client_R3_Voip_SPC.Core
{
    public partial class Installer_Client : Form
    {
        private File_Extraction Extraction_Module;
        private Language Language_Module;
        private Language_Mapping LanguageMapping_Module;
        private Social_Networks SocialNetworks_Module;

        private Label Description_Label, Status_Label;
        private Custom_ProgressBar Progress_Bar;
        private ListBox ExtractedFiles_List;
        private string Selected_Path = string.Empty;
        private string Current_Language = "Português";
        private List<string> Available_Languages;

        public Installer_Client()
        {
            Language_Module = new Language();
            LanguageMapping_Module = new Language_Mapping();
            Extraction_Module = new File_Extraction();
            SocialNetworks_Module = new Social_Networks();

            SetupClient_Style();
            Load_Languages();
            CreateLanguage_Buttons();
        }

        private void SetupClient_Style()
        {
            Text = "Client R3 Voip - SPC";
            Size = new Size(700, 500);
            StartPosition = FormStartPosition.CenterScreen;
            FormBorderStyle = FormBorderStyle.FixedSingle;
            MaximizeBox = false;
            BackColor = Colors_Client.Background;

            var Get_Assembly = Assembly.GetExecutingAssembly();
            var Resource_Name = Get_Assembly.GetManifestResourceNames().FirstOrDefault(r => r.Contains("icons.social") && r.EndsWith("spc-window.ico"));

            if (Resource_Name == null)
                return;

            using (Stream Stream = Get_Assembly.GetManifestResourceStream(Resource_Name))
            {
                if (Stream != null)
                    Icon = new Icon(Stream);
            }
        }

        private void Load_Languages()
        {
            Available_Languages = Language_Module.GetAvailable_Languages();

            if (Available_Languages.Count == 0)
                MessageBox.Show("Error: No translation files found.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
        }

        private void Load_Translations(string Language) =>
            Language_Module.Load_Translations(Language);

        private string Translate(string Key) => 
            Language_Module.Translate(Key);

        private void CreateLanguage_Buttons()
        {
            Controls.Clear();

            AddCentered_Label("Languages", 16);

            Panel Button_Panel = new Panel
            {
                AutoScroll = true,
                Dock = DockStyle.None,
                Location = new Point(0, 140),
                Width = this.ClientSize.Width,
                Height = this.ClientSize.Height - 140,
                BackColor = this.BackColor
            };

            int Icon_Size = 50;
            int Button_Width = 200;
            int Button_Height = 120;
            int Padding = 20;
            int MaxButtons_PerRow = 3;

            for (int i = 0; i < Available_Languages.Count; i++)
            {
                var Language = Available_Languages[i];
                var Language_Button = CreateLanguage_Button(Language, Icon_Size, Button_Width, Button_Height, i, MaxButtons_PerRow, Padding);
                Button_Panel.Controls.Add(Language_Button);
            }

            Panel Bottom_Space = new Panel
            {
                Height = 20,
                Width = Button_Width,
                Left = Padding,
                Top = ((Available_Languages.Count - 1) / MaxButtons_PerRow + 1) * (Button_Height + Padding)
            };
            Button_Panel.Controls.Add(Bottom_Space);
            Controls.Add(Button_Panel);
        }

        private Button CreateLanguage_Button(string Language, int Icon_Size, int Button_Width, int Button_Height, int Index, int MaxButtons_PerRow, int Padding)
        {
            var Language_Button = new Button
            {
                Text = Language,
                BackColor = Colors_Client.Secondary,
                ForeColor = Colors_Client.Text,
                FlatStyle = FlatStyle.Flat,
                Width = Button_Width,
                Height = Button_Height,
                Left = Padding + 2 + (Index % MaxButtons_PerRow) * (Button_Width + Padding),
                Top = (Index / MaxButtons_PerRow) * (Button_Height + Padding),
                Font = new Font("Segoe UI", 10, FontStyle.Bold)
            };

            Language_Button.FlatAppearance.BorderColor = Colors_Client.Accent;
            Language_Button.FlatAppearance.MouseOverBackColor = Colors_Client.Hover;

            var Flag = GetFlag_Image(Language, Icon_Size);
            if (Flag != null)
            {
                Language_Button.Image = Flag;
                Language_Button.ImageAlign = ContentAlignment.MiddleCenter;
                Language_Button.TextAlign = ContentAlignment.BottomCenter;
            }

            Language_Button.Click += (s, e) =>
            {
                Current_Language = ((Button)s).Text;
                Load_Translations(Current_Language);
                Initialize_Installer();
            };

            return Language_Button;
        }

        private Bitmap GetFlag_Image(string Language, int Icon_Size)
        {
            var Get_Assembly = Assembly.GetExecutingAssembly();
            var Image_Code = LanguageMapping_Module.GetImage_Code(Language);
            
            var Flag_Resource_Name = Get_Assembly.GetManifestResourceNames().FirstOrDefault(r => r.Contains("icons.languages") && r.EndsWith($"{Image_Code}.png", StringComparison.InvariantCultureIgnoreCase));
            
            if (Flag_Resource_Name != null)
            {
                using var Stream = Get_Assembly.GetManifestResourceStream(Flag_Resource_Name);
                return new Bitmap(Image.FromStream(Stream), new Size(Icon_Size, Icon_Size));
            }
            return null;
        }

        private void AddCentered_Label(string Text, int Font_Size)
        {
            var Title_Label = new Label
            {
                Text = Text,
                Font = new Font("Segoe UI", Font_Size, FontStyle.Bold),
                ForeColor = Colors_Client.Text,
                Top = 50,
                AutoSize = true
            };

            using (var Graphics = CreateGraphics())
            {
                SizeF Text_Size = Graphics.MeasureString(Text, Title_Label.Font);
                Title_Label.Left = (this.ClientSize.Width - (int)Text_Size.Width) / 2;
            }

            Controls.Add(Title_Label);
        }

        private void Initialize_Installer()
        {
            Controls.Clear();

            AddCentered_Label(Translate("client_installer_title"), 16);

            Description_Label = new Label
            {
                Text = Translate("client_installer_description"),
                Top = 105,
                Left = 170,
                ForeColor = Colors_Client.Text,
                AutoSize = true,
                MaximumSize = new Size(360, 0),
                Font = new Font("Segoe UI", 9.1f, FontStyle.Regular)
            };
            Controls.Add(Description_Label);

            var Continue_Button = CreateStyled_Button(Translate("continue"));
            Continue_Button.Top = 409;
            Continue_Button.Left = 540;
            Continue_Button.Width = 130;
            Continue_Button.Height = 40;
            Continue_Button.Click += (sender, e) => Selecting_Folder(); 
            Controls.Add(Continue_Button);
        }

        private void Selecting_Folder()
        {
            Controls.Clear();

            AddCentered_Label(Translate("folder_title"), 16);

            Description_Label = new Label
            {
                Text = Translate("folder_description"),
                Top = 105,
                Left = 170,
                ForeColor = Colors_Client.Text,
                AutoSize = true,
                MaximumSize = new Size(360, 0),
                Font = new Font("Segoe UI", 9.1f, FontStyle.Regular)
            };
            Controls.Add(Description_Label);

            var Title_Label = new Label
            {
                Text = Translate("selected_folder_title"),
                Font = new Font("Segoe UI", 13, FontStyle.Bold),
                ForeColor = Colors_Client.Text,
                Top = 265,
                Left = 100,
                AutoSize = true
            };
            Controls.Add(Title_Label);

            Status_Label = new Label
            {
                Text = Translate("no_folder_selected"),
                Top = 300,
                Left = 20,
                MaximumSize = new Size(465, 0),
                ForeColor = Colors_Client.Text,
                AutoSize = true
            };
            Controls.Add(Status_Label);

            var SelectFolder_Button = CreateStyled_Button(Translate("select_folder"));
            SelectFolder_Button.Top = 300;
            SelectFolder_Button.Left = 525;
            SelectFolder_Button.Width = 140;
            SelectFolder_Button.Height = 50;

            void HandleFolder_Selection(object sender, EventArgs e)
            {
                using var Dialog = new FolderBrowserDialog();
                if (Dialog.ShowDialog() == DialogResult.OK)
                {
                    Selected_Path = Dialog.SelectedPath;
                    Status_Label.Text = $"{Translate("selected_folder")} {Selected_Path}";
                    Status_Label.ForeColor = Colors_Client.Text;
                    
                    SelectFolder_Button.Click -= HandleFolder_Selection;
                    SelectFolder_Button.Text = Translate("continue");
                    SelectFolder_Button.Click += Verify_Folder;

                    if (!Controls.OfType<Button>().Any(b => b.Text == Translate("other_folder")))
                    {
                        var AnotherFolder_Button = CreateStyled_Button(Translate("other_folder"));
                        AnotherFolder_Button.Top = SelectFolder_Button.Top + SelectFolder_Button.Height + 10;
                        AnotherFolder_Button.Left = SelectFolder_Button.Left;
                        AnotherFolder_Button.Width = SelectFolder_Button.Width;
                        AnotherFolder_Button.Height = SelectFolder_Button.Height;
                        AnotherFolder_Button.Click += HandleFolder_Selection;
                        Controls.Add(AnotherFolder_Button);
                    }
                }
            }

            SelectFolder_Button.Click += HandleFolder_Selection;
            Controls.Add(SelectFolder_Button);
        }

        private void Verify_Folder(object Sender, EventArgs E)
        {
            Controls.Clear();

            AddCentered_Label(Translate("folder_verification_title"), 16);

            Status_Label = new Label
            {
                Text = Translate("verifying_folder"),
                Top = 125,
                Left = 47,
                ForeColor = Colors_Client.Text,
                AutoSize = true
            };
            Controls.Add(Status_Label);

            Progress_Bar = new Custom_ProgressBar
            {
                Top = 150,
                Left = 50,
                Width = 600,
                Value = 0,
                Maximum = 100,
                GradientStart_Color = Colors_Client.Accent,
                GradientEnd_Color = Color.FromArgb(Colors_Client.Accent.R + 20, Colors_Client.Accent.G + 20, Colors_Client.Accent.B + 20),
                Background_Color = Colors_Client.Secondary,
                Animation_Speed = 8,
                Corner_Radius = 5,
                Show_Percentage = true
            };
            Progress_Bar.OnCompletion += (s, e) => {
                if (!IsDisposed)
                {
                    Selecting_Folder();
                    
                    if (Path.GetFileName(Selected_Path) != "Grand Theft Auto San Andreas")
                    {
                        Status_Label.Text = Translate("invalid_folder");
                        Status_Label.ForeColor = Color.Red;
                    }
                    else if (!File.Exists(Path.Combine(Selected_Path, "gta_sa.exe")))
                    {
                        Status_Label.Text = Translate("invalid_file");
                        Status_Label.ForeColor = Color.Red;
                    }
                    else
                        ShowDownload_Screen();
                }
            };
            Controls.Add(Progress_Bar);

            new Thread(() =>
            {
                for (int i = 0; i <= 100; i += 20)
                {
                    Thread.Sleep(1000);
                    
                    if (Progress_Bar.IsDisposed)
                        return;

                    Progress_Bar.Invoke(new Action(() => 
                    {
                        if (!Progress_Bar.IsDisposed)
                            Progress_Bar.Value = i;
                    }));
                }
            })
            { 
                IsBackground = true
            }.Start();
        }

        private void ShowDownload_Screen()
        {
            Controls.Clear();
            
            AddCentered_Label(Translate("install_client_title"), 16);

            Description_Label = new Label
            {
                Text = Translate("install_client_description"),
                Top = 105,
                Left = 170,
                ForeColor = Colors_Client.Text,
                AutoSize = true,
                MaximumSize = new Size(360, 0),
                Font = new Font("Segoe UI", 9.1f, FontStyle.Regular)
            };
            Controls.Add(Description_Label);

            var Cancel_Button = CreateStyled_Button(Translate("cancel"));
            Cancel_Button.Top = 350;
            Cancel_Button.Left = 100;
            Cancel_Button.Click += Handle_Cancellation;
            Controls.Add(Cancel_Button);

            var Proceed_Button = CreateStyled_Button(Translate("continue"));
            Proceed_Button.Top = 350;
            Proceed_Button.Left = 400;
            Proceed_Button.Click += Start_Download;
            Controls.Add(Proceed_Button);
        }

        private void Handle_Cancellation(object Sender, EventArgs E)
        {
            Controls.Clear();

            AddCentered_Label(Translate("canceling_downloand_title"), 16);

            Status_Label = new Label
            {
                Text = Translate("canceling_downloand"),
                Top = 125,
                Left = 47,
                ForeColor = Colors_Client.Text,
                AutoSize = true
            };
            Controls.Add(Status_Label);

            Progress_Bar = new Custom_ProgressBar
            {
                Top = 150,
                Left = 50,
                Width = 600,
                Value = 0,
                Maximum = 100,
                GradientStart_Color = Colors_Client.Accent,
                GradientEnd_Color = Color.FromArgb(Colors_Client.Accent.R + 20, Colors_Client.Accent.G + 20, Colors_Client.Accent.B + 20),
                Background_Color = Colors_Client.Secondary,
                Animation_Speed = 8,
                Corner_Radius = 5,
                Show_Percentage = true
            };
            Progress_Bar.OnCompletion += (s, e) => {
                if (!IsDisposed)
                    ShowSocial_Networks();
            };
            Controls.Add(Progress_Bar);

            new Thread(() =>
            {
                for (int i = 0; i <= 100; i += 20)
                {
                    Thread.Sleep(1000);

                    if (Progress_Bar.IsDisposed)
                        return;

                    Progress_Bar.Invoke(new Action(() => 
                    {
                        if (!Progress_Bar.IsDisposed)
                            Progress_Bar.Value = i;
                    }));
                }
            })
            { 
                IsBackground = true
            }.Start();
        }

        private async Task<List<string>> ExtractClient_Files()
        {
            var progress = new Progress<(int progress, string fileName)>(update => 
            {
                Progress_Bar.Value = update.progress;
                ExtractedFiles_List.Items.Add(update.fileName);
            });
            
            return await Extraction_Module.ExtractClient_Files(Selected_Path, progress);
        }

        private async void Start_Download(object Sender, EventArgs E)
        {
            Controls.Clear();

            AddCentered_Label(Translate("file_extraction_title"), 16);

            Status_Label = new Label
            {
                Text = Translate("extracting_files"),
                Top = 125,
                Left = 47,
                ForeColor = Colors_Client.Text,
                AutoSize = true
            };
            Controls.Add(Status_Label);

            Progress_Bar = new Custom_ProgressBar
            {
                Top = 150,
                Left = 50,
                Width = 600,
                Value = 0,
                Maximum = 100,
                GradientStart_Color = Colors_Client.Accent,
                GradientEnd_Color = Color.FromArgb(Colors_Client.Accent.R + 20, Colors_Client.Accent.G + 20, Colors_Client.Accent.B + 20),
                Background_Color = Colors_Client.Secondary,
                Animation_Speed = 8,
                Corner_Radius = 5,
                Show_Percentage = true
            };
            Controls.Add(Progress_Bar);

            ExtractedFiles_List = new ListBox
            {
                Top = 200,
                Left = 50,
                Width = 600,
                Height = 200,
                BackColor = Colors_Client.Secondary,
                ForeColor = Colors_Client.Text
            };
            Controls.Add(ExtractedFiles_List);

            var extractedFiles = await ExtractClient_Files();

            Progress_Bar.OnCompletion += (s, e) => {
                if (!IsDisposed)
                    ShowCompletion_Screen(extractedFiles);
            };
        }

        private void ShowCompletion_Screen(List<string> Extracted_Files)
        {
            Controls.Clear();

            AddCentered_Label(Translate("extraction_completed_title"), 16);

            ExtractedFiles_List = new ListBox
            {
                Top = 130,
                Left = 50,
                Width = 600,
                Height = 220,
                BackColor = Colors_Client.Secondary,
                ForeColor = Colors_Client.Text
            };
            ExtractedFiles_List.Items.AddRange(Extracted_Files.ToArray());
            Controls.Add(ExtractedFiles_List);

            var Conclude_Button = CreateStyled_Button(Translate("finish"));
            Conclude_Button.Top = 380;
            Conclude_Button.Left = 250;
            Conclude_Button.Click += (s, e) => ShowSocial_Networks();
            Controls.Add(Conclude_Button);
        }

        private void ShowSocial_Networks()
        {
            Controls.Clear();

            AddCentered_Label(Translate("social_title"), 16);

            string[] Social_Networks = { 
                "Discord SPC", 
                "YouTube", 
                "Instagram", 
                "TikTok", 
                "GitHub" 
            };

            int Icon_Size = 35;
            int Button_Width = 200;
            int Button_Height = 50;
            int Padding = 20;

            for (int i = 0; i < Social_Networks.Length; i++)
            {
                var Social_Button = CreateSocial_NetworkButton(Social_Networks[i], Icon_Size, Button_Width, Button_Height, i, Padding);
                Controls.Add(Social_Button);
            }

            var Close_Button = CreateStyled_Button(Translate("close"));
            Close_Button.Top = 409;
            Close_Button.Left = 540;
            Close_Button.Width = 130;
            Close_Button.Height = 40;
            Close_Button.Click += (s, e) => Application.Exit();
            Controls.Add(Close_Button);
        }

        private Button CreateSocial_NetworkButton(string Network, int Icon_Size, int Button_Width, int Button_Height, int Index, int Padding)
        {
            var Social_Button = new Button
            {
                Text = Network,
                BackColor = Colors_Client.Secondary,
                ForeColor = Colors_Client.Text,
                FlatStyle = FlatStyle.Flat,
                Width = Button_Width,
                Height = Button_Height,
                Top = 150 + ((Index / 2) * (Button_Height + Padding)),
                Left = 145 + ((Index % 2) * (Button_Width + Padding)),
                Font = new Font("Segoe UI", 10, FontStyle.Bold),
                ImageAlign = ContentAlignment.MiddleLeft,
                TextAlign = ContentAlignment.MiddleCenter,
                Padding = new Padding(10, 0, -5, 0)
            };

            Social_Button.FlatAppearance.BorderColor = Colors_Client.Accent;
            Social_Button.FlatAppearance.MouseOverBackColor = Colors_Client.Hover;

            var Icon = GetSocial_NetworkIcon(Network, Icon_Size);
            if (Icon != null)
                Social_Button.Image = Icon;

            Social_Button.Click += (s, e) => 
            {
                string Button_Text = ((Button)s).Text;
                OpenSocial_Network(Button_Text);
            };

            return Social_Button;
        }

        private Bitmap GetSocial_NetworkIcon(string Network, int Icon_Size)
        {
            var Get_Assembly = Assembly.GetExecutingAssembly();
            var Icon_Resource_Name = Get_Assembly.GetManifestResourceNames().FirstOrDefault(r => r.Contains("icons.social") && r.EndsWith($"{Network.ToLower().Replace(" ", "-")}.png"));

            if (Icon_Resource_Name != null)
            {
                using var Stream = Get_Assembly.GetManifestResourceStream(Icon_Resource_Name);
                return new Bitmap(Image.FromStream(Stream), new Size(Icon_Size, Icon_Size));
            }

            return null;
        }

        private void OpenSocial_Network(string Network) =>
            SocialNetworks_Module.OpenSocial_Network(Network);

        private Button CreateStyled_Button(string Text)
        {
            return new Button
            {
                Text = Text,
                BackColor = Colors_Client.Accent,
                ForeColor = Colors_Client.Text,
                FlatStyle = FlatStyle.Flat,
                Font = new Font("Segoe UI", 10, FontStyle.Bold),
                Width = 200,
                Height = 50,
                Cursor = Cursors.Hand
            };
        }
    }
}