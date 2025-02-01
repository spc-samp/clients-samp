# clients-samp

[![Licença](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![C#](https://img.shields.io/badge/C%23-11.0-blue.svg)](https://docs.microsoft.com/en-us/dotnet/csharp/)
[![.NET](https://img.shields.io/badge/.NET-9.0-purple.svg)](https://dotnet.microsoft.com/)
[![Windows Forms](https://img.shields.io/badge/Windows%20Forms-net9.0--windows-blue)](https://docs.microsoft.com/en-us/dotnet/desktop/winforms/)

Ce dépôt contient le code source de plusieurs installateurs de Client SA:MP (San Andreas Multiplayer) développés par la SPC (SA-MP Programming Community). Ces installateurs ont été créés pour fournir des alternatives sûres et fiables aux installateurs originaux du mod, qui ne sont plus considérés comme fiables.

## Langues

- Português: [README](../../)
- Deutsch: [README](../Deutsch/README.md)
- English: [README](../English/README.md)
- Español: [README](../Espanol/README.md)
- Italiano: [README](../Italiano/README.md)
- Polski: [README](../Polski/README.md)
- Русский: [README](../Русский/README.md)
- Svenska: [README](../Svenska/README.md)
- Türkçe: [README](../Turkce/README.md)

## Index

- [clients-samp](#clients-samp)
  - [Langues](#langues)
  - [Index](#index)
  - [Aperçu](#aperçu)
  - [Versions Disponibles](#versions-disponibles)
  - [Structure du Projet](#structure-du-projet)
  - [Fonctionnalités](#fonctionnalités)
  - [Installation](#installation)
  - [Compilation](#compilation)
    - [Prérequis](#prérequis)
    - [Comment compiler](#comment-compiler)
  - [Structure du Code et Composants](#structure-du-code-et-composants)
    - [Composants Principaux](#composants-principaux)
      - [Client Installeur (`InstallerClient.cs`)](#client-installeur-installerclientcs)
    - [Services](#services)
      - [Service d'extraction de fichiers (`FileExtraction.cs`)](#service-dextraction-de-fichiers-fileextractioncs)
      - [Support des langues (`Language.cs`)](#support-des-langues-languagecs)
      - [Service de mappage des langues (`LanguageMapping.cs`)](#service-de-mappage-des-langues-languagemappingcs)
      - [Service des réseaux sociaux (`SocialNetworks.cs`)](#service-des-réseaux-sociaux-socialnetworkscs)
      - [Composants d'interface personnalisés](#composants-dinterface-personnalisés)
        - [Barre de progression (`CustomProgressBar.cs`)](#barre-de-progression-customprogressbarcs)
        - [Couleurs du thème (`Colors.cs`)](#couleurs-du-thème-colorscs)
    - [Fonctionnalités de sécurité](#fonctionnalités-de-sécurité)
      - [Privilèges administratifs](#privilèges-administratifs)
      - [Signature d'Assembly](#signature-dassembly)
    - [Internationalisation](#internationalisation)
      - [Système de traduction](#système-de-traduction)
      - [Icônes de Drapeaux](#icônes-de-drapeaux)
  - [Configuration du projet (.csproj)](#configuration-du-projet-csproj)
    - [Paramètres de base](#paramètres-de-base)
    - [Informations sur la version et l'entreprise](#informations-sur-la-version-et-lentreprise)
    - [Paramètres d'exécution](#paramètres-dexécution)
    - [Ressources intégrées](#ressources-intégrées)
    - [Remarques importantes](#remarques-importantes)
  - [Screenshots](#screenshots)
  - [Licence](#licence)
    - [Conditions Générales d'Utilisation](#conditions-générales-dutilisation)
      - [1. Droits Accordés](#1-droits-accordés)
      - [2. Conditions Obligatoires](#2-conditions-obligatoires)
      - [3. Restrictions et Limitations](#3-restrictions-et-limitations)
      - [4. Propriété Intellectuelle](#4-propriété-intellectuelle)
      - [5. Clause de Non-Garantie et Limitation de Responsabilité](#5-clause-de-non-garantie-et-limitation-de-responsabilité)

## Aperçu

Le projet a pour objectif de fournir des installateurs sûrs et fiables pour différentes versions du mod SA:MP. Chaque installateur est développé en C# utilisant Windows Forms, offrant une interface moderne et conviviale avec un support multilingue et une fenêtre avec les réseaux sociaux.

## Versions Disponibles

Le dépôt inclut les versions suivantes du Client:

- `samp-client-dl-r1`: Installateur du Client DL R1
- `samp-client-r1`: Installateur du Client R1
- `samp-client-r1-voip`: Client R1 avec intégration SAMPVOICE
- `samp-client-r2`: Installateur du Client R2
- `samp-client-r3`: Installateur du Client R3
- `samp-client-r3-voip`: Client R3 avec intégration SAMPVOICE
- `samp-client-r4`: Installateur du Client R4
- `samp-client-r5`: Installateur du Client R5

## Structure du Projet

Chaque version du Client suit une structure de projet cohérente: 

```
clients-samp/
└── samp-client-v/
    ├── archives/
    │   └── samp-client-{v}.zip
    ├── icons/
    │   ├── languages/
    │   │   └── [icônes de drapeaux des langues]
    │   └── social/
    │       └── [icônes des réseaux sociaux]
    ├── src/
    │   ├── Core/
    │   │   └── InstallerClient.cs
    │   ├── Modèles/
    │   │   └── Colors.cs
    │   ├── Services/
    │   │   ├── FileExtraction.cs
    │   │   ├── Language.cs
    │   │   ├── LanguageMapping.cs
    │   │   └── SocialNetworks.cs
    │   └── UI/
    │       └── CustomProgressBar.cs
    ├── translations/
    │   └── [30 fichiers XML de langues]
    ├── adm.manifest
    ├── compile.bat
    ├── Main.cs
    └── samp-client-{v}.csproj
```

## Fonctionnalités

- Prise en charge de plusieurs langues (30 langues)
- Interface utilisateur moderne et intuitive
- Extraction et installation sécurisée des fichiers
- Validation du répertoire du jeu
- Suivi en temps réel de la progression
- Fenêtre avec les réseaux sociaux
- Signature d'assembly optionnelle pour une sécurité renforcée
- Barre de progression personnalisée avec animations
- Schéma de couleurs et style cohérents

## Installation

1. Accédez à la page des [releases](https://github.com/spc-samp/clients-samp/releases) du projet
2. Téléchargez la dernière version du Client déjà compilée
3. Exécutez et suivez les étapes de procédure

## Compilation

### Prérequis

- SDK .NET 9.0 ou supérieur
- Système d'exploitation Windows
- Visual Studio 2022 ou supérieur (optionnel)
- Visual Studio Code (optionnel)

### Comment compiler

La méthode la plus simple pour compiler n'importe quelle version du Client est d'utiliser le fichier batch fourni:

1. Ouvrez un terminal dans le répertoire de la version du Client
2. Exécutez la commande de compilation:
```bash
.\compile
```

Vous pouvez également compiler directement en utilisant le CLI .NET:
```bash
dotnet publish -c Release -r win-x64 --self-contained true -p:PublishSingleFile=true -p:EnableCompressionInSingleFile=true -o ./published
```

> [!NOTE]
> Cette commande générera un fichier exécutable unique et optimisé pour Windows 64 bits, contenant toutes les dépendances nécessaires. Le fichier exécutable sera créé dans le dossier `published` du répertoire du projet.

## Structure du Code et Composants

### Composants Principaux

#### Client Installeur (`InstallerClient.cs`)

Le formulaire principal qui gère tout le processus d'installation. Il implémente une interface de type assistant étape par étape:

```csharp
public partial class Installer_Client : Form
{
    // Modules principaux
    private File_Extraction Extraction_Module;
    private Language Language_Module;
    private Language_Mapping LanguageMapping_Module;
    private Social_Networks SocialNetworks_Module;

    // Éléments de l'interface
    private Label Description_Label, Status_Label;
    private Custom_ProgressBar Progress_Bar;
    private ListBox ExtractedFiles_List;
}
```

Principales fonctionnalités et responsabilités:

1. **Sélection de la langue**
   ```csharp
   private void CreateLanguage_Buttons()
   {
       // Crée une grille de boutons de langue avec des drapeaux
       Panel Button_Panel = new Panel
       {
           AutoScroll = true,
           Dock = DockStyle.None,
           Location = new Point(0, 140),
           Width = this.ClientSize.Width,
           Height = this.ClientSize.Height - 140
       };
       
       // Création dynamique de boutons avec des drapeaux
       for (int i = 0; i < Available_Languages.Count; i++)
       {
           var Language = Available_Languages[i];
           var Language_Button = CreateLanguage_Button(Language, Icon_Size, Button_Width, Button_Height, i, MaxButtons_PerRow, Padding);
           Button_Panel.Controls.Add(Language_Button);
       }
   }
   ```

2. **Sélection du répertoire d'installation**
   ```csharp
   private void Selecting_Folder()
   {
       // Dialogue de sélection de dossier avec validation
       using var Dialog = new FolderBrowserDialog();
       if (Dialog.ShowDialog() == DialogResult.OK)
       {
           Selected_Path = Dialog.SelectedPath;
           // Valide le répertoire d'installation de GTA:SA
           if (Path.GetFileName(Selected_Path) != "Grand Theft Auto San Andreas")
           {
               Status_Label.Text = Translate("invalid_folder");
               Status_Label.ForeColor = Color.Red;
           }
       }
   }
   ```

3. **Processus d'extraction des fichiers**
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

4. **Fenêtre avec les réseaux sociaux**
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

       // Crée des boutons pour chaque réseau social avec des icônes
       for (int i = 0; i < Social_Networks.Length; i++)
       {
           var Social_Button = CreateSocial_NetworkButton(Social_Networks[i], Icon_Size, Button_Width, Button_Height, i, Padding);
           Controls.Add(Social_Button);
       }
   }
   ```

### Services

#### Service d'extraction de fichiers (`FileExtraction.cs`)

Gère l'extraction sécurisée des fichiers du Client SA:MP à partir des ressources intégrées:

```csharp
public class File_Extraction
{
    public async Task<List<string>> ExtractClient_Files(string Target_Path, IProgress<(int progress, string fileName)> progress)
    {
        // Charge la ressource ZIP intégrée
        var Current_Assembly = Assembly.GetExecutingAssembly();
        var Zip_Resource = Current_Assembly.GetManifestResourceNames().FirstOrDefault(Res => Res.Contains("archives") && Res.EndsWith("samp-client-v.zip"));

        using var Zip_Archive = new ZipArchive(Temp_Buffer, ZipArchiveMode.Read);
        var Total_Files = Zip_Archive.Entries.Count;
        var Processed_Files = new List<string>();

        // Extrait les fichiers avec rapport de progression
        for (int File_Index = 0; File_Index < Total_Files; File_Index++)
        {
            var Current_Entry = Zip_Archive.Entries[File_Index];
            var File_Target_Path = Path.Combine(Target_Path, Current_Entry.FullName);

            // Informe la progression pour les mises à jour de l'interface
            int Completion_Percent = (int)((File_Index + 1) * 100.0 / Total_Files);
            progress.Report((Completion_Percent, Current_Entry.FullName));
        }

        return Processed_Files;
    }
}
```

#### Support des langues (`Language.cs`)

Gère le système de support de plusieurs langues à l'aide de ressources XML:

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
        // Charge et analyse le fichier XML de traduction
        using var Resource_Stream = Current_Assembly.GetManifestResourceStream(Resource_Name);
        var XML_Document = XDocument.Load(Resource_Stream);

        Translation_Dictionary = XML_Document.Descendants("string").ToDictionary(Element => Element.Attribute("key")?.Value ?? string.Empty, Element => Element.Value);
    }
}
```

#### Service de mappage des langues (`LanguageMapping.cs`)

Gère le mappage entre les noms de langues et leurs codes d'image de drapeaux correspondants:

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
            // Mappages de langues supplémentaires...
        };
    }

    public string GetImage_Code(string Language_Name) =>
        LanguageTo_ImageCode.TryGetValue(Path.GetFileNameWithoutExtension(Language_Name), out var Code) ? Code : Language_Name.ToLower();
}
```

#### Service des réseaux sociaux (`SocialNetworks.cs`)

Gère l'ouverture des liens des réseaux sociaux dans le navigateur par défaut:

```csharp
public class Social_Networks
{
    public void OpenSocial_Network(string Network_Name)
    {
        string Network_Url = Network_Name switch
        {
            "Discord SPC" => "https://discord.gg/3fApZh66Tf",
            "YouTube" => "https://youtube.com/@spc-samp",
            // Mappages supplémentaires de réseaux...
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

#### Composants d'interface personnalisés

##### Barre de progression (`CustomProgressBar.cs`)

Une barre de progression hautement personnalisée avec animations et style moderne:

```csharp
public class Custom_ProgressBar : ProgressBar
{
    // Propriétés de personnalisation
    public Color GradientStart_Color { get; set; }
    public Color GradientEnd_Color { get; set; }
    public int Animation_Speed { get; set; }
    public int Corner_Radius { get; set; }
    public bool Show_Percentage { get; set; }

    protected override void OnPaint(PaintEventArgs e)
    {
        // Implémente le dessin personnalisé avec des dégradés et des animations
        using (var Path = GetRounded_Rectangle(Progress_Rect, Corner_Radius_II))
        using (var Gradient = new LinearGradientBrush(Progress_Rect, GradientStart_Color_II, GradientEnd_Color_II, LinearGradientMode.Horizontal))
        {
            // Applique un mélange de couleurs pour des transitions douces
            ColorBlend Blend = new ColorBlend();
            Blend.Positions = Positions;
            Blend.Colors = Colors;
            Gradient.InterpolationColors = Blend;

            // Applique une animation de rotation
            Matrix Matrix = new Matrix();
            Matrix.RotateAt(Animation_Step, new PointF(Progress_Rect.Left + Progress_Rect.Width / 2, Progress_Rect.Top + Progress_Rect.Height / 2));
            Gradient.MultiplyTransform(Matrix);

            e.Graphics.FillPath(Gradient, Path);
        }
    }
}
```

##### Couleurs du thème (`Colors.cs`)

Définit le schéma de couleurs de l'application:

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

### Fonctionnalités de sécurité

#### Privilèges administratifs

L'installateur nécessite des privilèges administratifs pour installer correctement les fichiers SA:MP dans le répertoire GTA:SA. Cela est géré via le fichier `adm.manifest`:

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

Principales fonctionnalités de l'exécution administrative:
- Assure les autorisations appropriées pour l'installation des fichiers
- Permet la modification de répertoires système protégés
- Gère automatiquement les invites UAC (Contrôle de compte d'utilisateur)
- Nécessaire pour les modifications du registre, si nécessaire

Pour activer l'exécution administrative, le fichier manifeste est référencé dans le fichier du projet:

```xml
<PropertyGroup>
    <ApplicationManifest>adm.manifest</ApplicationManifest>
</PropertyGroup>
```

#### Signature d'Assembly

Le projet prend en charge la signature avec une clé forte pour une sécurité accrue. Cela peut être activé dans le fichier du projet:

```xml
<PropertyGroup>
    <SignAssembly>true</SignAssembly>
    <AssemblyOriginatorKeyFile>MyKey.snk</AssemblyOriginatorKeyFile>
</PropertyGroup>
```

Pour générer une clé forte:

```bash
sn -k MyKey.snk
```

Avantages de la signature d'assembly:
- Assure l'intégrité de l'assembly
- Empêche la falsification de l'assembly
- Fournit une identité unique à l'assembly
- Permet le déploiement dans le GAC
- Prend en charge le déploiement ClickOnce

> [!NOTE]
> Gardez votre fichier de clé forte (*.snk) sécurisé et ne le soumettez jamais au contrôle de version.

### Internationalisation

#### Système de traduction

Les traductions sont stockées dans des fichiers XML avec la structure suivante:

```xml
<translations>
  <string key="continue">Continuer</string>
  <string key="cancel">Annuler</string>
  <string key="finish">Terminer</string>
  <string key="close">Fermer</string>
  <!-- Traductions supplémentaires -->
</strings>
```

La classe `Language` charge ces traductions dynamiquement:

```csharp
public string Translate(string Key) => 
    Translation_Dictionary.TryGetValue(Key, out var Value) ? Value : Key;
```

#### Icônes de Drapeaux

Les drapeaux des langues sont stockés en tant que ressources embarquées et chargés dynamiquement:

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

## Configuration du projet (.csproj)

Le fichier `.csproj` est un composant crucial du projet qui définit les configurations et propriétés fondamentales de l'application. Voici la structure détaillée des principales configurations utilisées:

### Paramètres de base
```xml
<PropertyGroup>
    <OutputType>WinExe</OutputType>
    <TargetFramework>net9.0-windows</TargetFramework>
    <UseWindowsForms>true</UseWindowsForms>
    <ApplicationManifest>adm.manifest</ApplicationManifest>
    <ApplicationIcon>icons\social\ico-spc.ico</ApplicationIcon>
</PropertyGroup>
```

- `OutputType`: Définit le type de sortie comme un exécutable Windows
- `TargetFramework`: Spécifie la version du framework .NET utilisée (9.0)
- `UseWindowsForms`: Active l'utilisation de Windows Forms pour l'interface graphique
- `ApplicationManifest`: Définit le manifeste de l'application pour les autorisations administratives
- `ApplicationIcon`: Définit l'icône principale de l'application

### Informations sur la version et l'entreprise
```xml
<PropertyGroup>
    <AssemblyVersion>1.0.0.0</AssemblyVersion>
    <FileVersion>1.0.0.0</FileVersion>
    <Company>SA-MP Programming Community</Company>
    <Product>samp-client-v</Product>
    <Copyright>Copyright © SPC</Copyright>
    <Description>Installeur du mod (San Andreas Multiplayer) version 0.3.7 V.</Description>
</PropertyGroup>
```

- `AssemblyVersion`: Version de l'assembly du projet
- `FileVersion`: Version du fichier exécutable
- `Company`: Nom de l'entreprise/organisation
- `Product`: Nom du produit
- `Copyright`: Informations sur les droits d'auteur
- `Description`: Description du projet

### Paramètres d'exécution
```xml
<PropertyGroup>
    <RollForward>LatestMajor</RollForward>
    <RuntimeFrameworkVersion>9.0.0</RuntimeFrameworkVersion>
</PropertyGroup>
```

- `RollForward`: Configure le comportement de mise à jour du runtime
- `RuntimeFrameworkVersion`: Spécifie la version exacte du runtime .NET

### Ressources intégrées
```xml
<ItemGroup>
    <EmbeddedResource Include="archives\**\*" />
    <EmbeddedResource Include="icons\**\*" />
    <EmbeddedResource Include="translations\**\*" />
</ItemGroup>
```

Cette section définit les ressources qui seront intégrées dans l'exécutable final:
- `archives`: Fichiers nécessaires pour l'installateur
- `icons`: Icônes et ressources visuelles
- `translations`: Fichiers de traduction pour différentes langues

### Remarques importantes

1. Le projet est configuré en tant qu'exécutable Windows Forms, adapté à la création d'une interface graphique utilisateur.
2. L'application est dirigée vers .NET 9.0, assurant la compatibilité avec les dernières fonctionnalités du framework.
3. Des ressources comme les icônes, les fichiers et les traductions sont intégrées directement dans l'exécutable, facilitant la distribution.
4. Les paramètres de version et les informations sur l'entreprise sont importants pour l'identification du logiciel.

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

Erreurs:

![Error 1 Client - SPC](/screenshots/error_1.png)
![Error 2 Client - SPC](/screenshots/error_2.png)

## Licence

Copyright © **SA-MP Programming Community**

Ce logiciel est sous licence Apache, Version 2.0 (la "Licence"); vous ne pouvez pas utiliser ce logiciel sauf en conformité avec la Licence. Vous pouvez obtenir une copie de la Licence sur: [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)

### Conditions Générales d'Utilisation

#### 1. Droits Accordés

La présente licence accorde gratuitement à toute personne obtenant une copie de ce logiciel et des fichiers de documentation associés les droits suivants:

* Utiliser, copier, modifier et distribuer le logiciel sur tout support ou format, à toute fin, commerciale ou non-commerciale
* Fusionner, publier, distribuer, sous-licencier et/ou vendre des copies du logiciel
* Permettre aux personnes à qui le logiciel est fourni de faire de même

#### 2. Conditions Obligatoires

Toutes les distributions du logiciel ou des travaux dérivés doivent:

* Inclure une copie complète de cette licence
* Indiquer clairement toutes modifications apportées au code source original
* Préserver tous les avis de droits d'auteur, brevets, marques déposées et attributions
* Fournir une documentation appropriée des modifications implémentées
* Maintenir l'avis de licence et de garantie dans toutes les copies

#### 3. Restrictions et Limitations

* Cette licence n'accorde pas la permission d'utiliser les marques déposées, logos ou noms commerciaux de la **SA-MP Programming Community**
* Les contributions au code source doivent être licenciées sous les mêmes termes que cette licence
* L'utilisation des noms des contributeurs pour approuver ou promouvoir des produits dérivés de ce logiciel nécessite une autorisation préalable spécifique

#### 4. Propriété Intellectuelle

Le logiciel et toute la documentation associée sont protégés par les lois sur les droits d'auteur et les traités internationaux. La **SA-MP Programming Community** conserve tous les droits, titres et intérêts non expressément accordés par cette licence.

#### 5. Clause de Non-Garantie et Limitation de Responsabilité

LE LOGICIEL EST FOURNI "EN L'ÉTAT", SANS GARANTIE D'AUCUNE SORTE, EXPRESSE OU IMPLICITE, Y COMPRIS, MAIS SANS S'Y LIMITER, LES GARANTIES DE COMMERCIALISATION, D'ADÉQUATION À UN USAGE PARTICULIER ET DE NON-VIOLATION.

EN AUCUN CAS LES AUTEURS OU LES TITULAIRES DES DROITS D'AUTEUR NE SERONT RESPONSABLES DE TOUTE RÉCLAMATION, DOMMAGE OU AUTRE RESPONSABILITÉ, QUE CE SOIT DANS LE CADRE D'UN CONTRAT, D'UN DÉLIT OU AUTREMENT, DÉCOULANT DE OU EN LIEN AVEC LE LOGICIEL OU L'UTILISATION OU D'AUTRES TRANSACTIONS DANS LE LOGICIEL.

---

Pour des informations détaillées sur la Licence Apache 2.0, consultez: http://www.apache.org/licenses/LICENSE-2.0