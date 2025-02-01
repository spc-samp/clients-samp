# clients-samp

[![Licença](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![C#](https://img.shields.io/badge/C%23-11.0-blue.svg)](https://docs.microsoft.com/en-us/dotnet/csharp/)
[![.NET](https://img.shields.io/badge/.NET-9.0-purple.svg)](https://dotnet.microsoft.com/)
[![Windows Forms](https://img.shields.io/badge/Windows%20Forms-net9.0--windows-blue)](https://docs.microsoft.com/en-us/dotnet/desktop/winforms/)

Bu depo, SPC (SA-MP Programlama Topluluğu) tarafından geliştirilen çeşitli Client SA:MP (San Andreas Multiplayer) yükleyicilerinin kaynak kodunu içermektedir. Bu yükleyiciler, artık güvenilir olarak kabul edilmeyen modun orijinal yükleyicilerine güvenli ve güvenilir alternatifler sağlamak için oluşturulmuştur.

## Diller

- Português: [README](../../)
- Deutsch: [README](../Deutsch/README.md)
- English: [README](../English/README.md)
- Español: [README](../Espanol/README.md)
- Français: [README](../Francais/README.md)
- Italiano: [README](../Italiano/README.md)
- Polski: [README](../Polski/README.md)
- Русский: [README](../Русский/README.md)
- Svenska: [README](../Svenska/README.md)

## İçindekiler

- [clients-samp](#clients-samp)
  - [Diller](#diller)
  - [İçindekiler](#i̇çindekiler)
  - [Genel Bakış](#genel-bakış)
  - [Mevcut Sürümler](#mevcut-sürümler)
  - [Proje Yapısı](#proje-yapısı)
  - [Özellikler](#özellikler)
  - [Yükleme](#yükleme)
  - [Derleme](#derleme)
    - [Önkoşullar](#önkoşullar)
    - [Nasıl Derlenir](#nasıl-derlenir)
  - [Kod Yapısı ve Bileşenler](#kod-yapısı-ve-bileşenler)
    - [Ana Bileşenler](#ana-bileşenler)
      - [İstemci Yükleyici (`InstallerClient.cs`)](#i̇stemci-yükleyici-installerclientcs)
    - [Servisler](#servisler)
      - [Dosya Çıkartma Servisi (`FileExtraction.cs`)](#dosya-çıkartma-servisi-fileextractioncs)
      - [Dil Desteği (`Language.cs`)](#dil-desteği-languagecs)
      - [Dil Eşleştirme Servisi (`LanguageMapping.cs`)](#dil-eşleştirme-servisi-languagemappingcs)
      - [Sosyal Medya Servisi (`SocialNetworks.cs`)](#sosyal-medya-servisi-socialnetworkscs)
      - [Özelleştirilmiş Arayüz Bileşenleri](#özelleştirilmiş-arayüz-bileşenleri)
        - [İlerleme Çubuğu (`CustomProgressBar.cs`)](#i̇lerleme-çubuğu-customprogressbarcs)
        - [Tema Renkleri (`Colors.cs`)](#tema-renkleri-colorscs)
    - [Güvenlik Özellikleri](#güvenlik-özellikleri)
      - [Yönetici Yetkileri](#yönetici-yetkileri)
      - [Assembly İmzası](#assembly-i̇mzası)
    - [Uluslararasılaştırma](#uluslararasılaştırma)
      - [Çeviri Sistemi](#çeviri-sistemi)
      - [Bayrak Simgeleri](#bayrak-simgeleri)
  - [Proje Yapılandırması (.csproj)](#proje-yapılandırması-csproj)
    - [Temel Yapılandırmalar](#temel-yapılandırmalar)
    - [Sürüm ve Şirket Bilgileri](#sürüm-ve-şirket-bilgileri)
    - [Çalışma Zamanı Yapılandırmaları](#çalışma-zamanı-yapılandırmaları)
    - [Yerleşik Kaynaklar](#yerleşik-kaynaklar)
    - [Önemli Notlar](#önemli-notlar)
  - [Screenshots](#screenshots)
  - [Lisans](#lisans)
    - [Kullanım Şartları ve Koşulları](#kullanım-şartları-ve-koşulları)
      - [1. Verilen İzinler](#1-verilen-i̇zinler)
      - [2. Zorunlu Koşullar](#2-zorunlu-koşullar)
      - [3. Kısıtlamalar ve Sınırlamalar](#3-kısıtlamalar-ve-sınırlamalar)
      - [4. Fikri Mülkiyet](#4-fikri-mülkiyet)
      - [5. Garanti Reddi ve Sorumluluk Sınırlaması](#5-garanti-reddi-ve-sorumluluk-sınırlaması)

## Genel Bakış

Bu proje, SA:MP modunun farklı sürümleri için güvenli ve güvenilir yükleyiciler sağlamayı amaçlamaktadır. Her yükleyici, Windows Forms kullanılarak C# ile geliştirilmiştir ve modern, kullanıcı dostu bir arayüz sunar. Ayrıca çoklu dil desteği ve sosyal medya bağlantılarının bulunduğu bir pencere içerir.

## Mevcut Sürümler

Depo, aşağıdaki Client sürümlerini içermektedir:

- `samp-client-dl-r1`: Client DL R1 Yükleyicisi
- `samp-client-r1`: Client R1 Yükleyicisi
- `samp-client-r1-voip`: SAMPVOICE entegrasyonu ile Client R1
- `samp-client-r2`: Client R2 Yükleyicisi
- `samp-client-r3`: Client R3 Yükleyicisi
- `samp-client-r3-voip`: SAMPVOICE entegrasyonu ile Client R3
- `samp-client-r4`: Client R4 Yükleyicisi
- `samp-client-r5`: Client R5 Yükleyicisi

## Proje Yapısı

Her Client sürümü, tutarlı bir proje yapısını takip eder:

```
clients-samp/
└── samp-client-v/
    ├── archives/
    │   └── samp-client-{v}.zip
    ├── icons/
    │   ├── languages/
    │   │   └── [dillerin bayrak ikonları]
    │   └── social/
    │       └── [sosyal medya ikonları]
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
    │   └── [30 dil dosyası XML]
    ├── adm.manifest
    ├── compile.bat
    ├── Main.cs
    └── samp-client-{v}.csproj
```

## Özellikler

- Çoklu dil desteği (30 dil)
- Modern ve sezgisel kullanıcı arayüzü
- Güvenli dosya çıkarımı ve yükleme
- Oyun dizininin doğrulanması
- Gerçek zamanlı ilerleme takibi
- Sosyal medya penceresi
- Gelişmiş güvenlik için isteğe bağlı assembly imzası
- Animasyonlu özel ilerleme çubuğu
- Tutarlı renk şeması ve stil

## Yükleme

1. Projenin [releases](https://github.com/spc-samp/clients-samp/releases) sayfasına gidin
2. Derlenmiş en son Client sürümünü indirin
3. Çalıştırın ve talimatları izleyin

## Derleme

### Önkoşullar

- .NET SDK 9.0 veya daha üstü
- Windows işletim sistemi
- Visual Studio 2022 veya üstü (isteğe bağlı)
- Visual Studio Code (isteğe bağlı)

### Nasıl Derlenir

Herhangi bir Client sürümünü derlemenin en kolay yolu sağlanan batch dosyasını kullanmaktır:

1. Client sürümünün bulunduğu dizinde bir terminal açın
2. Derleme komutunu çalıştırın:
```bash
.\compile
```

Ayrıca, doğrudan .NET CLI kullanarak derleme yapabilirsiniz:
```bash
dotnet publish -c Release -r win-x64 --self-contained true -p:PublishSingleFile=true -p:EnableCompressionInSingleFile=true -o ./published
```

> [!NOTE]
> Bu komut, tüm gerekli bağımlılıkları içeren ve Windows 64-bit için optimize edilmiş tek bir çalıştırılabilir dosya oluşturacaktır. Çalıştırılabilir dosya, proje dizinindeki `published` klasörüne kaydedilecektir.

## Kod Yapısı ve Bileşenler

### Ana Bileşenler

#### İstemci Yükleyici (`InstallerClient.cs`)

Tüm yükleme sürecini yöneten ana form. Adım adım bir sihirbaz arayüzü uygular:

```csharp
public partial class Installer_Client : Form
{
    // Ana modüller
    private File_Extraction Extraction_Module;
    private Language Language_Module;
    private Language_Mapping LanguageMapping_Module;
    private Social_Networks SocialNetworks_Module;

    // Arayüz bileşenleri
    private Label Description_Label, Status_Label;
    private Custom_ProgressBar Progress_Bar;
    private ListBox ExtractedFiles_List;
}
```

Ana özellikler ve sorumluluklar:

1. **Dil Seçimi**
   ```csharp
   private void CreateLanguage_Buttons()
   {
       // Bayraklarla dil düğmeleri için bir ızgara oluşturur
       Panel Button_Panel = new Panel
       {
           AutoScroll = true,
           Dock = DockStyle.None,
           Location = new Point(0, 140),
           Width = this.ClientSize.Width,
           Height = this.ClientSize.Height - 140
       };
       
       // Bayraklarla dinamik dil düğmeleri oluşturur
       for (int i = 0; i < Available_Languages.Count; i++)
       {
           var Language = Available_Languages[i];
           var Language_Button = CreateLanguage_Button(Language, Icon_Size, Button_Width, Button_Height, i, MaxButtons_PerRow, Padding);
           Button_Panel.Controls.Add(Language_Button);
       }
   }
   ```

2. **Yükleme Dizini Seçimi**
   ```csharp
   private void Selecting_Folder()
   {
       // Klasör seçim diyaloğu ve doğrulama
       using var Dialog = new FolderBrowserDialog();
       if (Dialog.ShowDialog() == DialogResult.OK)
       {
           Selected_Path = Dialog.SelectedPath;
           // GTA:SA yükleme dizinini doğrular
           if (Path.GetFileName(Selected_Path) != "Grand Theft Auto San Andreas")
           {
               Status_Label.Text = Translate("invalid_folder");
               Status_Label.ForeColor = Color.Red;
           }
       }
   }
   ```

3. **Dosya Çıkartma Süreci**
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

4. **Sosyal Medya Penceresi**
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

       // Her sosyal medya için simgelerle düğmeler oluşturur
       for (int i = 0; i < Social_Networks.Length; i++)
       {
           var Social_Button = CreateSocial_NetworkButton(Social_Networks[i], Icon_Size, Button_Width, Button_Height, i, Padding);
           Controls.Add(Social_Button);
       }
   }
   ```

### Servisler

#### Dosya Çıkartma Servisi (`FileExtraction.cs`)

İstemci SA:MP dosyalarının güvenli bir şekilde çıkartılmasını yönetir:

```csharp
public class File_Extraction
{
    public async Task<List<string>> ExtractClient_Files(string Target_Path, IProgress<(int progress, string fileName)> progress)
    {
        // Gömülü ZIP kaynağını yükler
        var Current_Assembly = Assembly.GetExecutingAssembly();
        var Zip_Resource = Current_Assembly.GetManifestResourceNames().FirstOrDefault(Res => Res.Contains("archives") && Res.EndsWith("samp-client-v.zip"));

        using var Zip_Archive = new ZipArchive(Temp_Buffer, ZipArchiveMode.Read);
        var Total_Files = Zip_Archive.Entries.Count;
        var Processed_Files = new List<string>();

        // Dosyaları ilerleme raporuyla çıkartır
        for (int File_Index = 0; File_Index < Total_Files; File_Index++)
        {
            var Current_Entry = Zip_Archive.Entries[File_Index];
            var File_Target_Path = Path.Combine(Target_Path, Current_Entry.FullName);

            // Arayüz güncellemeleri için ilerlemeyi raporlar
            int Completion_Percent = (int)((File_Index + 1) * 100.0 / Total_Files);
            progress.Report((Completion_Percent, Current_Entry.FullName));
        }

        return Processed_Files;
    }
}
```

#### Dil Desteği (`Language.cs`)

XML kaynaklarını kullanarak çoklu dil desteği sistemini yönetir:

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
        // Çeviri XML dosyasını yükler ve analiz eder
        using var Resource_Stream = Current_Assembly.GetManifestResourceStream(Resource_Name);
        var XML_Document = XDocument.Load(Resource_Stream);

        Translation_Dictionary = XML_Document.Descendants("string").ToDictionary(Element => Element.Attribute("key")?.Value ?? string.Empty, Element => Element.Value);
    }
}
```

#### Dil Eşleştirme Servisi (`LanguageMapping.cs`)

Dil isimleri ile bunlara karşılık gelen bayrak simge kodları arasındaki eşleştirmeyi yönetir:

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
            // Diğer dil eşleştirmeleri...
        };
    }

    public string GetImage_Code(string Language_Name) =>
        LanguageTo_ImageCode.TryGetValue(Path.GetFileNameWithoutExtension(Language_Name), out var Code) ? Code : Language_Name.ToLower();
}
```

#### Sosyal Medya Servisi (`SocialNetworks.cs`)

Sosyal medya bağlantılarının tarayıcıda açılmasını yönetir:

```csharp
public class Social_Networks
{
    public void OpenSocial_Network(string Network_Name)
    {
        string Network_Url = Network_Name switch
        {
            "Discord SPC" => "https://discord.gg/3fApZh66Tf",
            "YouTube" => "https://youtube.com/@spc-samp",
            // Diğer sosyal medya eşleştirmeleri...
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

#### Özelleştirilmiş Arayüz Bileşenleri

##### İlerleme Çubuğu (`CustomProgressBar.cs`)

Animasyonlar ve modern tarzla yüksek düzeyde özelleştirilmiş bir ilerleme çubuğu:

```csharp
public class Custom_ProgressBar : ProgressBar
{
    // Özelleştirme özellikleri
    public Color GradientStart_Color { get; set; }
    public Color GradientEnd_Color { get; set; }
    public int Animation_Speed { get; set; }
    public int Corner_Radius { get; set; }
    public bool Show_Percentage { get; set; }

    protected override void OnPaint(PaintEventArgs e)
    {
        // Özelleştirilmiş çizim, gradyanlar ve animasyonlar uygular
        using (var Path = GetRounded_Rectangle(Progress_Rect, Corner_Radius_II))
        using (var Gradient = new LinearGradientBrush(Progress_Rect, GradientStart_Color_II, GradientEnd_Color_II, LinearGradientMode.Horizontal))
        {
            // Yumuşak geçişler için renk karışımı uygular
            ColorBlend Blend = new ColorBlend();
            Blend.Positions = Positions;
            Blend.Colors = Colors;
            Gradient.InterpolationColors = Blend;

            // Döndürme animasyonu uygular
            Matrix Matrix = new Matrix();
            Matrix.RotateAt(Animation_Step, new PointF(Progress_Rect.Left + Progress_Rect.Width / 2, Progress_Rect.Top + Progress_Rect.Height / 2));
            Gradient.MultiplyTransform(Matrix);

            e.Graphics.FillPath(Gradient, Path);
        }
    }
}
```

##### Tema Renkleri (`Colors.cs`)

Uygulamanın renk şemasını tanımlar:

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

### Güvenlik Özellikleri

#### Yönetici Yetkileri

Yükleyici, SA:MP dosyalarını GTA:SA dizinine doğru şekilde yüklemek için yönetici yetkileri gerektirir. Bu, `adm.manifest` dosyası aracılığıyla yönetilir:

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

Yönetici yürütme özelliklerinin başlıca avantajları:
- Yükleme için uygun dosya izinlerini garanti eder
- Korunan sistem dizinlerini değiştirmeye izin verir
- UAC (Kullanıcı Hesabı Denetimi) istemlerini otomatik olarak yönetir
- Gerektiğinde kayıt defteri değişiklikleri için gereklidir

Yönetici yürütmesini etkinleştirmek için, manifest dosyası proje dosyasına referans olarak eklenir:

```xml
<PropertyGroup>
    <ApplicationManifest>adm.manifest</ApplicationManifest>
</PropertyGroup>
```

#### Assembly İmzası

Proje, gelişmiş güvenlik için güçlü adla imzalamayı destekler. Bu, proje dosyasında etkinleştirilebilir:

```xml
<PropertyGroup>
    <SignAssembly>true</SignAssembly>
    <AssemblyOriginatorKeyFile>MyKey.snk</AssemblyOriginatorKeyFile>
</PropertyGroup>
```

Güçlü ad anahtarı oluşturmak için:

```bash
sn -k MyKey.snk
```

Assembly imzasının faydaları:
- Assembly'nin bütünlüğünü garanti eder
- Assembly'nin değiştirilmesini engeller
- Assembly'e benzersiz bir kimlik sağlar
- GAC'a dağıtım yapmaya izin verir
- ClickOnce dağıtımını destekler

> [!NOT]
> Güçlü ad anahtar dosyanızı (*.snk) güvende tutun ve asla kaynak kontrolüne göndermeyin.

### Uluslararasılaştırma

#### Çeviri Sistemi

Çeviriler, aşağıdaki yapıya sahip XML dosyalarında saklanır:

```xml
<translations>
  <string key="continue">Devam Et</string>
  <string key="cancel">İptal Et</string>
  <string key="finish">Tamamla</string>
  <string key="close">Kapat</string>
  <!-- Ek çeviriler -->
</translations>
```

`Language` sınıfı bu çevirileri dinamik olarak yükler:

```csharp
public string Translate(string Key) => 
    Translation_Dictionary.TryGetValue(Key, out var Value) ? Value : Key;
```

#### Bayrak Simgeleri

Dil bayrakları, yerleşik kaynaklar olarak saklanır ve dinamik olarak yüklenir:

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

## Proje Yapılandırması (.csproj)

`.csproj` dosyası, uygulamanın temel yapılandırmalarını ve özelliklerini tanımlayan önemli bir bileşendir. Aşağıda, kullanılan başlıca yapılandırmaların ayrıntılı yapısı verilmiştir:

### Temel Yapılandırmalar
```xml
<PropertyGroup>
    <OutputType>WinExe</OutputType>
    <TargetFramework>net9.0-windows</TargetFramework>
    <UseWindowsForms>true</UseWindowsForms>
    <ApplicationManifest>adm.manifest</ApplicationManifest>
    <ApplicationIcon>icons\social\ico-spc.ico</ApplicationIcon>
</PropertyGroup>
```

- `OutputType`: Çıktı türünü bir Windows yürütülebilir dosyası olarak tanımlar
- `TargetFramework`: Kullanılan .NET Framework sürümünü belirtir (9.0)
- `UseWindowsForms`: Grafiksel kullanıcı arayüzü için Windows Forms kullanımını etkinleştirir
- `ApplicationManifest`: Uygulama için yönetici izinlerini tanımlayan manifest dosyasını belirler
- `ApplicationIcon`: Uygulamanın ana simgesini tanımlar

### Sürüm ve Şirket Bilgileri
```xml
<PropertyGroup>
    <AssemblyVersion>1.0.0.0</AssemblyVersion>
    <FileVersion>1.0.0.0</FileVersion>
    <Company>SA-MP Programming Community</Company>
    <Product>samp-client-v</Product>
    <Copyright>Copyright © SPC</Copyright>
    <Description>Mod yükleyicisi (San Andreas Multiplayer) sürüm 0.3.7 V.</Description>
</PropertyGroup>
```

- `AssemblyVersion`: Projenin assembly sürümü
- `FileVersion`: Yürütülebilir dosyanın sürümü
- `Company`: Şirket/organizasyon adı
- `Product`: Ürün adı
- `Copyright`: Telif hakkı bilgileri
- `Description`: Proje açıklaması

### Çalışma Zamanı Yapılandırmaları
```xml
<PropertyGroup>
    <RollForward>LatestMajor</RollForward>
    <RuntimeFrameworkVersion>9.0.0</RuntimeFrameworkVersion>
</PropertyGroup>
```

- `RollForward`: Çalışma zamanının güncellenme davranışını yapılandırır
- `RuntimeFrameworkVersion`: .NET çalışma zamanı sürümünü belirtir

### Yerleşik Kaynaklar
```xml
<ItemGroup>
    <EmbeddedResource Include="archives\**\*" />
    <EmbeddedResource Include="icons\**\*" />
    <EmbeddedResource Include="translations\**\*" />
</ItemGroup>
```

Bu bölüm, son yürütülebilir dosyada yerleşik olacak kaynakları tanımlar:
- `archives`: Yükleyici için gerekli dosyalar
- `icons`: İkonlar ve görsel kaynaklar
- `translations`: Farklı dillerdeki çeviri dosyaları

### Önemli Notlar

1. Proje, grafiksel kullanıcı arayüzü oluşturmak için uygun olan bir Windows Forms uygulaması olarak yapılandırılmıştır.
2. Uygulama, .NET 9.0'a yönelik olup, framework'ün son özellikleriyle uyumludur.
3. İkonlar, dosyalar ve çeviriler gibi kaynaklar doğrudan yürütülebilir dosyaya yerleştirilmiş ve dağıtımı kolaylaştırılmıştır.
4. Sürüm ve şirket bilgileri, yazılımın kimliğini belirlemek için önemlidir.

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

Hatalar:

![Error 1 Client - SPC](/screenshots/error_1.png)
![Error 2 Client - SPC](/screenshots/error_2.png)

## Lisans

Copyright © **SA-MP Programming Community**

Bu yazılım Apache Lisansı, Sürüm 2.0 ("Lisans") şartları altında lisanslanmıştır; bu yazılımı Lisans ile uyumlu olmayan bir şekilde kullanamazsınız. Lisansın bir kopyasını şu adresten edinebilirsiniz: [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)

### Kullanım Şartları ve Koşulları

#### 1. Verilen İzinler

Bu lisans, bu yazılımın ve ilgili belgelendirme dosyalarının bir kopyasını edinen herhangi bir kişiye ücretsiz olarak aşağıdaki hakları vermektedir:

* Yazılımı herhangi bir ortamda veya formatta, ticari veya ticari olmayan herhangi bir amaçla kullanmak, kopyalamak, değiştirmek ve dağıtmak
* Yazılımın kopyalarını birleştirmek, yayınlamak, dağıtmak, alt lisansını vermek ve/veya satmak
* Yazılımın sağlandığı kişilerin aynısını yapmasına izin vermek

#### 2. Zorunlu Koşullar

Yazılımın veya türetilmiş çalışmaların tüm dağıtımları şunları içermelidir:

* Bu lisansın tam bir kopyası
* Orijinal kaynak kodunda yapılan değişikliklerin açıkça belirtilmesi
* Tüm telif hakkı, patent, ticari marka bildirimleri ve atıfların korunması
* Uygulanan değişikliklerin yeterli dokümantasyonu
* Tüm kopyalarda lisans ve garanti bildiriminin korunması

#### 3. Kısıtlamalar ve Sınırlamalar

* Bu lisans, **SA-MP Programming Community**'nin ticari markalarının, logolarının veya ticari isimlerinin kullanımı için izin vermez
* Kaynak koduna yapılan katkılar bu lisansın aynı şartları altında lisanslanmalıdır
* Katkıda bulunanların isimlerinin bu yazılımdan türetilen ürünleri desteklemek veya tanıtmak için kullanılması özel önceden izin gerektirir

#### 4. Fikri Mülkiyet

Yazılım ve ilgili tüm belgeler telif hakkı yasaları ve uluslararası anlaşmalar tarafından korunmaktadır. **SA-MP Programming Community**, bu lisans tarafından açıkça verilmeyen tüm hakları, unvanları ve çıkarları elinde tutar.

#### 5. Garanti Reddi ve Sorumluluk Sınırlaması

YAZILIM "OLDUĞU GİBİ" SAĞLANIR, TİCARİ ELVERİŞLİLİK, BELİRLİ BİR AMACA UYGUNLUK VE İHLAL ETMEME GARANTİLERİ DAHİL ANCAK BUNLARLA SINIRLI OLMAMAK ÜZERE, AÇIK VEYA ZIMNİ HİÇBİR GARANTİ VERİLMEMEKTEDİR.

HİÇBİR DURUMDA YAZARLAR VEYA TELİF HAKKI SAHİPLERİ, YAZILIMIN KULLANIMI VEYA YAZILIM İLE İLGİLİ DİĞER İŞLEMLERDEN KAYNAKLANAN VEYA BUNLARLA BAĞLANTILI HERHANGİ BİR İDDİA, HASAR VEYA DİĞER YÜKÜMLÜLÜKLERDEN, SÖZLEŞME, HAKSIZ FİİL VEYA BAŞKA BİR ŞEKİLDE SORUMLU TUTULAMAZ.

---

Apache Lisansı 2.0 hakkında detaylı bilgi için: http://www.apache.org/licenses/LICENSE-2.0