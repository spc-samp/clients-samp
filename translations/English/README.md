# clients-samp

[![Licença](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![C#](https://img.shields.io/badge/C%23-11.0-blue.svg)](https://docs.microsoft.com/en-us/dotnet/csharp/)
[![.NET](https://img.shields.io/badge/.NET-9.0-purple.svg)](https://dotnet.microsoft.com/)
[![Windows Forms](https://img.shields.io/badge/Windows%20Forms-net9.0--windows-blue)](https://docs.microsoft.com/en-us/dotnet/desktop/winforms/)

This repository contains the source code of various Client SA:MP (San Andreas Multiplayer) installers developed by the SPC (SA-MP Programming Community). These installers were created to provide safe and reliable alternatives to the original mod installers, which are no longer considered trustworthy.

## Languages

- Português: [README](../../)
- Deutsch: [README](../Deutsch/README.md)
- Español: [README](../Espanol/README.md)
- Français: [README](../Francais/README.md)
- Italiano: [README](../Italiano/README.md)
- Polski: [README](../Polski/README.md)
- Русский: [README](../Русский/README.md)
- Svenska: [README](../Svenska/README.md)
- Türkçe: [README](../Turkce/README.md)

## Index

- [clients-samp](#clients-samp)
  - [Languages](#languages)
  - [Index](#index)
  - [Overview](#overview)
  - [Available Versions](#available-versions)
  - [Project Structure](#project-structure)
  - [Features](#features)
  - [Installation](#installation)
  - [Compilation](#compilation)
    - [Prerequisites](#prerequisites)
    - [How to compile](#how-to-compile)
  - [Code Structure and Components](#code-structure-and-components)
    - [Main Components](#main-components)
      - [Installer Client (`InstallerClient.cs`)](#installer-client-installerclientcs)
    - [Services](#services)
      - [File Extraction Service (`FileExtraction.cs`)](#file-extraction-service-fileextractioncs)
      - [Language Support (`Language.cs`)](#language-support-languagecs)
      - [Language Mapping Service (`LanguageMapping.cs`)](#language-mapping-service-languagemappingcs)
      - [Social Networks Service (`SocialNetworks.cs`)](#social-networks-service-socialnetworkscs)
      - [Custom Interface Components](#custom-interface-components)
        - [Progress Bar (`CustomProgressBar.cs`)](#progress-bar-customprogressbarcs)
        - [Theme Colors (`Colors.cs`)](#theme-colors-colorscs)
    - [Security Features](#security-features)
      - [Administrative Privileges](#administrative-privileges)
      - [Assembly Signing](#assembly-signing)
    - [Internationalization](#internationalization)
      - [Translation System](#translation-system)
      - [Flag Icons](#flag-icons)
  - [Project Configuration (.csproj)](#project-configuration-csproj)
    - [Basic Settings](#basic-settings)
    - [Version and Company Information](#version-and-company-information)
    - [Runtime Settings](#runtime-settings)
    - [Embedded Resources](#embedded-resources)
    - [Important Notes](#important-notes)
  - [Screenshots](#screenshots)
  - [License](#license)
    - [What you can do ✅](#what-you-can-do-)
    - [What you must do ⚠️](#what-you-must-do-️)
    - [What you cannot do ❌](#what-you-cannot-do-)

## Overview

The project aims to provide secure and reliable installers for different versions of the SA:MP mod. Each installer is developed in C# using Windows Forms, offering a modern and user-friendly interface with support for multiple languages and a window with social media links.

## Available Versions

The repository includes the following Client versions:

- `samp-client-dl-r1`: Installer for Client DL R1
- `samp-client-r1`: Installer for Client R1
- `samp-client-r1-voip`: Client R1 with SAMPVOICE integration
- `samp-client-r2`: Installer for Client R2
- `samp-client-r3`: Installer for Client R3
- `samp-client-r3-voip`: Client R3 with SAMPVOICE integration
- `samp-client-r4`: Installer for Client R4
- `samp-client-r5`: Installer for Client R5

## Project Structure

Each Client version follows a consistent project structure:

```
clients-samp/
└── samp-client-v/
    ├── archives/
    │   └── samp-client-{v}.zip
    ├── icons/
    │   ├── languages/
    │   │   └── [language flag icons]
    │   └── social/
    │       └── [social media icons]
    ├── src/
    │   ├── Core/
    │   │   └── InstallerClient.cs
    │   ├── Models/
    │   │   └── Colors.cs
    │   ├── Services/
    │   │   ├── FileExtraction.cs
    │   │   ├── Language.cs
    │   │   ├── LanguageMapping.cs
    │   │   └── SocialNetworks.cs
    │   └── UI/
    │       └── CustomProgressBar.cs
    ├── translations/
    │   └── [30 XML language files]
    ├── adm.manifest
    ├── compile.bat
    ├── Main.cs
    └── samp-client-{v}.csproj
```

## Features

- Support for multiple languages (30 languages)
- Modern and intuitive user interface
- Secure extraction and installation of files
- Game directory validation
- Real-time progress tracking
- Window with social media links
- Optional assembly signing for enhanced security
- Custom progress bar with animations
- Consistent color scheme and style

## Installation

1. Go to the [releases](https://github.com/spc-samp/clients-samp/releases) page of the project
2. Download the latest compiled version of the Client
3. Run it and proceed with the setup

## Compilation

### Prerequisites

- .NET SDK 9.0 or higher
- Windows operating system
- Visual Studio 2022 or higher (optional)
- Visual Studio Code (optional)

### How to compile

The easiest way to compile any version of the Client is by using the provided batch file:

1. Open a terminal in the Client version directory
2. Run the build command:
```bash
.\compile
```

You can also compile directly using the .NET CLI:
```bash
dotnet publish -c Release -r win-x64 --self-contained true -p:PublishSingleFile=true -p:EnableCompressionInSingleFile=true -o ./published
```

> [!NOTE]
> This command will generate a single executable file optimized for 64-bit Windows, containing all necessary dependencies. The executable will be created inside the `published` folder in the project directory.

## Code Structure and Components

### Main Components

#### Installer Client (`InstallerClient.cs`)

The main form that manages the entire installation process. It implements a step-by-step wizard interface:

```csharp
public partial class Installer_Client : Form
{
    // Main modules
    private File_Extraction Extraction_Module;
    private Language Language_Module;
    private Language_Mapping LanguageMapping_Module;
    private Social_Networks SocialNetworks_Module;

    // Interface elements
    private Label Description_Label, Status_Label;
    private Custom_ProgressBar Progress_Bar;
    private ListBox ExtractedFiles_List;
}
```

Main features and responsibilities:

1. **Language Selection**
   ```csharp
   private void CreateLanguage_Buttons()
   {
       // Creates a grid of language buttons with flags
       Panel Button_Panel = new Panel
       {
           AutoScroll = true,
           Dock = DockStyle.None,
           Location = new Point(0, 140),
           Width = this.ClientSize.Width,
           Height = this.ClientSize.Height - 140
       };
       
       // Dynamically create buttons with flags
       for (int i = 0; i < Available_Languages.Count; i++)
       {
           var Language = Available_Languages[i];
           var Language_Button = CreateLanguage_Button(Language, Icon_Size, Button_Width, Button_Height, i, MaxButtons_PerRow, Padding);
           Button_Panel.Controls.Add(Language_Button);
       }
   }
   ```

2. **Select Installation Directory**
   ```csharp
   private void Selecting_Folder()
   {
       // Folder selection dialog with validation
       using var Dialog = new FolderBrowserDialog();
       if (Dialog.ShowDialog() == DialogResult.OK)
       {
           Selected_Path = Dialog.SelectedPath;
           // Validates the GTA:SA installation directory
           if (Path.GetFileName(Selected_Path) != "Grand Theft Auto San Andreas")
           {
               Status_Label.Text = Translate("invalid_folder");
               Status_Label.ForeColor = Color.Red;
           }
       }
   }
   ```

3. **File Extraction Process**
   ```csharp
   private async Task<List<string>> ExtractClient_Files()
   {
       var progress = new Progress<(int progress, string fileName)>(update => 
       {
           Progress_Bar.Value = update.progress;
           ExtractedFiles_List.Items.Add(update.fileName);
       });
       
       return await Extraction_Module.ExtractClient_Files(Selected_Path, progress);
   }
   ```

4. **Window with Social Networks**
   ```csharp
   private void ShowSocial_Networks()
   {
       string[] Social_Networks = { 
           "Discord SPC", 
           "YouTube", 
           "Instagram", 
           "TikTok", 
           "GitHub" 
       };

       // Creates buttons for each social network with icons
       for (int i = 0; i < Social_Networks.Length; i++)
       {
           var Social_Button = CreateSocial_NetworkButton(Social_Networks[i], Icon_Size, Button_Width, Button_Height, i, Padding);
           Controls.Add(Social_Button);
       }
   }
   ```

### Services

#### File Extraction Service (`FileExtraction.cs`)

Manages the secure extraction of files from the SA:MP Client embedded resources:

```csharp
public class File_Extraction
{
    public async Task<List<string>> ExtractClient_Files(string Target_Path, IProgress<(int progress, string fileName)> progress)
    {
        // Loads the embedded ZIP resource
        var Current_Assembly = Assembly.GetExecutingAssembly();
        var Zip_Resource = Current_Assembly.GetManifestResourceNames().FirstOrDefault(Res => Res.Contains("archives") && Res.EndsWith("samp-client-v.zip"));

        using var Zip_Archive = new ZipArchive(Temp_Buffer, ZipArchiveMode.Read);
        var Total_Files = Zip_Archive.Entries.Count;
        var Processed_Files = new List<string>();

        // Extracts files with progress reporting
        for (int File_Index = 0; File_Index < Total_Files; File_Index++)
        {
            var Current_Entry = Zip_Archive.Entries[File_Index];
            var File_Target_Path = Path.Combine(Target_Path, Current_Entry.FullName);

            // Reports progress for interface updates
            int Completion_Percent = (int)((File_Index + 1) * 100.0 / Total_Files);
            progress.Report((Completion_Percent, Current_Entry.FullName));
        }

        return Processed_Files;
    }
}
```

#### Language Support (`Language.cs`)

Manages the multi-language support system using XML resources:

```csharp
public class Language
{
    private Dictionary<string, string> Translation_Dictionary = new();

    public List<string> GetAvailable_Languages()
    {
        var Current_Assembly = Assembly.GetExecutingAssembly();
        Available_Languages = Current_Assembly.GetManifestResourceNames().Where(Resource => Resource.Contains("translations") && Resource.EndsWith(".xml"))
            .Select(Resource => Path.GetFileNameWithoutExtension(Resource.Split('.').ElementAt(Resource.Split('.').Length - 2))).ToList();

        return Available_Languages;
    }

    public void Load_Translations(string Language_Name)
    {
        // Loads and parses the translation XML file
        using var Resource_Stream = Current_Assembly.GetManifestResourceStream(Resource_Name);
        var XML_Document = XDocument.Load(Resource_Stream);

        Translation_Dictionary = XML_Document.Descendants("string").ToDictionary(Element => Element.Attribute("key")?.Value ?? string.Empty, Element => Element.Value);
    }
}
```

#### Language Mapping Service (`LanguageMapping.cs`)

Manages the mapping between language names and their corresponding flag image codes:

```csharp
public class Language_Mapping : Language_Mapping_II
{
    private readonly Dictionary<string, string> LanguageTo_ImageCode;

    public Language_Mapping()
    {
        LanguageTo_ImageCode = new Dictionary<string, string>
        {
            { "English", "en" },
            { "Português", "pt" },
            { "Español", "es" }
            // Additional language mappings...
        };
    }

    public string GetImage_Code(string Language_Name) =>
        LanguageTo_ImageCode.TryGetValue(Path.GetFileNameWithoutExtension(Language_Name), out var Code) ? Code : Language_Name.ToLower();
}
```

#### Social Networks Service (`SocialNetworks.cs`)

Manages the opening of social network links in the default browser:

```csharp
public class Social_Networks
{
    public void OpenSocial_Network(string Network_Name)
    {
        string Network_Url = Network_Name switch
        {
            "Discord SPC" => "https://discord.gg/3fApZh66Tf",
            "YouTube" => "https://youtube.com/@spc-samp",
            // Additional network mappings...
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
```

#### Custom Interface Components

##### Progress Bar (`CustomProgressBar.cs`)

A highly customized progress bar with animations and modern styling:

```csharp
public class Custom_ProgressBar : ProgressBar
{
    // Customization properties
    public Color GradientStart_Color { get; set; }
    public Color GradientEnd_Color { get; set; }
    public int Animation_Speed { get; set; }
    public int Corner_Radius { get; set; }
    public bool Show_Percentage { get; set; }

    protected override void OnPaint(PaintEventArgs e)
    {
        // Implements custom drawing with gradients and animations
        using (var Path = GetRounded_Rectangle(Progress_Rect, Corner_Radius_II))
        using (var Gradient = new LinearGradientBrush(Progress_Rect, GradientStart_Color_II, GradientEnd_Color_II, LinearGradientMode.Horizontal))
        {
            // Applies color blend for smooth transitions
            ColorBlend Blend = new ColorBlend();
            Blend.Positions = Positions;
            Blend.Colors = Colors;
            Gradient.InterpolationColors = Blend;

            // Applies rotation animation
            Matrix Matrix = new Matrix();
            Matrix.RotateAt(Animation_Step, new PointF(Progress_Rect.Left + Progress_Rect.Width / 2, Progress_Rect.Top + Progress_Rect.Height / 2));
            Gradient.MultiplyTransform(Matrix);

            e.Graphics.FillPath(Gradient, Path);
        }
    }
}
```

##### Theme Colors (`Colors.cs`)

Defines the application's color scheme:

```csharp
public static class Colors_Client
{
    public static readonly Color Background = Color.FromArgb(32, 34, 37);
    public static readonly Color Secondary = Color.FromArgb(47, 49, 54);
    public static readonly Color Accent = Color.FromArgb(0, 139, 139);
    public static readonly Color Text = Color.White;
    public static readonly Color Hover = Color.FromArgb(64, 68, 75);
}
```

### Security Features

#### Administrative Privileges

The installer requires administrative privileges to correctly install the SA:MP files in the GTA:SA directory. This is managed through the `adm.manifest` file:

```xml
<?xml version="1.0" encoding="utf-8"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
  <trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">
    <security>
      <requestedPrivileges xmlns="urn:schemas-microsoft-com:asm.v3">
        <requestedExecutionLevel level="requireAdministrator" uiAccess="false" />
      </requestedPrivileges>
    </security>
  </trustInfo>
</assembly>
```

Main features of administrative execution:
- Ensures proper file permissions for installation
- Allows modification of protected system directories
- Automatically manages UAC (User Account Control) prompts
- Required for registry modifications if necessary

To enable administrative execution, the manifest file is referenced in the project file:

```xml
<PropertyGroup>
    <ApplicationManifest>adm.manifest</ApplicationManifest>
</PropertyGroup>
```

#### Assembly Signing

The project supports strong name signing for enhanced security. This can be enabled in the project file:

```xml
<PropertyGroup>
    <SignAssembly>true</SignAssembly>
    <AssemblyOriginatorKeyFile>MyKey.snk</AssemblyOriginatorKeyFile>
</PropertyGroup>
```

To generate a strong name key:

```bash
sn -k MyKey.snk
```

Benefits of assembly signing:
- Ensures assembly integrity
- Prevents tampering with the assembly
- Provides a unique identity for the assembly
- Allows deployment to the GAC
- Supports ClickOnce deployment

> [!NOTE]
> Keep your strong name key file (*.snk) secure and never commit it to source control.

### Internationalization

#### Translation System

Translations are stored in XML files with the following structure:

```xml
<translations>
  <string key="continue">Continue</string>
  <string key="cancel">Cancel</string>
  <string key="finish">Finish</string>
  <string key="close">Close</string>
  <!-- Additional translations -->
</translations>
```

The `Language` class loads these translations dynamically:

```csharp
public string Translate(string Key) => 
    Translation_Dictionary.TryGetValue(Key, out var Value) ? Value : Key;
```

#### Flag Icons

Language flags are stored as embedded resources and loaded dynamically:

```csharp
private Bitmap GetFlag_Image(string Language, int Icon_Size)
{
    var Image_Code = LanguageMapping_Module.GetImage_Code(Language);
    var Flag_Resource_Name = Get_Assembly.GetManifestResourceNames().FirstOrDefault(r => r.Contains("icons.languages") && r.EndsWith($"{Image_Code}.png"));
    
    if (Flag_Resource_Name != null)
    {
        using var Stream = Get_Assembly.GetManifestResourceStream(Flag_Resource_Name);
        return new Bitmap(Image.FromStream(Stream), new Size(Icon_Size, Icon_Size));
    }
    return null;
}
```

## Project Configuration (.csproj)

The `.csproj` file is a crucial component of the project, defining the application's settings and properties. Below is the detailed structure of the main configurations used:

### Basic Settings
```xml
<PropertyGroup>
    <OutputType>WinExe</OutputType>
    <TargetFramework>net9.0-windows</TargetFramework>
    <UseWindowsForms>true</UseWindowsForms>
    <ApplicationManifest>adm.manifest</ApplicationManifest>
    <ApplicationIcon>icons\social\ico-spc.ico</ApplicationIcon>
</PropertyGroup>
```

- `OutputType`: Defines the output type as a Windows executable
- `TargetFramework`: Specifies the .NET Framework version used (9.0)
- `UseWindowsForms`: Enables the use of Windows Forms for the graphical interface
- `ApplicationManifest`: Defines the application manifest for administrative permissions
- `ApplicationIcon`: Defines the application's main icon

### Version and Company Information
```xml
<PropertyGroup>
    <AssemblyVersion>1.0.0.0</AssemblyVersion>
    <FileVersion>1.0.0.0</FileVersion>
    <Company>SA-MP Programming Community</Company>
    <Product>samp-client-v</Product>
    <Copyright>Copyright © SPC</Copyright>
    <Description>Installer for the mod (San Andreas Multiplayer) version 0.3.7 V.</Description>
</PropertyGroup>
```

- `AssemblyVersion`: Version of the project's assembly
- `FileVersion`: Version of the executable file
- `Company`: Company/organization name
- `Product`: Product name
- `Copyright`: Copyright information
- `Description`: Project description

### Runtime Settings
```xml
<PropertyGroup>
    <RollForward>LatestMajor</RollForward>
    <RuntimeFrameworkVersion>9.0.0</RuntimeFrameworkVersion>
</PropertyGroup>
```

- `RollForward`: Configures runtime update behavior
- `RuntimeFrameworkVersion`: Specifies the exact version of the .NET runtime

### Embedded Resources
```xml
<ItemGroup>
    <EmbeddedResource Include="archives\**\*" />
    <EmbeddedResource Include="icons\**\*" />
    <EmbeddedResource Include="translations\**\*" />
</ItemGroup>
```

This section defines the resources that will be embedded in the final executable:
- `archives`: Files necessary for the installer
- `icons`: Icons and visual resources
- `translations`: Translation files for different languages

### Important Notes

1. The project is configured as a Windows Forms executable, suitable for creating a graphical user interface.
2. The application targets .NET 9.0, ensuring compatibility with the latest framework features.
3. Resources like icons, files, and translations are embedded directly into the executable, simplifying distribution.
4. Version settings and company information are important for software identification.

## Screenshots

![Screenshot 1 Client - SPC](/screenshots/screenshot_1.png)
![Screenshot 2 Client - SPC](/screenshots/screenshot_2.png)
![Screenshot 3 Client - SPC](/screenshots/screenshot_3.png)
![Screenshot 4 Client - SPC](/screenshots/screenshot_4.png)
![Screenshot 5 Client - SPC](/screenshots/screenshot_5.png)
![Screenshot 6 Client - SPC](/screenshots/screenshot_6.png)
![Screenshot 7 Client - SPC](/screenshots/screenshot_7.png)
![Screenshot 8 Client - SPC](/screenshots/screenshot_8.png)
![Screenshot 9 Client - SPC](/screenshots/screenshot_9.png)
![Screenshot 10 Client - SPC](/screenshots/screenshot_10.png)

Errors:

![Error 1 Client - SPC](/screenshots/error_1.png)
![Error 2 Client - SPC](/screenshots/error_2.png)

## License

Copyright © SA-MP Programming Community

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

### What you can do ✅

1. **Commercial Use**: 
   - You can use the code for commercial purposes
   - You can sell products that use this code
   - You can incorporate it into business solutions

2. **Modification**: 
   - You can modify the source code
   - You can adapt it to your needs
   - You can create derivative works

3. **Distribution**: 
   - You can distribute the software
   - You can share your modifications
   - You can include it in other projects

4. **Private Use**: 
   - You can use and modify the code privately
   - There's no obligation to make it public
   - You can use it in internal projects

5. **Patent Grant**: 
   - This license explicitly provides patent rights
   - Protection against contributors' patent claims
   - Guaranteed use without patent concerns

### What you must do ⚠️

1. **Include License**: 
   - A copy of the license must be included with the code
   - Must be easily accessible
   - Must be in its original format

2. **State Changes**: 
   - Significant changes must be declared
   - Document important alterations
   - Maintain a record of modifications

3. **Copyright Notice**: 
   - Preserve all copyright notices
   - Maintain original attributions
   - Include notices in all copies

4. **Document Changes**: 
   - Document all changes made
   - Maintain a changelog
   - Explain important modifications

### What you cannot do ❌

1. **Use Trademarks**: 
   - This license does not grant trademark rights
   - Cannot use names and logos without permission
   - Requires separate authorization for trademarks

2. **Hold Authors Liable**: 
   - Authors are not liable for damages
   - No warranties of operation
   - Use at your own risk