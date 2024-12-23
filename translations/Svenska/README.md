# clients-samp

[![Licença](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![C#](https://img.shields.io/badge/C%23-11.0-blue.svg)](https://docs.microsoft.com/en-us/dotnet/csharp/)
[![.NET](https://img.shields.io/badge/.NET-9.0-purple.svg)](https://dotnet.microsoft.com/)
[![Windows Forms](https://img.shields.io/badge/Windows%20Forms-net9.0--windows-blue)](https://docs.microsoft.com/en-us/dotnet/desktop/winforms/)

Detta repository innehåller källkoden för flera installatörer för Client SA:MP (San Andreas Multiplayer) utvecklade av SPC (SA-MP Programming Community). Dessa installatörer skapades för att erbjuda säkra och pålitliga alternativ till de ursprungliga installatörerna för modden, som inte längre anses vara pålitliga.

## Språk

- Português: [README](https://github.com/spc-samp/clients-samp)
- Deutsch: [README](../Deutsch/README.md)
- English: [README](../English/README.md)
- Español: [README](../Espanol/README.md)
- Français: [README](../Francais/README.md)
- Italiano: [README](../Italiano/README.md)
- Polski: [README](../Polski/README.md)
- Русский: [README](../Русский/README.md)
- Turk: [README](../Turk/README.md)

## Index

- [clients-samp](#clients-samp)
  - [Språk](#språk)
  - [Index](#index)
  - [Översikt](#översikt)
  - [Tillgängliga Versioner](#tillgängliga-versioner)
  - [Projektstruktur](#projektstruktur)
  - [Funktioner](#funktioner)
  - [Installation](#installation)
  - [Kompilering](#kompilering)
    - [Förutsättningar](#förutsättningar)
    - [Hur man kompilera](#hur-man-kompilera)
  - [Kodstruktur och Komponenter](#kodstruktur-och-komponenter)
    - [Huvudkomponenter](#huvudkomponenter)
      - [Installer Klient (`InstallerClient.cs`)](#installer-klient-installerclientcs)
    - [Tjänster](#tjänster)
      - [Filextraktionstjänst (`FileExtraction.cs`)](#filextraktionstjänst-fileextractioncs)
      - [Språkstöd (`Language.cs`)](#språkstöd-languagecs)
      - [Språkavbildningstjänst (`LanguageMapping.cs`)](#språkavbildningstjänst-languagemappingcs)
      - [Sociala nätverkstjänst (`SocialNetworks.cs`)](#sociala-nätverkstjänst-socialnetworkscs)
      - [Anpassade Gränssnittskomponenter](#anpassade-gränssnittskomponenter)
        - [Anpassad ProgressBar (`CustomProgressBar.cs`)](#anpassad-progressbar-customprogressbarcs)
        - [Temafärger (`Colors.cs`)](#temafärger-colorscs)
    - [Säkerhetsfunktioner](#säkerhetsfunktioner)
      - [Administrativa Behörigheter](#administrativa-behörigheter)
      - [Assemblingssignering](#assemblingssignering)
    - [Internationalisering](#internationalisering)
      - [Översättningssystem](#översättningssystem)
      - [Flaggsymboler](#flaggsymboler)
  - [Projektkonfiguration (.csproj)](#projektkonfiguration-csproj)
    - [Grundläggande Inställningar](#grundläggande-inställningar)
    - [Versionsinformation och Företagsinformation](#versionsinformation-och-företagsinformation)
    - [Runtime-inställningar](#runtime-inställningar)
    - [Inbäddade Resurser](#inbäddade-resurser)
    - [Viktiga Observationer](#viktiga-observationer)
  - [Screenshots](#screenshots)

## Översikt

Projektet syftar till att tillhandahålla säkra och pålitliga installationsprogram för olika versioner av mod SA:MP. Varje installationsprogram utvecklas i C# med Windows Forms och erbjuder ett modernt och användarvänligt gränssnitt med stöd för flera språk och ett fönster med sociala nätverk.

## Tillgängliga Versioner

Förrådet inkluderar följande versioner av Client:

- `samp-client-dl-r1`: Installationsprogram för Client DL R1
- `samp-client-r1`: Installationsprogram för Client R1
- `samp-client-r1-voip`: Client R1 med SAMPVOICE-integration
- `samp-client-r2`: Installationsprogram för Client R2
- `samp-client-r3`: Installationsprogram för Client R3
- `samp-client-r3-voip`: Client R3 med SAMPVOICE-integration
- `samp-client-r4`: Installationsprogram för Client R4
- `samp-client-r5`: Installationsprogram för Client R5

## Projektstruktur

Varje version av Client följer en konsekvent projektstruktur:

```
clients-samp/
└── samp-client-v/
    ├── archives/
    │   └── samp-client-{v}.zip
    ├── icons/
    │   ├── languages/
    │   │   └── [ikoner för språkflaggor]
    │   └── social/
    │       └── [ikoner för sociala nätverk]
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
    │   └── [30 språk-XML-filer]
    ├── adm.manifest
    ├── compile.bat
    ├── Main.cs
    └── samp-client-{v}.csproj
```

## Funktioner

- Stöd för flera språk (30 språk)
- Modernt och intuitivt användargränssnitt
- Säker extrahering och installation av filer
- Validering av spelkatalogen
- Realtidsframsteg
- Fönster med sociala nätverk
- Valfri assembliesignatur för förbättrad säkerhet
- Anpassad progress bar med animationer
- Konsistent färgschema och stil

## Installation

1. Gå till projektets [releases](https://github.com/spc-samp/clients-samp/releases)
2. Ladda ner den senaste versionen av Client som redan är kompilerad
3. Kör och följ instruktionerna

## Kompilering

### Förutsättningar

- .NET SDK 9.0 eller högre
- Windows operativsystem
- Visual Studio 2022 eller högre (valfritt)
- Visual Studio Code (valfritt)

### Hur man kompilera

Det enklaste sättet att kompilera en version av Client är att använda batch-filen som medföljer:

1. Öppna ett terminalfönster i katalogen för den version av Client
2. Kör kommandot för att kompilera:
```bash
.\compile
```

Du kan även kompilera direkt med .NET CLI:
```bash
dotnet publish -c Release -r win-x64 --self-contained true -p:PublishSingleFile=true -p:EnableCompressionInSingleFile=true -o ./published
```

> [!NOTE]
> Detta kommando kommer att generera en enda optimerad körbar fil för Windows 64-bit, som innehåller alla nödvändiga beroenden. Den körbara filen kommer att skapas i mappen `published` i projektkatalogen.

## Kodstruktur och Komponenter

### Huvudkomponenter

#### Installer Klient (`InstallerClient.cs`)

Huvudformuläret som hanterar hela installationsprocessen. Implementerar ett steg-för-steg assistentgränssnitt:

```csharp
public partial class Installer_Client : Form
{
    // Huvudmoduler
    private File_Extraction Extraction_Module;
    private Language Language_Module;
    private Language_Mapping LanguageMapping_Module;
    private Social_Networks SocialNetworks_Module;

    // Gränssnittselement
    private Label Description_Label, Status_Label;
    private Custom_ProgressBar Progress_Bar;
    private ListBox ExtractedFiles_List;
}
```

Huvudfunktioner och ansvar:

1. **Språkval**
   ```csharp
   private void CreateLanguage_Buttons()
   {
       // Skapar en matris med språkknappar med flaggor
       Panel Button_Panel = new Panel
       {
           AutoScroll = true,
           Dock = DockStyle.None,
           Location = new Point(0, 140),
           Width = this.ClientSize.Width,
           Height = this.ClientSize.Height - 140
       };
       
       // Dynamisk skapelse av knappar med flaggor
       for (int i = 0; i < Available_Languages.Count; i++)
       {
           var Language = Available_Languages[i];
           var Language_Button = CreateLanguage_Button(Language, Icon_Size, Button_Width, Button_Height, i, MaxButtons_PerRow, Padding);
           Button_Panel.Controls.Add(Language_Button);
       }
   }
   ```

2. **Val av installationsmapp**
   ```csharp
   private void Selecting_Folder()
   {
       // Dialog för mappval med validering
       using var Dialog = new FolderBrowserDialog();
       if (Dialog.ShowDialog() == DialogResult.OK)
       {
           Selected_Path = Dialog.SelectedPath;
           // Validerar installationsmappen för GTA:SA
           if (Path.GetFileName(Selected_Path) != "Grand Theft Auto San Andreas")
           {
               Status_Label.Text = Translate("invalid_folder");
               Status_Label.ForeColor = Color.Red;
           }
       }
   }
   ```

3. **Filextraktionsprocess**
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

4. **Fönster med sociala nätverk**
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

       // Skapar knappar för varje socialt nätverk med ikoner
       for (int i = 0; i < Social_Networks.Length; i++)
       {
           var Social_Button = CreateSocial_NetworkButton(Social_Networks[i], Icon_Size, Button_Width, Button_Height, i, Padding);
           Controls.Add(Social_Button);
       }
   }
   ```

### Tjänster

#### Filextraktionstjänst (`FileExtraction.cs`)

Hanterar säker extraktion av SA:MP-klientfiler från inbäddade resurser:

```csharp
public class File_Extraction
{
    public async Task<List<string>> ExtractClient_Files(string Target_Path, IProgress<(int progress, string fileName)> progress)
    {
        // Laddar den inbäddade ZIP-resursen
        var Current_Assembly = Assembly.GetExecutingAssembly();
        var Zip_Resource = Current_Assembly.GetManifestResourceNames().FirstOrDefault(Res => Res.Contains("archives") && Res.EndsWith("samp-client-v.zip"));

        using var Zip_Archive = new ZipArchive(Temp_Buffer, ZipArchiveMode.Read);
        var Total_Files = Zip_Archive.Entries.Count;
        var Processed_Files = new List<string>();

        // Extraherar filer med rapportering av framsteg
        for (int File_Index = 0; File_Index < Total_Files; File_Index++)
        {
            var Current_Entry = Zip_Archive.Entries[File_Index];
            var File_Target_Path = Path.Combine(Target_Path, Current_Entry.FullName);

            // Rapporterar framsteg för uppdateringar i gränssnittet
            int Completion_Percent = (int)((File_Index + 1) * 100.0 / Total_Files);
            progress.Report((Completion_Percent, Current_Entry.FullName));
        }

        return Processed_Files;
    }
}
```

#### Språkstöd (`Language.cs`)

Hanterar systemet för flerspråkigt stöd med hjälp av XML-resurser:

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
        // Laddar och analyserar XML-översättningsfilen
        using var Resource_Stream = Current_Assembly.GetManifestResourceStream(Resource_Name);
        var XML_Document = XDocument.Load(Resource_Stream);

        Translation_Dictionary = XML_Document.Descendants("string").ToDictionary(Element => Element.Attribute("key")?.Value ?? string.Empty, Element => Element.Value);
    }
}
```

#### Språkavbildningstjänst (`LanguageMapping.cs`)

Hanterar mappning mellan språknamn och deras tillhörande bildkoder för flaggor:

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
            // Ytterligare språkmappningar...
        };
    }

    public string GetImage_Code(string Language_Name) =>
        LanguageTo_ImageCode.TryGetValue(Path.GetFileNameWithoutExtension(Language_Name), out var Code) ? Code : Language_Name.ToLower();
}
```

#### Sociala nätverkstjänst (`SocialNetworks.cs`)

Hanterar öppning av sociala nätverkslänkar i standardwebbläsaren:

```csharp
public class Social_Networks
{
    public void OpenSocial_Network(string Network_Name)
    {
        string Network_Url = Network_Name switch
        {
            "Discord SPC" => "https://discord.gg/3fApZh66Tf",
            "YouTube" => "https://youtube.com/@spc-samp",
            // Ytterligare nätverksmappningar...
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

#### Anpassade Gränssnittskomponenter

##### Anpassad ProgressBar (`CustomProgressBar.cs`)

En mycket anpassad progressbar med animationer och modern stil:

```csharp
public class Custom_ProgressBar : ProgressBar
{
    // Anpassningsbara egenskaper
    public Color GradientStart_Color { get; set; }
    public Color GradientEnd_Color { get; set; }
    public int Animation_Speed { get; set; }
    public int Corner_Radius { get; set; }
    public bool Show_Percentage { get; set; }

    protected override void OnPaint(PaintEventArgs e)
    {
        // Implementerar anpassad ritning med gradienter och animationer
        using (var Path = GetRounded_Rectangle(Progress_Rect, Corner_Radius_II))
        using (var Gradient = new LinearGradientBrush(Progress_Rect, GradientStart_Color_II, GradientEnd_Color_II, LinearGradientMode.Horizontal))
        {
            // Tillämpa färgövergångar för mjuka övergångar
            ColorBlend Blend = new ColorBlend();
            Blend.Positions = Positions;
            Blend.Colors = Colors;
            Gradient.InterpolationColors = Blend;

            // Tillämpa roterande animation
            Matrix Matrix = new Matrix();
            Matrix.RotateAt(Animation_Step, new PointF(Progress_Rect.Left + Progress_Rect.Width / 2, Progress_Rect.Top + Progress_Rect.Height / 2));
            Gradient.MultiplyTransform(Matrix);

            e.Graphics.FillPath(Gradient, Path);
        }
    }
}
```

##### Temafärger (`Colors.cs`)

Definierar applikationens färgschema:

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

### Säkerhetsfunktioner

#### Administrativa Behörigheter

Installationsprogrammet kräver administrativa behörigheter för att korrekt installera SA:MP-filerna i GTA:SA-katalogen. Detta hanteras genom filen `adm.manifest`:

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

Huvudsakliga funktioner för administrativ körning:
- Säkerställer lämpliga filbehörigheter för installation
- Möjliggör ändring av skyddade systemkataloger
- Hanterar automatiskt UAC-promptar (Kontokontroll)
- Nödvändigt för registreringsändringar om det behövs

För att aktivera administrativ körning, refereras manifestfilen i projektfilen:

```xml
<PropertyGroup>
    <ApplicationManifest>adm.manifest</ApplicationManifest>
</PropertyGroup>
```

#### Assemblingssignering

Projektet stöder signering med stark namn för förbättrad säkerhet. Detta kan aktiveras i projektfilen:

```xml
<PropertyGroup>
    <SignAssembly>true</SignAssembly>
    <AssemblyOriginatorKeyFile>MyKey.snk</AssemblyOriginatorKeyFile>
</PropertyGroup>
```

För att generera ett starkt namn:

```bash
sn -k MyKey.snk
```

Fördelar med assembliesignering:
- Säkerställer assemblyns integritet
- Förhindrar manipulation av assembly
- Ger ett unikt identitetsbevis för assemblyn
- Möjliggör distribution i GAC
- Stöder ClickOnce-distribution

> [!NOTE]
> Håll din starka nyckelfil (*.snk) säker och lämna aldrig den för källkodskontroll.

### Internationalisering

#### Översättningssystem

Översättningar lagras i XML-filer med följande struktur:

```xml
<translations>
  <string key="continue">Fortsätt</string>
  <string key="cancel">Avbryt</string>
  <string key="finish">Slutför</string>
  <string key="close">Stäng</string>
  <!-- Ytterligare översättningar -->
</strings>
```

Klassen `Language` laddar dessa översättningar dynamiskt:

```csharp
public string Translate(string Key) => 
    Translation_Dictionary.TryGetValue(Key, out var Value) ? Value : Key;
```

#### Flaggsymboler

Flaggorna för språken lagras som inbäddade resurser och laddas dynamiskt:

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

## Projektkonfiguration (.csproj)

Filen `.csproj` är en viktig komponent i projektet som definierar de grundläggande inställningarna och egenskaperna för applikationen. Nedan finns en detaljerad struktur för de viktigaste konfigurationerna:

### Grundläggande Inställningar
```xml
<PropertyGroup>
    <OutputType>WinExe</OutputType>
    <TargetFramework>net9.0-windows</TargetFramework>
    <UseWindowsForms>true</UseWindowsForms>
    <ApplicationManifest>adm.manifest</ApplicationManifest>
    <ApplicationIcon>icons\social\ico-spc.ico</ApplicationIcon>
</PropertyGroup>
```

- `OutputType`: Definierar utdata som en Windows-exekverbar fil
- `TargetFramework`: Specificerar vilken version av .NET Framework som används (9.0)
- `UseWindowsForms`: Aktiverar användning av Windows Forms för det grafiska användargränssnittet
- `ApplicationManifest`: Definierar applikationens manifest för administrativa behörigheter
- `ApplicationIcon`: Definierar applikationens huvudikon

### Versionsinformation och Företagsinformation
```xml
<PropertyGroup>
    <AssemblyVersion>1.0.0.0</AssemblyVersion>
    <FileVersion>1.0.0.0</FileVersion>
    <Company>SA-MP Programming Community</Company>
    <Product>samp-client-v</Product>
    <Copyright>Copyright © SPC</Copyright>
    <Description>Installationsprogram för mod (San Andreas Multiplayer) version 0.3.7 V.</Description>
</PropertyGroup>
```

- `AssemblyVersion`: Version av projektets assembly
- `FileVersion`: Version av den exekverbara filen
- `Company`: Företags-/organisationsnamn
- `Product`: Produktens namn
- `Copyright`: Upphovsrättsinformation
- `Description`: Projektbeskrivning

### Runtime-inställningar
```xml
<PropertyGroup>
    <RollForward>LatestMajor</RollForward>
    <RuntimeFrameworkVersion>9.0.0</RuntimeFrameworkVersion>
</PropertyGroup>
```

- `RollForward`: Konfigurerar uppdateringsbeteendet för runtime
- `RuntimeFrameworkVersion`: Specificerar exakt version av .NET runtime

### Inbäddade Resurser
```xml
<ItemGroup>
    <EmbeddedResource Include="archives\**\*" />
    <EmbeddedResource Include="icons\**\*" />
    <EmbeddedResource Include="translations\**\*" />
</ItemGroup>
```

Denna sektion definierar de resurser som kommer att inbäddas i den slutliga exekverbara filen:
- `archives`: Filer som behövs för installationsprogrammet
- `icons`: Ikoner och visuella resurser
- `translations`: Översättningsfiler för olika språk

### Viktiga Observationer

1. Projektet är konfigurerat som en Windows Forms-applikation, vilket är lämpligt för att skapa ett grafiskt användargränssnitt.
2. Applikationen är riktad för .NET 9.0, vilket säkerställer kompatibilitet med de senaste funktionerna i ramverket.
3. Resurser som ikoner, filer och översättningar är inbäddade direkt i den exekverbara filen, vilket underlättar distributionen.
4. Versionsinställningar och företagsinformation är viktiga för identifiering av programvaran.

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

Fel:

![Error 1 Client - SPC](/screenshots/error_1.png)
![Error 2 Client - SPC](/screenshots/error_2.png)