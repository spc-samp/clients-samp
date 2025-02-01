# clients-samp

[![Licença](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![C#](https://img.shields.io/badge/C%23-11.0-blue.svg)](https://docs.microsoft.com/en-us/dotnet/csharp/)
[![.NET](https://img.shields.io/badge/.NET-9.0-purple.svg)](https://dotnet.microsoft.com/)
[![Windows Forms](https://img.shields.io/badge/Windows%20Forms-net9.0--windows-blue)](https://docs.microsoft.com/en-us/dotnet/desktop/winforms/)

To repo zawiera kod źródłowy kilku instalatorów Client SA:MP (San Andreas Multiplayer) opracowanych przez SPC (SA-MP Programming Community). Te instalatory zostały stworzone, aby zapewnić bezpieczne i niezawodne alternatywy dla oryginalnych instalatorów moda, które nie są już uważane za wiarygodne.

## Języki

- Português: [README](../../)
- Deutsch: [README](../Deutsch/README.md)
- English: [README](../English/README.md)
- Español: [README](../Espanol/README.md)
- Français: [README](../Francais/README.md)
- Italiano: [README](../Italiano/README.md)
- Русский: [README](../Русский/README.md)
- Svenska: [README](../Svenska/README.md)
- Türkçe: [README](../Turkce/README.md)

## Spis treści

- [clients-samp](#clients-samp)
  - [Języki](#języki)
  - [Spis treści](#spis-treści)
  - [Przegląd](#przegląd)
  - [Dostępne Wersje](#dostępne-wersje)
  - [Struktura Projektu](#struktura-projektu)
  - [Funkcjonalności](#funkcjonalności)
  - [Instalacja](#instalacja)
  - [Kompilacja](#kompilacja)
    - [Wymagania wstępne](#wymagania-wstępne)
    - [Jak skompilować](#jak-skompilować)
  - [Struktura Kodu i Komponenty](#struktura-kodu-i-komponenty)
    - [Główne Komponenty](#główne-komponenty)
      - [Instalator Klienta (`InstallerClient.cs`)](#instalator-klienta-installerclientcs)
    - [Usługi](#usługi)
      - [Usługa Ekstrakcji Plików (`FileExtraction.cs`)](#usługa-ekstrakcji-plików-fileextractioncs)
      - [Obsługa Języków (`Language.cs`)](#obsługa-języków-languagecs)
      - [Usługa Mapowania Języków (`LanguageMapping.cs`)](#usługa-mapowania-języków-languagemappingcs)
      - [Usługa Sieci Społecznościowych (`SocialNetworks.cs`)](#usługa-sieci-społecznościowych-socialnetworkscs)
      - [Niestandardowe Komponenty Interfejsu](#niestandardowe-komponenty-interfejsu)
        - [Pasek Postępu (`CustomProgressBar.cs`)](#pasek-postępu-customprogressbarcs)
        - [Kolory Motywu (`Colors.cs`)](#kolory-motywu-colorscs)
    - [Zasoby Bezpieczeństwa](#zasoby-bezpieczeństwa)
      - [Uprawnienia Administracyjne](#uprawnienia-administracyjne)
      - [Podpisywanie Zestawu](#podpisywanie-zestawu)
    - [Internacjonalizacja](#internacjonalizacja)
      - [System Tłumaczeń](#system-tłumaczeń)
      - [Ikony Flag](#ikony-flag)
  - [Konfiguracja Projektu (.csproj)](#konfiguracja-projektu-csproj)
    - [Ustawienia Podstawowe](#ustawienia-podstawowe)
    - [Informacje o Wersji i Firmie](#informacje-o-wersji-i-firmie)
    - [Ustawienia Runtime](#ustawienia-runtime)
    - [Zasoby Osadzone](#zasoby-osadzone)
    - [Ważne Uwagi](#ważne-uwagi)
  - [Screenshots](#screenshots)
  - [Licencja](#licencja)
    - [Warunki użytkowania](#warunki-użytkowania)
      - [1. Przyznane uprawnienia](#1-przyznane-uprawnienia)
      - [2. Obowiązkowe warunki](#2-obowiązkowe-warunki)
      - [3. Ograniczenia](#3-ograniczenia)
      - [4. Własność intelektualna](#4-własność-intelektualna)
      - [5. Wyłączenie gwarancji i ograniczenie odpowiedzialności](#5-wyłączenie-gwarancji-i-ograniczenie-odpowiedzialności)

## Przegląd

Celem projektu jest dostarczenie bezpiecznych i niezawodnych instalatorów dla różnych wersji moda SA:MP. Każdy instalator jest rozwijany w C# przy użyciu Windows Forms, oferując nowoczesny i przyjazny interfejs z obsługą wielu języków oraz oknem z mediami społecznościowymi.

## Dostępne Wersje

Repozytorium zawiera następujące wersje Klienta:

- `samp-client-dl-r1`: Instalator Klienta DL R1
- `samp-client-r1`: Instalator Klienta R1
- `samp-client-r1-voip`: Klient R1 z integracją SAMPVOICE
- `samp-client-r2`: Instalator Klienta R2
- `samp-client-r3`: Instalator Klienta R3
- `samp-client-r3-voip`: Klient R3 z integracją SAMPVOICE
- `samp-client-r4`: Instalator Klienta R4
- `samp-client-r5`: Instalator Klienta R5

## Struktura Projektu

Każda wersja Klienta ma spójną strukturę projektu:

```
clients-samp/
└── samp-client-v/
    ├── archives/
    │   └── samp-client-{v}.zip
    ├── icons/
    │   ├── languages/
    │   │   └── [ikony flag języków]
    │   └── social/
    │       └── [ikony mediów społecznościowych]
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
    │   └── [30 plików XML z językami]
    ├── adm.manifest
    ├── compile.bat
    ├── Main.cs
    └── samp-client-{v}.csproj
```

## Funkcjonalności

- Obsługa wielu języków (30 języków)
- Nowoczesny i intuicyjny interfejs użytkownika
- Bezpieczne wyodrębnianie i instalowanie plików
- Walidacja katalogu gry
- Śledzenie postępu w czasie rzeczywistym
- Okno z mediami społecznościowymi
- Opcjonalne podpisywanie plików assembly dla lepszego bezpieczeństwa
- Niestandardowy pasek postępu z animacjami
- Spójne schematy kolorów i stylów

## Instalacja

1. Wejdź na stronę [releases](https://github.com/spc-samp/clients-samp/releases) projektu
2. Pobierz najnowszą wersję skompilowanego Klienta
3. Uruchom i postępuj zgodnie z instrukcjami

## Kompilacja

### Wymagania wstępne

- SDK .NET 9.0 lub nowsze
- System operacyjny Windows
- Visual Studio 2022 lub nowsze (opcjonalnie)
- Visual Studio Code (opcjonalnie)

### Jak skompilować

Najłatwiejszym sposobem kompilacji dowolnej wersji Klienta jest użycie dostarczonego pliku wsadowego:

1. Otwórz terminal w katalogu wersji Klienta
2. Wykonaj polecenie kompilacji:
```bash
.\compile
```

Możesz także skompilować bezpośrednio przy użyciu CLI .NET:
```bash
dotnet publish -c Release -r win-x64 --self-contained true -p:PublishSingleFile=true -p:EnableCompressionInSingleFile=true -o ./published
```

> [!NOTE]
> To polecenie wygeneruje pojedynczy plik wykonywalny zoptymalizowany dla Windows 64-bit, zawierający wszystkie wymagane zależności. Plik wykonywalny zostanie utworzony w folderze `published` w katalogu projektu.

## Struktura Kodu i Komponenty

### Główne Komponenty

#### Instalator Klienta (`InstallerClient.cs`)

Główny formularz zarządzający całym procesem instalacji. Implementuje interfejs kreatora krok po kroku:

```csharp
public partial class Installer_Client : Form
{
    // Główne moduły
    private File_Extraction Extraction_Module;
    private Language Language_Module;
    private Language_Mapping LanguageMapping_Module;
    private Social_Networks SocialNetworks_Module;

    // Elementy interfejsu
    private Label Description_Label, Status_Label;
    private Custom_ProgressBar Progress_Bar;
    private ListBox ExtractedFiles_List;
}
```

Główne funkcje i odpowiedzialności:

1. **Wybór Języka**
   ```csharp
   private void CreateLanguage_Buttons()
   {
       // Tworzy siatkę przycisków językowych z flagami
       Panel Button_Panel = new Panel
       {
           AutoScroll = true,
           Dock = DockStyle.None,
           Location = new Point(0, 140),
           Width = this.ClientSize.Width,
           Height = this.ClientSize.Height - 140
       };
       
       // Dynamiczne tworzenie przycisków z flagami
       for (int i = 0; i < Available_Languages.Count; i++)
       {
           var Language = Available_Languages[i];
           var Language_Button = CreateLanguage_Button(Language, Icon_Size, Button_Width, Button_Height, i, MaxButtons_PerRow, Padding);
           Button_Panel.Controls.Add(Language_Button);
       }
   }
   ```

2. **Wybór Katalogu Instalacji**
   ```csharp
   private void Selecting_Folder()
   {
       // Dialog wyboru folderu z walidacją
       using var Dialog = new FolderBrowserDialog();
       if (Dialog.ShowDialog() == DialogResult.OK)
       {
           Selected_Path = Dialog.SelectedPath;
           // Walidacja katalogu instalacyjnego GTA:SA
           if (Path.GetFileName(Selected_Path) != "Grand Theft Auto San Andreas")
           {
               Status_Label.Text = Translate("invalid_folder");
               Status_Label.ForeColor = Color.Red;
           }
       }
   }
   ```

3. **Proces Ekstrakcji Plików**
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

4. **Okno z Sieciami Społecznościowymi**
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

       // Tworzy przyciski dla każdej sieci społecznościowej z ikonami
       for (int i = 0; i < Social_Networks.Length; i++)
       {
           var Social_Button = CreateSocial_NetworkButton(Social_Networks[i], Icon_Size, Button_Width, Button_Height, i, Padding);
           Controls.Add(Social_Button);
       }
   }
   ```

### Usługi

#### Usługa Ekstrakcji Plików (`FileExtraction.cs`)

Zarządza bezpieczną ekstrakcją plików klienta SA:MP z wbudowanych zasobów:

```csharp
public class File_Extraction
{
    public async Task<List<string>> ExtractClient_Files(string Target_Path, IProgress<(int progress, string fileName)> progress)
    {
        // Ładuje wbudowany zasób ZIP
        var Current_Assembly = Assembly.GetExecutingAssembly();
        var Zip_Resource = Current_Assembly.GetManifestResourceNames().FirstOrDefault(Res => Res.Contains("archives") && Res.EndsWith("samp-client-v.zip"));

        using var Zip_Archive = new ZipArchive(Temp_Buffer, ZipArchiveMode.Read);
        var Total_Files = Zip_Archive.Entries.Count;
        var Processed_Files = new List<string>();

        // Ekstrahuje pliki z raportem postępu
        for (int File_Index = 0; File_Index < Total_Files; File_Index++)
        {
            var Current_Entry = Zip_Archive.Entries[File_Index];
            var File_Target_Path = Path.Combine(Target_Path, Current_Entry.FullName);

            // Raportuje postęp dla aktualizacji interfejsu
            int Completion_Percent = (int)((File_Index + 1) * 100.0 / Total_Files);
            progress.Report((Completion_Percent, Current_Entry.FullName));
        }

        return Processed_Files;
    }
}
```

#### Obsługa Języków (`Language.cs`)

Zarządza systemem obsługi wielu języków za pomocą zasobów XML:

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
        // Ładuje i analizuje plik XML tłumaczenia
        using var Resource_Stream = Current_Assembly.GetManifestResourceStream(Resource_Name);
        var XML_Document = XDocument.Load(Resource_Stream);

        Translation_Dictionary = XML_Document.Descendants("string").ToDictionary(Element => Element.Attribute("key")?.Value ?? string.Empty, Element => Element.Value);
    }
}
```

#### Usługa Mapowania Języków (`LanguageMapping.cs`)

Zarządza mapowaniem nazw języków i odpowiadających im kodów obrazów flag:

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
            // Dodatkowe mapowania języków...
        };
    }

    public string GetImage_Code(string Language_Name) =>
        LanguageTo_ImageCode.TryGetValue(Path.GetFileNameWithoutExtension(Language_Name), out var Code) ? Code : Language_Name.ToLower();
}
```

#### Usługa Sieci Społecznościowych (`SocialNetworks.cs`)

Zarządza otwieraniem linków do sieci społecznościowych w domyślnej przeglądarki:

```csharp
public class Social_Networks
{
    public void OpenSocial_Network(string Network_Name)
    {
        string Network_Url = Network_Name switch
        {
            "Discord SPC" => "https://discord.gg/3fApZh66Tf",
            "YouTube" => "https://youtube.com/@spc-samp",
            // Dodatkowe mapowania sieci...
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

#### Niestandardowe Komponenty Interfejsu

##### Pasek Postępu (`CustomProgressBar.cs`)

Wysoko spersonalizowany pasek postępu z animacjami i nowoczesnym stylem:

```csharp
public class Custom_ProgressBar : ProgressBar
{
    // Właściwości personalizacji
    public Color GradientStart_Color { get; set; }
    public Color GradientEnd_Color { get; set; }
    public int Animation_Speed { get; set; }
    public int Corner_Radius { get; set; }
    public bool Show_Percentage { get; set; }

    protected override void OnPaint(PaintEventArgs e)
    {
        // Implementuje niestandardowe rysowanie z gradientami i animacjami
        using (var Path = GetRounded_Rectangle(Progress_Rect, Corner_Radius_II))
        using (var Gradient = new LinearGradientBrush(Progress_Rect, GradientStart_Color_II, GradientEnd_Color_II, LinearGradientMode.Horizontal))
        {
            // Zastosowanie mieszania kolorów dla płynnych przejść
            ColorBlend Blend = new ColorBlend();
            Blend.Positions = Positions;
            Blend.Colors = Colors;
            Gradient.InterpolationColors = Blend;

            // Zastosowanie animacji obrotu
            Matrix Matrix = new Matrix();
            Matrix.RotateAt(Animation_Step, new PointF(Progress_Rect.Left + Progress_Rect.Width / 2, Progress_Rect.Top + Progress_Rect.Height / 2));
            Gradient.MultiplyTransform(Matrix);

            e.Graphics.FillPath(Gradient, Path);
        }
    }
}
```

##### Kolory Motywu (`Colors.cs`)

Definiuje schemat kolorów aplikacji:

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

### Zasoby Bezpieczeństwa

#### Uprawnienia Administracyjne

Instalator wymaga uprawnień administracyjnych, aby poprawnie zainstalować pliki SA:MP w katalogu GTA:SA. Zarządza tym plik `adm.manifest`:

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

Główne cechy wykonania administracyjnego:
- Zapewnia odpowiednie uprawnienia do plików w celu instalacji
- Umożliwia modyfikację chronionych katalogów systemowych
- Automatycznie zarządza monitami UAC (Kontrola Konta Użytkownika)
- Wymagane do modyfikacji rejestru, jeśli to konieczne

Aby włączyć wykonanie administracyjne, plik manifestu jest odwołany w pliku projektu:

```xml
<PropertyGroup>
    <ApplicationManifest>adm.manifest</ApplicationManifest>
</PropertyGroup>
```

#### Podpisywanie Zestawu

Projekt wspiera podpisywanie za pomocą silnych nazw w celu poprawy bezpieczeństwa. Można to włączyć w pliku projektu:

```xml
<PropertyGroup>
    <SignAssembly>true</SignAssembly>
    <AssemblyOriginatorKeyFile>MyKey.snk</AssemblyOriginatorKeyFile>
</PropertyGroup>
```

Aby wygenerować silny klucz nazwy:

```bash
sn -k MyKey.snk
```

Korzyści z podpisywania zestawu:
- Zapewnia integralność zestawu
- Zapobiega manipulacjom zestawem
- Daje unikalną tożsamość zestawowi
- Umożliwia wdrożenie w GAC
- Obsługuje wdrożenie ClickOnce

> [!NOTE]
> Zachowaj plik silnego klucza nazwy (*.snk) w bezpiecznym miejscu i nigdy nie umieszczaj go w systemie kontroli wersji.

### Internacjonalizacja

#### System Tłumaczeń

Tłumaczenia są przechowywane w plikach XML o następującej strukturze:

```xml
<translations>
  <string key="continue">Kontynuować</string>
  <string key="cancel">Anulować</string>
  <string key="finish">Zakończyć</string>
  <string key="close">Zamknąć</string>
  <!-- Dodatkowe tłumaczenia -->
</strings>
```

Klasa `Language` dynamicznie ładuje te tłumaczenia:

```csharp
public string Translate(string Key) => 
    Translation_Dictionary.TryGetValue(Key, out var Value) ? Value : Key;
```

#### Ikony Flag

Flagi języków są przechowywane jako zasoby osadzone i ładowane dynamicznie:

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

## Konfiguracja Projektu (.csproj)

Plik `.csproj` jest kluczowym komponentem projektu, który definiuje ustawienia i podstawowe właściwości aplikacji. Poniżej znajduje się szczegółowa struktura głównych ustawień:

### Ustawienia Podstawowe
```xml
<PropertyGroup>
    <OutputType>WinExe</OutputType>
    <TargetFramework>net9.0-windows</TargetFramework>
    <UseWindowsForms>true</UseWindowsForms>
    <ApplicationManifest>adm.manifest</ApplicationManifest>
    <ApplicationIcon>icons\social\ico-spc.ico</ApplicationIcon>
</PropertyGroup>
```

- `OutputType`: Definiuje typ wyjściowy jako plik wykonywalny Windows
- `TargetFramework`: Określa wersję używanego frameworka .NET (9.0)
- `UseWindowsForms`: Włącza użycie Windows Forms do interfejsu graficznego
- `ApplicationManifest`: Definiuje manifest aplikacji dla uprawnień administracyjnych
- `ApplicationIcon`: Określa główną ikonę aplikacji

### Informacje o Wersji i Firmie
```xml
<PropertyGroup>
    <AssemblyVersion>1.0.0.0</AssemblyVersion>
    <FileVersion>1.0.0.0</FileVersion>
    <Company>SA-MP Programming Community</Company>
    <Product>samp-client-v</Product>
    <Copyright>Copyright © SPC</Copyright>
    <Description>Instalator mod (San Andreas Multiplayer) wersja 0.3.7 V.</Description>
</PropertyGroup>
```

- `AssemblyVersion`: Wersja zestawu projektu
- `FileVersion`: Wersja pliku wykonywalnego
- `Company`: Nazwa firmy/organizacji
- `Product`: Nazwa produktu
- `Copyright`: Informacje o prawach autorskich
- `Description`: Opis projektu

### Ustawienia Runtime
```xml
<PropertyGroup>
    <RollForward>LatestMajor</RollForward>
    <RuntimeFrameworkVersion>9.0.0</RuntimeFrameworkVersion>
</PropertyGroup>
```

- `RollForward`: Ustawia zachowanie aktualizacji środowiska wykonawczego
- `RuntimeFrameworkVersion`: Określa dokładną wersję środowiska wykonawczego .NET

### Zasoby Osadzone
```xml
<ItemGroup>
    <EmbeddedResource Include="archives\**\*" />
    <EmbeddedResource Include="icons\**\*" />
    <EmbeddedResource Include="translations\**\*" />
</ItemGroup>
```

Ta sekcja definiuje zasoby, które będą osadzone w końcowym pliku wykonywalnym:
- `archives`: Pliki wymagane do instalatora
- `icons`: Ikony i zasoby wizualne
- `translations`: Pliki tłumaczeń dla różnych języków

### Ważne Uwagi

1. Projekt jest skonfigurowany jako aplikacja Windows Forms, odpowiednia do tworzenia interfejsu graficznego.
2. Aplikacja jest skierowana na .NET 9.0, zapewniając kompatybilność z najnowszymi funkcjami frameworka.
3. Zasoby takie jak ikony, pliki i tłumaczenia są osadzone bezpośrednio w pliku wykonywalnym, co ułatwia dystrybucję.
4. Ustawienia wersji i informacje o firmie są ważne do identyfikacji oprogramowania.

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

Błędy:

![Error 1 Client - SPC](/screenshots/error_1.png)
![Error 2 Client - SPC](/screenshots/error_2.png)

## Licencja

Copyright © **SA-MP Programming Community**

To oprogramowanie jest licencjonowane na warunkach Licencji Apache, Wersja 2.0 ("Licencja"); nie możesz korzystać z tego oprogramowania w sposób niezgodny z Licencją. Kopię Licencji można uzyskać pod adresem: [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)

### Warunki użytkowania

#### 1. Przyznane uprawnienia

Niniejsza licencja bezpłatnie przyznaje każdej osobie, która otrzyma kopię tego oprogramowania i powiązanych plików dokumentacji, następujące prawa:
* Używanie, kopiowanie, modyfikowanie i rozpowszechnianie oprogramowania w dowolnym medium lub formacie, w celach komercyjnych lub niekomercyjnych
* Łączenie, publikowanie, rozpowszechnianie, sublicencjonowanie i/lub sprzedaż kopii oprogramowania
* Zezwalanie osobom, którym oprogramowanie jest udostępniane, na to samo

#### 2. Obowiązkowe warunki

Wszystkie dystrybucje oprogramowania lub prace pochodne muszą:
* Zawierać pełną kopię tej licencji
* Wyraźnie wskazywać wszelkie modyfikacje wprowadzone w oryginalnym kodzie źródłowym
* Zachować wszystkie informacje o prawach autorskich, patentach, znakach towarowych i przypisaniu
* Dostarczyć odpowiednią dokumentację wprowadzonych zmian
* Zachować informację o licencji i gwarancji we wszystkich kopiach

#### 3. Ograniczenia

* Licencja nie przyznaje prawa do używania znaków towarowych, logo lub nazw handlowych **SA-MP Programming Community**
* Wkład do kodu źródłowego musi być licencjonowany na tych samych warunkach co ta licencja
* Wykorzystanie nazw współtwórców do promowania produktów pochodnych tego oprogramowania wymaga uprzedniej szczególnej zgody

#### 4. Własność intelektualna

Oprogramowanie i cała powiązana dokumentacja są chronione prawami autorskimi i międzynarodowymi traktatami. **SA-MP Programming Community** zachowuje wszystkie prawa, tytuły i udziały, które nie zostały wyraźnie przyznane na mocy tej licencji.

#### 5. Wyłączenie gwarancji i ograniczenie odpowiedzialności

OPROGRAMOWANIE JEST DOSTARCZANE "TAK JAK JEST", BEZ JAKICHKOLWIEK GWARANCJI, WYRAŹNYCH LUB DOROZUMIANYCH, W TYM MIĘDZY INNYMI GWARANCJI PRZYDATNOŚCI HANDLOWEJ, PRZYDATNOŚCI DO OKREŚLONEGO CELU I NIENARUSZANIA PRAW.

W ŻADNYM WYPADKU AUTORZY LUB POSIADACZE PRAW AUTORSKICH NIE PONOSZĄ ODPOWIEDZIALNOŚCI ZA JAKIEKOLWIEK ROSZCZENIA, SZKODY LUB INNE ZOBOWIĄZANIA, CZY TO W RAMACH DZIAŁANIA UMOWY, CZYNU NIEDOZWOLONEGO CZY W INNY SPOSÓB, POWSTAŁE W ZWIĄZKU Z OPROGRAMOWANIEM LUB UŻYTKOWANIEM LUB INNYMI CZYNNOŚCIAMI W OPROGRAMOWANIU.

---

Szczegółowe informacje na temat Licencji Apache 2.0 można znaleźć pod adresem: http://www.apache.org/licenses/LICENSE-2.0