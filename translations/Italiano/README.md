# clients-samp

[![Licença](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![C#](https://img.shields.io/badge/C%23-11.0-blue.svg)](https://docs.microsoft.com/en-us/dotnet/csharp/)
[![.NET](https://img.shields.io/badge/.NET-9.0-purple.svg)](https://dotnet.microsoft.com/)
[![Windows Forms](https://img.shields.io/badge/Windows%20Forms-net9.0--windows-blue)](https://docs.microsoft.com/en-us/dotnet/desktop/winforms/)

Questo repository contiene il codice sorgente di diversi installer per il Client SA:MP (San Andreas Multiplayer) sviluppati dalla SPC (SA-MP Programming Community). Questi installer sono stati creati per fornire alternative sicure e affidabili agli installer originali del mod, che non sono più considerati affidabili.

## Lingue

- Português: [README](https://github.com/spc-samp/clients-samp)
- Deutsch: [README](../Deutsch/README.md)
- English: [README](../English/README.md)
- Español: [README](../Espanol/README.md)
- Français: [README](../Francais/README.md)
- Polski: [README](../Polski/README.md)
- Русский: [README](../Русский/README.md)
- Svenska: [README](../Svenska/README.md)
- Turk: [README](../Turk/README.md)

## Indice

- [clients-samp](#clients-samp)
  - [Lingue](#lingue)
  - [Indice](#indice)
  - [Panoramica](#panoramica)
  - [Versioni Disponibili](#versioni-disponibili)
  - [Struttura del Progetto](#struttura-del-progetto)
  - [Funzionalità](#funzionalità)
  - [Installazione](#installazione)
  - [Compilazione](#compilazione)
    - [Requisiti](#requisiti)
    - [Come compilare](#come-compilare)
  - [Struttura del Codice e Componenti](#struttura-del-codice-e-componenti)
    - [Componenti Principali](#componenti-principali)
      - [Client Installatore (`InstallerClient.cs`)](#client-installatore-installerclientcs)
    - [Servizi](#servizi)
      - [Servizio di Estrazione dei File (`FileExtraction.cs`)](#servizio-di-estrazione-dei-file-fileextractioncs)
      - [Supporto per le Lingue (`Language.cs`)](#supporto-per-le-lingue-languagecs)
      - [Servizio di Mappatura delle Lingue (`LanguageMapping.cs`)](#servizio-di-mappatura-delle-lingue-languagemappingcs)
      - [Servizio delle Reti Sociali (`SocialNetworks.cs`)](#servizio-delle-reti-sociali-socialnetworkscs)
      - [Componenti dell'Interfaccia Personalizzati](#componenti-dellinterfaccia-personalizzati)
        - [Barra di Progresso (`CustomProgressBar.cs`)](#barra-di-progresso-customprogressbarcs)
        - [Colori del Tema (`Colors.cs`)](#colori-del-tema-colorscs)
    - [Risorse di Sicurezza](#risorse-di-sicurezza)
      - [Privilegi Amministrativi](#privilegi-amministrativi)
      - [Firma dell'Assembly](#firma-dellassembly)
    - [Internazionalizzazione](#internazionalizzazione)
      - [Sistema di Traduzione](#sistema-di-traduzione)
      - [Icone delle Bandierine](#icone-delle-bandierine)
  - [Configurazione del Progetto (.csproj)](#configurazione-del-progetto-csproj)
    - [Configurazioni di Base](#configurazioni-di-base)
    - [Informazioni sulla Versione e sull'Azienda](#informazioni-sulla-versione-e-sullazienda)
    - [Configurazioni di Runtime](#configurazioni-di-runtime)
    - [Risorse Incorporate](#risorse-incorporate)
    - [Osservazioni Importanti](#osservazioni-importanti)
  - [Screenshots](#screenshots)

## Panoramica

Il progetto ha come obiettivo fornire installer sicuri e affidabili per diverse versioni del mod SA:MP. Ogni installer è sviluppato in C# utilizzando Windows Forms, offrendo un'interfaccia moderna e user-friendly con supporto per più lingue e una finestra con i social media.

## Versioni Disponibili

Il repository include le seguenti versioni del Client:

- `samp-client-dl-r1`: Installer del Client DL R1
- `samp-client-r1`: Installer del Client R1
- `samp-client-r1-voip`: Client R1 con integrazione SAMPVOICE
- `samp-client-r2`: Installer del Client R2
- `samp-client-r3`: Installer del Client R3
- `samp-client-r3-voip`: Client R3 con integrazione SAMPVOICE
- `samp-client-r4`: Installer del Client R4
- `samp-client-r5`: Installer del Client R5

## Struttura del Progetto

Ogni versione del Client segue una struttura di progetto consistente:

```
clients-samp/
└── samp-client-v/
    ├── archives/
    │   └── samp-client-{v}.zip
    ├── icons/
    │   ├── languages/
    │   │   └── [icone delle bandiere delle lingue]
    │   └── social/
    │       └── [icone dei social media]
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
    │   └── [30 file XML delle lingue]
    ├── adm.manifest
    ├── compile.bat
    ├── Main.cs
    └── samp-client-{v}.csproj
```

## Funzionalità

- Supporto per più lingue (30 lingue)
- Interfaccia utente moderna e intuitiva
- Estrazione e installazione sicura dei file
- Validazione della directory del gioco
- Monitoraggio del progresso in tempo reale
- Finestra con i social media
- Firma dell'assembly opzionale per una maggiore sicurezza
- Barra di progresso personalizzata con animazioni
- Schema di colori e stile coerente

## Installazione

1. Accedi alla pagina di [releases](https://github.com/spc-samp/clients-samp/releases) del progetto
2. Scarica l'ultima versione compilata del Client
3. Esegui e procedi con le istruzioni

## Compilazione

### Requisiti

- SDK .NET 9.0 o superiore
- Sistema operativo Windows
- Visual Studio 2022 o superiore (opzionale)
- Visual Studio Code (opzionale)

### Come compilare

Il modo più semplice per compilare qualsiasi versione del Client è usare il file batch fornito:

1. Apri un terminale nella cartella della versione del Client
2. Esegui il comando di compilazione:
```bash
.\compile
```

Puoi anche compilare direttamente usando il CLI di .NET:
```bash
dotnet publish -c Release -r win-x64 --self-contained true -p:PublishSingleFile=true -p:EnableCompressionInSingleFile=true -o ./published
```

> [!NOTE]
> Questo comando genererà un file eseguibile unico e ottimizzato per Windows a 64 bit, contenente tutte le dipendenze necessarie. Il file eseguibile verrà creato nella cartella `published` nella directory del progetto.

## Struttura del Codice e Componenti

### Componenti Principali

#### Client Installatore (`InstallerClient.cs`)

Il modulo principale che gestisce l'intero processo di installazione. Implementa un'interfaccia assistente passo dopo passo:

```csharp
public partial class Installer_Client : Form
{
    // Moduli principali
    private File_Extraction Extraction_Module;
    private Language Language_Module;
    private Language_Mapping LanguageMapping_Module;
    private Social_Networks SocialNetworks_Module;

    // Elementi dell'interfaccia
    private Label Description_Label, Status_Label;
    private Custom_ProgressBar Progress_Bar;
    private ListBox ExtractedFiles_List;
}
```

Caratteristiche principali e responsabilità:

1. **Selezione della Lingua**
   ```csharp
   private void CreateLanguage_Buttons()
   {
       // Crea una griglia di pulsanti per le lingue con bandiere
       Panel Button_Panel = new Panel
       {
           AutoScroll = true,
           Dock = DockStyle.None,
           Location = new Point(0, 140),
           Width = this.ClientSize.Width,
           Height = this.ClientSize.Height - 140
       };
       
       // Creazione dinamica dei pulsanti con bandiere
       for (int i = 0; i < Available_Languages.Count; i++)
       {
           var Language = Available_Languages[i];
           var Language_Button = CreateLanguage_Button(Language, Icon_Size, Button_Width, Button_Height, i, MaxButtons_PerRow, Padding);
           Button_Panel.Controls.Add(Language_Button);
       }
   }
   ```

2. **Selezione della Cartella di Installazione**
   ```csharp
   private void Selecting_Folder()
   {
       // Dialogo di selezione della cartella con validazione
       using var Dialog = new FolderBrowserDialog();
       if (Dialog.ShowDialog() == DialogResult.OK)
       {
           Selected_Path = Dialog.SelectedPath;
           // Valida la cartella di installazione di GTA:SA
           if (Path.GetFileName(Selected_Path) != "Grand Theft Auto San Andreas")
           {
               Status_Label.Text = Translate("invalid_folder");
               Status_Label.ForeColor = Color.Red;
           }
       }
   }
   ```

3. **Processo di Estrazione dei File**
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

4. **Finestra con le Reti Sociali**
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

       // Crea pulsanti per ogni rete sociale con icone
       for (int i = 0; i < Social_Networks.Length; i++)
       {
           var Social_Button = CreateSocial_NetworkButton(Social_Networks[i], Icon_Size, Button_Width, Button_Height, i, Padding);
           Controls.Add(Social_Button);
       }
   }
   ```

### Servizi

#### Servizio di Estrazione dei File (`FileExtraction.cs`)

Gestisce l'estrazione sicura dei file del Client SA:MP dalle risorse incorporate:

```csharp
public class File_Extraction
{
    public async Task<List<string>> ExtractClient_Files(string Target_Path, IProgress<(int progress, string fileName)> progress)
    {
        // Carica la risorsa ZIP incorporata
        var Current_Assembly = Assembly.GetExecutingAssembly();
        var Zip_Resource = Current_Assembly.GetManifestResourceNames().FirstOrDefault(Res => Res.Contains("archives") && Res.EndsWith("samp-client-v.zip"));

        using var Zip_Archive = new ZipArchive(Temp_Buffer, ZipArchiveMode.Read);
        var Total_Files = Zip_Archive.Entries.Count;
        var Processed_Files = new List<string>();

        // Estrae i file con rapporto di progresso
        for (int File_Index = 0; File_Index < Total_Files; File_Index++)
        {
            var Current_Entry = Zip_Archive.Entries[File_Index];
            var File_Target_Path = Path.Combine(Target_Path, Current_Entry.FullName);

            // Riporta il progresso per aggiornamenti dell'interfaccia
            int Completion_Percent = (int)((File_Index + 1) * 100.0 / Total_Files);
            progress.Report((Completion_Percent, Current_Entry.FullName));
        }

        return Processed_Files;
    }
}
```

#### Supporto per le Lingue (`Language.cs`)

Gestisce il sistema di supporto per più lingue utilizzando risorse XML:

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
        // Carica e analizza il file XML di traduzione
        using var Resource_Stream = Current_Assembly.GetManifestResourceStream(Resource_Name);
        var XML_Document = XDocument.Load(Resource_Stream);

        Translation_Dictionary = XML_Document.Descendants("string").ToDictionary(Element => Element.Attribute("key")?.Value ?? string.Empty, Element => Element.Value);
    }
}
```

#### Servizio di Mappatura delle Lingue (`LanguageMapping.cs`)

Gestisce la mappatura tra i nomi delle lingue e i loro codici di immagine delle bandiere corrispondenti:

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
            // Mappature aggiuntive di lingue...
        };
    }

    public string GetImage_Code(string Language_Name) =>
        LanguageTo_ImageCode.TryGetValue(Path.GetFileNameWithoutExtension(Language_Name), out var Code) ? Code : Language_Name.ToLower();
}
```

#### Servizio delle Reti Sociali (`SocialNetworks.cs`)

Gestisce l'apertura dei link delle reti sociali nel browser predefinito:

```csharp
public class Social_Networks
{
    public void OpenSocial_Network(string Network_Name)
    {
        string Network_Url = Network_Name switch
        {
            "Discord SPC" => "https://discord.gg/3fApZh66Tf",
            "YouTube" => "https://youtube.com/@spc-samp",
            // Mappature aggiuntive di reti...
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

#### Componenti dell'Interfaccia Personalizzati

##### Barra di Progresso (`CustomProgressBar.cs`)

Una barra di progresso altamente personalizzata con animazioni e uno stile moderno:

```csharp
public class Custom_ProgressBar : ProgressBar
{
    // Proprietà di personalizzazione
    public Color GradientStart_Color { get; set; }
    public Color GradientEnd_Color { get; set; }
    public int Animation_Speed { get; set; }
    public int Corner_Radius { get; set; }
    public bool Show_Percentage { get; set; }

    protected override void OnPaint(PaintEventArgs e)
    {
        // Implementa il disegno personalizzato con gradienti e animazioni
        using (var Path = GetRounded_Rectangle(Progress_Rect, Corner_Radius_II))
        using (var Gradient = new LinearGradientBrush(Progress_Rect, GradientStart_Color_II, GradientEnd_Color_II, LinearGradientMode.Horizontal))
        {
            // Applica una mescolanza di colori per transizioni morbide
            ColorBlend Blend = new ColorBlend();
            Blend.Positions = Positions;
            Blend.Colors = Colors;
            Gradient.InterpolationColors = Blend;

            // Applica l'animazione di rotazione
            Matrix Matrix = new Matrix();
            Matrix.RotateAt(Animation_Step, new PointF(Progress_Rect.Left + Progress_Rect.Width / 2, Progress_Rect.Top + Progress_Rect.Height / 2));
            Gradient.MultiplyTransform(Matrix);

            e.Graphics.FillPath(Gradient, Path);
        }
    }
}
```

##### Colori del Tema (`Colors.cs`)

Definisce lo schema dei colori dell'applicazione:

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

### Risorse di Sicurezza

#### Privilegi Amministrativi

L'installatore richiede privilegi amministrativi per installare correttamente i file di SA:MP nella directory di GTA:SA. Questo viene gestito tramite il file `adm.manifest`:

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

Principali funzionalità dell'esecuzione amministrativa:
- Garantisce i permessi adeguati per i file durante l'installazione
- Permette la modifica delle directory protette del sistema
- Gestisce automaticamente i prompt UAC (Controllo Account Utente)
- Necessario per modifiche al registro, se necessario

Per abilitare l'esecuzione amministrativa, il file di manifesto è referenziato nel file del progetto:

```xml
<PropertyGroup>
    <ApplicationManifest>adm.manifest</ApplicationManifest>
</PropertyGroup>
```

#### Firma dell'Assembly

Il progetto supporta la firma con chiave forte per una maggiore sicurezza. Questo può essere abilitato nel file del progetto:

```xml
<PropertyGroup>
    <SignAssembly>true</SignAssembly>
    <AssemblyOriginatorKeyFile>MyKey.snk</AssemblyOriginatorKeyFile>
</PropertyGroup>
```

Per generare una chiave forte:

```bash
sn -k MyKey.snk
```

Vantaggi della firma dell'assembly:
- Garantisce l'integrità dell'assembly
- Previene la manomissione dell'assembly
- Fornisce un'identità unica all'assembly
- Permette il deployment nel GAC
- Supporta il deployment ClickOnce

> [!NOTE]
> Mantieni il tuo file di chiave forte (*.snk) sicuro e non sottoporlo al controllo di versione.

### Internazionalizzazione

#### Sistema di Traduzione

Le traduzioni sono memorizzate in file XML con la seguente struttura:

```xml
<translations>
  <string key="continue">Continua</string>
  <string key="cancel">Annulla</string>
  <string key="finish">Completa</string>
  <string key="close">Chiudi</string>
  <!-- Traduzioni aggiuntive -->
</strings>
```

La classe `Language` carica queste traduzioni dinamicamente:

```csharp
public string Translate(string Key) => 
    Translation_Dictionary.TryGetValue(Key, out var Value) ? Value : Key;
```

#### Icone delle Bandierine

Le bandiere delle lingue sono memorizzate come risorse incorporate e caricate dinamicamente:

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

## Configurazione del Progetto (.csproj)

Il file `.csproj` è una componente fondamentale del progetto, che definisce le configurazioni e le proprietà di base dell'applicazione. Di seguito è riportata la struttura dettagliata delle principali configurazioni utilizzate:

### Configurazioni di Base
```xml
<PropertyGroup>
    <OutputType>WinExe</OutputType>
    <TargetFramework>net9.0-windows</TargetFramework>
    <UseWindowsForms>true</UseWindowsForms>
    <ApplicationManifest>adm.manifest</ApplicationManifest>
    <ApplicationIcon>icons\social\ico-spc.ico</ApplicationIcon>
</PropertyGroup>
```

- `OutputType`: Definisce il tipo di output come un eseguibile Windows
- `TargetFramework`: Specifica la versione del .NET Framework utilizzato (9.0)
- `UseWindowsForms`: Abilita l'uso di Windows Forms per l'interfaccia grafica
- `ApplicationManifest`: Definisce il manifesto dell'applicazione per i permessi amministrativi
- `ApplicationIcon`: Definisce l'icona principale dell'applicazione

### Informazioni sulla Versione e sull'Azienda
```xml
<PropertyGroup>
    <AssemblyVersion>1.0.0.0</AssemblyVersion>
    <FileVersion>1.0.0.0</FileVersion>
    <Company>SA-MP Programming Community</Company>
    <Product>samp-client-v</Product>
    <Copyright>Copyright © SPC</Copyright>
    <Description>Installer del mod (San Andreas Multiplayer) versione 0.3.7 V.</Description>
</PropertyGroup>
```

- `AssemblyVersion`: Versione dell'assembly del progetto
- `FileVersion`: Versione del file eseguibile
- `Company`: Nome dell'azienda/organizzazione
- `Product`: Nome del prodotto
- `Copyright`: Informazioni sul copyright
- `Description`: Descrizione del progetto

### Configurazioni di Runtime
```xml
<PropertyGroup>
    <RollForward>LatestMajor</RollForward>
    <RuntimeFrameworkVersion>9.0.0</RuntimeFrameworkVersion>
</PropertyGroup>
```

- `RollForward`: Configura il comportamento di aggiornamento del runtime
- `RuntimeFrameworkVersion`: Specifica la versione esatta del runtime .NET

### Risorse Incorporate
```xml
<ItemGroup>
    <EmbeddedResource Include="archives\**\*" />
    <EmbeddedResource Include="icons\**\*" />
    <EmbeddedResource Include="translations\**\*" />
</ItemGroup>
```

Questa sezione definisce le risorse che verranno incorporate nell'eseguibile finale:
- `archives`: File necessari per l'installatore
- `icons`: Icone e risorse visive
- `translations`: File di traduzione per diverse lingue

### Osservazioni Importanti

1. Il progetto è configurato come un eseguibile Windows Forms, adatto per creare un'interfaccia grafica utente.
2. L'applicazione è indirizzata alla versione 9.0 di .NET, garantendo compatibilità con le funzionalità più recenti del framework.
3. Risorse come icone, file e traduzioni sono incorporate direttamente nell'eseguibile, facilitando la distribuzione.
4. Le configurazioni di versione e le informazioni sull'azienda sono importanti per identificare il software.

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

Errori:

![Error 1 Client - SPC](/screenshots/error_1.png)
![Error 2 Client - SPC](/screenshots/error_2.png)