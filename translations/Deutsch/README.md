# clients-samp

[![Licença](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![C#](https://img.shields.io/badge/C%23-11.0-blue.svg)](https://docs.microsoft.com/en-us/dotnet/csharp/)
[![.NET](https://img.shields.io/badge/.NET-9.0-purple.svg)](https://dotnet.microsoft.com/)
[![Windows Forms](https://img.shields.io/badge/Windows%20Forms-net9.0--windows-blue)](https://docs.microsoft.com/en-us/dotnet/desktop/winforms/)

Dieses Repository enthält den Quellcode verschiedener Installer für den SA:MP-Client (San Andreas Multiplayer), die von der SPC (SA-MP Programming Community) entwickelt wurden. Diese Installer wurden erstellt, um sichere und zuverlässige Alternativen zu den ursprünglichen Mod-Installern bereitzustellen, die nicht mehr als vertrauenswürdig gelten.

## Sprachen

- Português: [README](../../)
- English: [README](../English/README.md)
- Español: [README](../Espanol/README.md)
- Français: [README](../Francais/README.md)
- Italiano: [README](../Italiano/README.md)
- Polski: [README](../Polski/README.md)
- Русский: [README](../Русский/README.md)
- Svenska: [README](../Svenska/README.md)
- Türkçe: [README](../Turkce/README.md)

## Inhaltsverzeichnis

- [clients-samp](#clients-samp)
  - [Sprachen](#sprachen)
  - [Inhaltsverzeichnis](#inhaltsverzeichnis)
    - [Übersicht](#übersicht)
    - [Verfügbare Versionen](#verfügbare-versionen)
    - [Projektstruktur](#projektstruktur)
  - [Funktionen](#funktionen)
  - [Installation](#installation)
  - [Kompilierung](#kompilierung)
    - [Voraussetzungen](#voraussetzungen)
    - [Kompilierungsanleitung](#kompilierungsanleitung)
    - [Struktur des Codes und Komponenten](#struktur-des-codes-und-komponenten)
      - [Hauptkomponenten](#hauptkomponenten)
        - [Installations-Client (`InstallerClient.cs`)](#installations-client-installerclientcs)
    - [Services](#services)
      - [Datei-Extraktionsdienst (`FileExtraction.cs`)](#datei-extraktionsdienst-fileextractioncs)
      - [Sprachunterstützung (`Language.cs`)](#sprachunterstützung-languagecs)
      - [Sprachzuordnungsdienst (`LanguageMapping.cs`)](#sprachzuordnungsdienst-languagemappingcs)
      - [Soziale Netzwerke Dienst (`SocialNetworks.cs`)](#soziale-netzwerke-dienst-socialnetworkscs)
      - [Benutzerdefinierte Benutzeroberflächenkomponenten](#benutzerdefinierte-benutzeroberflächenkomponenten)
        - [Fortschrittsbalken (`CustomProgressBar.cs`)](#fortschrittsbalken-customprogressbarcs)
        - [Farbthema (`Colors.cs`)](#farbthema-colorscs)
    - [Sicherheitsfunktionen](#sicherheitsfunktionen)
      - [Administratorrechte](#administratorrechte)
      - [Assembly-Signatur](#assembly-signatur)
    - [Internationalisierung](#internationalisierung)
      - [Übersetzungssystem](#übersetzungssystem)
      - [Flaggen-Icons](#flaggen-icons)
  - [Projektkonfiguration (.csproj)](#projektkonfiguration-csproj)
    - [Grundlegende Einstellungen](#grundlegende-einstellungen)
    - [Versions- und Firmeninformationen](#versions--und-firmeninformationen)
    - [Laufzeiteinstellungen](#laufzeiteinstellungen)
    - [Eingebettete Ressourcen](#eingebettete-ressourcen)
    - [Wichtige Hinweise](#wichtige-hinweise)
  - [Screenshots](#screenshots)
  - [Lizenz](#lizenz)
    - [Nutzungsbedingungen](#nutzungsbedingungen)
      - [1. Gewährte Berechtigungen](#1-gewährte-berechtigungen)
      - [2. Verpflichtende Bedingungen](#2-verpflichtende-bedingungen)
      - [3. Einschränkungen und Beschränkungen](#3-einschränkungen-und-beschränkungen)
      - [4. Geistiges Eigentum](#4-geistiges-eigentum)
      - [5. Gewährleistungsausschluss und Haftungsbeschränkung](#5-gewährleistungsausschluss-und-haftungsbeschränkung)

### Übersicht

Das Projekt hat das Ziel, sichere und zuverlässige Installer für verschiedene Versionen des SA:MP-Mods bereitzustellen. Jeder Installer wird in C# mit Windows Forms entwickelt und bietet eine moderne und benutzerfreundliche Oberfläche mit Unterstützung für mehrere Sprachen sowie ein Fenster mit Links zu sozialen Netzwerken.

### Verfügbare Versionen

Das Repository enthält die folgenden Client-Versionen:

- `samp-client-dl-r1`: Installer für den Client DL R1
- `samp-client-r1`: Installer für den Client R1
- `samp-client-r1-voip`: Client R1 mit SAMPVOICE-Integration
- `samp-client-r2`: Installer für den Client R2
- `samp-client-r3`: Installer für den Client R3
- `samp-client-r3-voip`: Client R3 mit SAMPVOICE-Integration
- `samp-client-r4`: Installer für den Client R4
- `samp-client-r5`: Installer für den Client R5

### Projektstruktur

Jede Client-Version folgt einer konsistenten Projektstruktur:

```
clients-samp/
└── samp-client-v/
    ├── archives/
    │   └── samp-client-{v}.zip
    ├── icons/
    │   ├── languages/
    │   │   └── [Symbole der Flaggen der Sprachen]
    │   └── social/
    │       └── [Symbole der sozialen Netzwerke]
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
    │   └── [30 XML-Dateien der Sprachen]
    ├── adm.manifest
    ├── compile.bat
    ├── Main.cs
    └── samp-client-{v}.csproj
```

## Funktionen

- Unterstützung für mehrere Sprachen (30 Sprachen)
- Moderne und intuitive Benutzeroberfläche
- Sicheres Extrahieren und Installieren von Dateien
- Validierung des Spielverzeichnisses
- Echtzeit-Überwachung des Fortschritts
- Fenster mit Links zu sozialen Netzwerken
- Optionale Assembly-Signierung für erhöhte Sicherheit
- Benutzerdefinierte Fortschrittsleiste mit Animationen
- Konsistente Farb- und Stilgestaltung

## Installation

1. Besuchen Sie die [releases](https://github.com/spc-samp/clients-samp/releases) des Projekts
2. Laden Sie die neueste, bereits kompilierte Version des Clients herunter
3. Führen Sie das Programm aus und folgen Sie den Anweisungen

## Kompilierung

### Voraussetzungen

- .NET SDK 9.0 oder höher
- Betriebssystem Windows
- Visual Studio 2022 oder höher (optional)
- Visual Studio Code (optional)

### Kompilierungsanleitung

Die einfachste Methode, eine Version des Clients zu kompilieren, ist die Verwendung der bereitgestellten Batch-Datei:

1. Öffnen Sie ein Terminal im Verzeichnis der Client-Version
2. Führen Sie den Kompilierungsbefehl aus:
```bash
.\compile
```

Sie können auch direkt mit dem .NET CLI kompilieren:
```bash
dotnet publish -c Release -r win-x64 --self-contained true -p:PublishSingleFile=true -p:EnableCompressionInSingleFile=true -o ./published
```

> [!NOTE]
> Dieser Befehl erstellt eine einzige ausführbare Datei, die für Windows 64-Bit optimiert ist und alle notwendigen Abhängigkeiten enthält. Die ausführbare Datei wird im Ordner `published` im Projektverzeichnis generiert.

### Struktur des Codes und Komponenten

#### Hauptkomponenten

##### Installations-Client (`InstallerClient.cs`)

Das Hauptformular, das den gesamten Installationsprozess verwaltet. Es implementiert eine Schritt-für-Schritt-Assistentenoberfläche:

```csharp
public partial class Installer_Client : Form
{
    // Hauptmodule
    private File_Extraction Extraction_Module;
    private Language Language_Module;
    private Language_Mapping LanguageMapping_Module;
    private Social_Networks SocialNetworks_Module;

    // Interface-Elemente
    private Label Description_Label, Status_Label;
    private Custom_ProgressBar Progress_Bar;
    private ListBox ExtractedFiles_List;
}
```

Wesentliche Funktionen und Verantwortlichkeiten:

1. **Sprachauswahl**
   ```csharp
   private void CreateLanguage_Buttons()
   {
       // Erstellen eines Rasters von Sprachbuttons mit Flaggen
       Panel Button_Panel = new Panel
       {
           AutoScroll = true,
           Dock = DockStyle.None,
           Location = new Point(0, 140),
           Width = this.ClientSize.Width,
           Height = this.ClientSize.Height - 140
       };
       
       // Dynamisches Erstellen von Buttons mit Flaggen
       for (int i = 0; i < Available_Languages.Count; i++)
       {
           var Language = Available_Languages[i];
           var Language_Button = CreateLanguage_Button(Language, Icon_Size, Button_Width, Button_Height, i, MaxButtons_PerRow, Padding);
           Button_Panel.Controls.Add(Language_Button);
       }
   }
   ```

2. **Auswahl des Installationsverzeichnisses**
   ```csharp
   private void Selecting_Folder()
   {
       // Dialog zur Ordnerauswahl mit Validierung
       using var Dialog = new FolderBrowserDialog();
       if (Dialog.ShowDialog() == DialogResult.OK)
       {
           Selected_Path = Dialog.SelectedPath;
           // Validierung des GTA:SA-Installationsverzeichnisses
           if (Path.GetFileName(Selected_Path) != "Grand Theft Auto San Andreas")
           {
               Status_Label.Text = Translate("invalid_folder");
               Status_Label.ForeColor = Color.Red;
           }
       }
   }
   ```

3. **Dateiextraktionsprozess**
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

4. **Fenster mit sozialen Netzwerken**
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

       // Buttons für jedes soziale Netzwerk mit Icons erstellen
       for (int i = 0; i < Social_Networks.Length; i++)
       {
           var Social_Button = CreateSocial_NetworkButton(Social_Networks[i], Icon_Size, Button_Width, Button_Height, i, Padding);
           Controls.Add(Social_Button);
       }
   }
   ```

### Services

#### Datei-Extraktionsdienst (`FileExtraction.cs`)

Verwaltet die sichere Extraktion der SA:MP-Client-Dateien aus eingebetteten Ressourcen:

```csharp
public class File_Extraction
{
    public async Task<List<string>> ExtractClient_Files(string Target_Path, IProgress<(int progress, string fileName)> progress)
    {
        // Lädt die eingebettete ZIP-Ressource
        var Current_Assembly = Assembly.GetExecutingAssembly();
        var Zip_Resource = Current_Assembly.GetManifestResourceNames().FirstOrDefault(Res => Res.Contains("archives") && Res.EndsWith("samp-client-v.zip"));

        using var Zip_Archive = new ZipArchive(Temp_Buffer, ZipArchiveMode.Read);
        var Total_Files = Zip_Archive.Entries.Count;
        var Processed_Files = new List<string>();

        // Extrahiert Dateien und meldet Fortschritt
        for (int File_Index = 0; File_Index < Total_Files; File_Index++)
        {
            var Current_Entry = Zip_Archive.Entries[File_Index];
            var File_Target_Path = Path.Combine(Target_Path, Current_Entry.FullName);

            // Fortschrittsaktualisierung für die Benutzeroberfläche
            int Completion_Percent = (int)((File_Index + 1) * 100.0 / Total_Files);
            progress.Report((Completion_Percent, Current_Entry.FullName));
        }

        return Processed_Files;
    }
}
```

#### Sprachunterstützung (`Language.cs`)

Verwaltet ein Mehrsprachigkeitssystem unter Verwendung von XML-Ressourcen:

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
        // Lädt und analysiert die XML-Übersetzungsdatei
        using var Resource_Stream = Current_Assembly.GetManifestResourceStream(Resource_Name);
        var XML_Document = XDocument.Load(Resource_Stream);

        Translation_Dictionary = XML_Document.Descendants("string").ToDictionary(Element => Element.Attribute("key")?.Value ?? string.Empty, Element => Element.Value);
    }
}
```

#### Sprachzuordnungsdienst (`LanguageMapping.cs`)

Verwaltet die Zuordnung zwischen Sprachnamen und ihren entsprechenden Flaggenbildcodes:

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
            // Zusätzliche Sprachzuordnungen...
        };
    }

    public string GetImage_Code(string Language_Name) =>
        LanguageTo_ImageCode.TryGetValue(Path.GetFileNameWithoutExtension(Language_Name), out var Code) ? Code : Language_Name.ToLower();
}
```

#### Soziale Netzwerke Dienst (`SocialNetworks.cs`)

Verwaltet das Öffnen von Links zu sozialen Netzwerken im Standardbrowser:

```csharp
public class Social_Networks
{
    public void OpenSocial_Network(string Network_Name)
    {
        string Network_Url = Network_Name switch
        {
            "Discord SPC" => "https://discord.gg/3fApZh66Tf",
            "YouTube" => "https://youtube.com/@spc-samp",
            // Zusätzliche Netzwerkzuordnungen...
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

#### Benutzerdefinierte Benutzeroberflächenkomponenten

##### Fortschrittsbalken (`CustomProgressBar.cs`)

Ein hochgradig anpassbarer Fortschrittsbalken mit Animationen und modernem Stil:

```csharp
public class Custom_ProgressBar : ProgressBar
{
    // Anpassungseigenschaften
    public Color GradientStart_Color { get; set; }
    public Color GradientEnd_Color { get; set; }
    public int Animation_Speed { get; set; }
    public int Corner_Radius { get; set; }
    public bool Show_Percentage { get; set; }

    protected override void OnPaint(PaintEventArgs e)
    {
        // Implementiert benutzerdefinierte Zeichnungen mit Farbverläufen und Animationen
        using (var Path = GetRounded_Rectangle(Progress_Rect, Corner_Radius_II))
        using (var Gradient = new LinearGradientBrush(Progress_Rect, GradientStart_Color_II, GradientEnd_Color_II, LinearGradientMode.Horizontal))
        {
            // Wendet Farbmischung für sanfte Übergänge an
            ColorBlend Blend = new ColorBlend();
            Blend.Positions = Positions;
            Blend.Colors = Colors;
            Gradient.InterpolationColors = Blend;

            // Wendet Rotationsanimation an
            Matrix Matrix = new Matrix();
            Matrix.RotateAt(Animation_Step, new PointF(Progress_Rect.Left + Progress_Rect.Width / 2, Progress_Rect.Top + Progress_Rect.Height / 2));
            Gradient.MultiplyTransform(Matrix);

            e.Graphics.FillPath(Gradient, Path);
        }
    }
}
```

##### Farbthema (`Colors.cs`)

Definiert das Farbschema der Anwendung:

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

### Sicherheitsfunktionen

#### Administratorrechte

Das Installationsprogramm erfordert Administratorrechte, um die SA:MP-Dateien im GTA:SA-Verzeichnis korrekt zu installieren. Dies wird über die Datei `adm.manifest` verwaltet:

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

Hauptfunktionen der Administratorausführung:
- Gewährleistet angemessene Dateiberechtigungen für die Installation
- Ermöglicht die Änderung geschützter Systemverzeichnisse
- Verwalten automatisch UAC-Eingabeaufforderungen (Benutzerkontensteuerung)
- Erforderlich für Änderungen in der Registrierung, falls notwendig

Um die Administratorausführung zu aktivieren, wird die Manifestdatei in der Projektdatei referenziert:

```xml
<PropertyGroup>
    <ApplicationManifest>adm.manifest</ApplicationManifest>
</PropertyGroup>
```

#### Assembly-Signatur

Das Projekt unterstützt die starke Namenssignatur für verbesserte Sicherheit. Dies kann in der Projektdatei aktiviert werden:

```xml
<PropertyGroup>
    <SignAssembly>true</SignAssembly>
    <AssemblyOriginatorKeyFile>MyKey.snk</AssemblyOriginatorKeyFile>
</PropertyGroup>
```

Um einen starken Namensschlüssel zu generieren:

```bash
sn -k MyKey.snk
```

Vorteile der Assembly-Signatur:
- Gewährleistet die Integrität der Assembly
- Verhindert Manipulation der Assembly
- Bietet der Assembly eine eindeutige Identität
- Ermöglicht die Bereitstellung im GAC
- Unterstützt ClickOnce-Bereitstellung

> [!NOTE]
> Halten Sie Ihre Datei für den starken Namensschlüssel (*.snk) sicher und geben Sie sie niemals in die Quellcodeverwaltung ein.

### Internationalisierung

#### Übersetzungssystem

Die Übersetzungen werden in XML-Dateien mit der folgenden Struktur gespeichert:

```xml
<translations>
  <string key="continue">Fortfahren</string>
  <string key="cancel">Abbrechen</string>
  <string key="finish">Abschließen</string>
  <string key="close">Schließen</string>
  <!-- Zusätzliche Übersetzungen -->
</translations>
```

Die Klasse `Language` lädt diese Übersetzungen dynamisch:

```csharp
public string Translate(string Key) => 
    Translation_Dictionary.TryGetValue(Key, out var Value) ? Value : Key;
```

#### Flaggen-Icons

Die Flaggen der Sprachen werden als eingebettete Ressourcen gespeichert und dynamisch geladen:

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

Die `.csproj`-Datei ist ein essenzieller Bestandteil des Projekts und definiert die grundlegenden Einstellungen und Eigenschaften der Anwendung. Im Folgenden ist die detaillierte Struktur der wichtigsten Einstellungen dargestellt:

### Grundlegende Einstellungen
```xml
<PropertyGroup>
    <OutputType>WinExe</OutputType>
    <TargetFramework>net9.0-windows</TargetFramework>
    <UseWindowsForms>true</UseWindowsForms>
    <ApplicationManifest>adm.manifest</ApplicationManifest>
    <ApplicationIcon>icons\social\ico-spc.ico</ApplicationIcon>
</PropertyGroup>
```

- `OutputType`: Legt den Ausgabetyp als Windows-Executable fest
- `TargetFramework`: Gibt die verwendete Version des .NET Frameworks an (9.0)
- `UseWindowsForms`: Aktiviert die Verwendung von Windows Forms für die grafische Benutzeroberfläche
- `ApplicationManifest`: Definiert das Anwendungsmanifest für administrative Berechtigungen
- `ApplicationIcon`: Legt das Hauptsymbol der Anwendung fest

### Versions- und Firmeninformationen
```xml
<PropertyGroup>
    <AssemblyVersion>1.0.0.0</AssemblyVersion>
    <FileVersion>1.0.0.0</FileVersion>
    <Company>SA-MP Programming Community</Company>
    <Product>samp-client-v</Product>
    <Copyright>Copyright © SPC</Copyright>
    <Description>Installer für das Mod (San Andreas Multiplayer) Version 0.3.7 V.</Description>
</PropertyGroup>
```

- `AssemblyVersion`: Version des Projekt-Assemblies
- `FileVersion`: Version der ausführbaren Datei
- `Company`: Name des Unternehmens/der Organisation
- `Product`: Produktname
- `Copyright`: Angaben zu den Urheberrechten
- `Description`: Beschreibung des Projekts

### Laufzeiteinstellungen
```xml
<PropertyGroup>
    <RollForward>LatestMajor</RollForward>
    <RuntimeFrameworkVersion>9.0.0</RuntimeFrameworkVersion>
</PropertyGroup>
```

- `RollForward`: Konfiguriert das Verhalten bei der Aktualisierung der Laufzeit
- `RuntimeFrameworkVersion`: Gibt die genaue Version der .NET-Laufzeit an

### Eingebettete Ressourcen
```xml
<ItemGroup>
    <EmbeddedResource Include="archives\**\*" />
    <EmbeddedResource Include="icons\**\*" />
    <EmbeddedResource Include="translations\**\*" />
</ItemGroup>
```

Dieser Abschnitt definiert die Ressourcen, die in die finale ausführbare Datei eingebettet werden:
- `archives`: Erforderliche Dateien für den Installer
- `icons`: Symbole und visuelle Ressourcen
- `translations`: Übersetzungsdateien für verschiedene Sprachen

### Wichtige Hinweise

1. Das Projekt ist als Windows-Forms-Executable konfiguriert, was sich für die Erstellung einer grafischen Benutzeroberfläche eignet.
2. Die Anwendung ist auf .NET 9.0 ausgerichtet, wodurch die neuesten Funktionen des Frameworks genutzt werden können.
3. Ressourcen wie Symbole, Dateien und Übersetzungen werden direkt in die ausführbare Datei eingebettet, was die Verteilung erleichtert.
4. Die Versions- und Firmeninformationen sind wichtig für die Identifikation der Software.

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

Fehler:

![Error 1 Client - SPC](/screenshots/error_1.png)
![Error 2 Client - SPC](/screenshots/error_2.png)

## Lizenz

Copyright © **SA-MP Programming Community**

Diese Software ist unter den Bedingungen der Apache-Lizenz Version 2.0 (die "Lizenz") lizenziert; Sie dürfen diese Software nur in Übereinstimmung mit der Lizenz verwenden. Eine Kopie der Lizenz erhalten Sie unter: [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)

### Nutzungsbedingungen

#### 1. Gewährte Berechtigungen

Diese Lizenz gewährt jeder Person, die eine Kopie dieser Software und der zugehörigen Dokumentationsdateien erhält, kostenlos folgende Rechte:

* Die Software in jedem Medium oder Format für jeden Zweck, kommerziell oder nicht-kommerziell, zu nutzen, zu kopieren, zu modifizieren und zu verteilen
* Die Software zu verschmelzen, zu veröffentlichen, zu verteilen, unterzulizenzieren und/oder Kopien zu verkaufen
* Personen, denen die Software zur Verfügung gestellt wird, dies ebenfalls zu ermöglichen

#### 2. Verpflichtende Bedingungen

Alle Verteilungen der Software oder abgeleiteten Werke müssen:

* Eine vollständige Kopie dieser Lizenz enthalten
* Alle Änderungen am ursprünglichen Quellcode deutlich kennzeichnen
* Alle Urheberrechts-, Patent-, Marken- und Zuordnungshinweise bewahren
* Angemessene Dokumentation der implementierten Änderungen bereitstellen
* Den Lizenz- und Gewährleistungshinweis in allen Kopien beibehalten

#### 3. Einschränkungen und Beschränkungen

* Diese Lizenz gewährt keine Erlaubnis zur Nutzung von Markenzeichen, Logos oder Handelsnamen der **SA-MP Programming Community**
* Beiträge zum Quellcode müssen unter denselben Bedingungen dieser Lizenz lizenziert werden
* Die Verwendung von Namen der Mitwirkenden zur Befürwortung oder Bewerbung von aus dieser Software abgeleiteten Produkten erfordert eine spezifische vorherige Genehmigung

#### 4. Geistiges Eigentum

Die Software und alle zugehörige Dokumentation sind durch Urheberrechtsgesetze und internationale Verträge geschützt. Die **SA-MP Programming Community** behält sich alle Rechte, Titel und Interessen vor, die nicht ausdrücklich durch diese Lizenz gewährt werden.

#### 5. Gewährleistungsausschluss und Haftungsbeschränkung

DIE SOFTWARE WIRD "WIE BESEHEN" OHNE JEGLICHE AUSDRÜCKLICHE ODER IMPLIZIERTE GEWÄHRLEISTUNG BEREITGESTELLT, EINSCHLIESSLICH, ABER NICHT BESCHRÄNKT AUF DIE GEWÄHRLEISTUNG DER MARKTFÄHIGKEIT, DER EIGNUNG FÜR EINEN BESTIMMTEN ZWECK UND DER NICHTVERLETZUNG VON RECHTEN DRITTER.

IN KEINEM FALL HAFTEN DIE AUTOREN ODER URHEBERRECHTSINHABER FÜR ANSPRÜCHE, SCHÄDEN ODER ANDERE VERPFLICHTUNGEN, OB IN EINER VERTRAGS- ODER HAFTUNGSKLAGE, EINER UNERLAUBTEN HANDLUNG ODER ANDERWEITIG, DIE SICH AUS ODER IN VERBINDUNG MIT DER SOFTWARE ODER DER NUTZUNG ODER ANDEREN GESCHÄFTEN MIT DER SOFTWARE ERGEBEN.

---

Für detaillierte Informationen zur Apache License 2.0 besuchen Sie: http://www.apache.org/licenses/LICENSE-2.0