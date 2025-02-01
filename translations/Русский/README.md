# clients-samp

[![Licença](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![C#](https://img.shields.io/badge/C%23-11.0-blue.svg)](https://docs.microsoft.com/en-us/dotnet/csharp/)
[![.NET](https://img.shields.io/badge/.NET-9.0-purple.svg)](https://dotnet.microsoft.com/)
[![Windows Forms](https://img.shields.io/badge/Windows%20Forms-net9.0--windows-blue)](https://docs.microsoft.com/en-us/dotnet/desktop/winforms/)

Этот репозиторий содержит исходный код нескольких установщиков клиента SA:MP (San Andreas Multiplayer), разработанных SPC (SA-MP Programming Community). Эти установщики были созданы для обеспечения безопасных и надежных альтернатив оригинальным установщикам мода, которые больше не считаются надежными.

## Языки

- Português: [README](../../)
- Deutsch: [README](../Deutsch/README.md)
- English: [README](../English/README.md)
- Español: [README](../Espanol/README.md)
- Français: [README](../Francais/README.md)
- Italiano: [README](../Italiano/README.md)
- Polski: [README](../Polski/README.md)
- Svenska: [README](../Svenska/README.md)
- Türkçe: [README](../Turkce/README.md)

## Индекс

- [clients-samp](#clients-samp)
  - [Языки](#языки)
  - [Индекс](#индекс)
  - [Обзор](#обзор)
  - [Доступные версии](#доступные-версии)
  - [Структура проекта](#структура-проекта)
  - [Функции](#функции)
  - [Установка](#установка)
  - [Сборка](#сборка)
    - [Требования](#требования)
    - [Как скомпилировать](#как-скомпилировать)
  - [Структура кода и компоненты](#структура-кода-и-компоненты)
    - [Основные компоненты](#основные-компоненты)
      - [Установщик клиента (`InstallerClient.cs`)](#установщик-клиента-installerclientcs)
    - [Сервисы](#сервисы)
      - [Сервис извлечения файлов (`FileExtraction.cs`)](#сервис-извлечения-файлов-fileextractioncs)
      - [Поддержка языков (`Language.cs`)](#поддержка-языков-languagecs)
      - [Сервис сопоставления языков (`LanguageMapping.cs`)](#сервис-сопоставления-языков-languagemappingcs)
      - [Сервис социальных сетей (`SocialNetworks.cs`)](#сервис-социальных-сетей-socialnetworkscs)
      - [Компоненты пользовательского интерфейса](#компоненты-пользовательского-интерфейса)
        - [Индивидуальная полоса прогресса (`CustomProgressBar.cs`)](#индивидуальная-полоса-прогресса-customprogressbarcs)
        - [Цвета темы (`Colors.cs`)](#цвета-темы-colorscs)
    - [Ресурсы безопасности](#ресурсы-безопасности)
      - [Административные привилегии](#административные-привилегии)
      - [Подпись сборки](#подпись-сборки)
    - [Интернационализация](#интернационализация)
      - [Система перевода](#система-перевода)
      - [Иконки флагов](#иконки-флагов)
  - [Конфигурация проекта (.csproj)](#конфигурация-проекта-csproj)
    - [Основные настройки](#основные-настройки)
    - [Информация о версии и компании](#информация-о-версии-и-компании)
    - [Настройки времени выполнения](#настройки-времени-выполнения)
    - [Встроенные ресурсы](#встроенные-ресурсы)
    - [Важные замечания](#важные-замечания)
  - [Screenshots](#screenshots)
  - [Лицензия](#лицензия)
    - [Условия использования](#условия-использования)
      - [1. Предоставляемые разрешения](#1-предоставляемые-разрешения)
      - [2. Обязательные условия](#2-обязательные-условия)
      - [3. Ограничения](#3-ограничения)
      - [4. Интеллектуальная собственность](#4-интеллектуальная-собственность)
      - [5. Отказ от гарантий и ограничение ответственности](#5-отказ-от-гарантий-и-ограничение-ответственности)

## Обзор

Проект направлен на предоставление безопасных и надежных установщиков для различных версий мода SA:MP. Каждый установщик разработан на C# с использованием Windows Forms, предлагая современный и удобный интерфейс с поддержкой нескольких языков и окном с социальными сетями.

## Доступные версии

Репозиторий включает следующие версии клиента:

- `samp-client-dl-r1`: Установщик клиента DL R1
- `samp-client-r1`: Установщик клиента R1
- `samp-client-r1-voip`: Клиент R1 с интеграцией SAMPVOICE
- `samp-client-r2`: Установщик клиента R2
- `samp-client-r3`: Установщик клиента R3
- `samp-client-r3-voip`: Клиент R3 с интеграцией SAMPVOICE
- `samp-client-r4`: Установщик клиента R4
- `samp-client-r5`: Установщик клиента R5

## Структура проекта

Каждая версия клиента следует последовательной структуре проекта:

```
clients-samp/
└── samp-client-v/
    ├── archives/
    │   └── samp-client-{v}.zip
    ├── icons/
    │   ├── languages/
    │   │   └── [иконки флагов языков]
    │   └── social/
    │       └── [иконки социальных сетей]
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
    │   └── [30 XML файлов языков]
    ├── adm.manifest
    ├── compile.bat
    ├── Main.cs
    └── samp-client-{v}.csproj
```

## Функции

- Поддержка нескольких языков (30 языков)
- Современный и интуитивно понятный интерфейс
- Безопасная извлечения и установка файлов
- Проверка директории игры
- Отслеживание прогресса в реальном времени
- Окно с социальными сетями
- Опциональная подпись сборки для повышения безопасности
- Пользовательская панель прогресса с анимацией
- Согласованная цветовая схема и стиль

## Установка

1. Перейдите на страницу [releases](https://github.com/spc-samp/clients-samp/releases) проекта
2. Скачайте последнюю компилированную версию клиента
3. Запустите и следуйте инструкциям

## Сборка

### Требования

- SDK .NET 9.0 или выше
- Операционная система Windows
- Visual Studio 2022 или выше (по желанию)
- Visual Studio Code (по желанию)

### Как скомпилировать

Самый простой способ собрать любую версию клиента — использовать предоставленный батч-файл:

1. Откройте терминал в директории версии клиента
2. Выполните команду для сборки:
```bash
.\compile
```

Вы также можете скомпилировать напрямую с использованием CLI .NET:
```bash
dotnet publish -c Release -r win-x64 --self-contained true -p:PublishSingleFile=true -p:EnableCompressionInSingleFile=true -o ./published
```

> [!NOTE]
> Эта команда создаст единственный исполнимый файл, оптимизированный для Windows 64-bit, содержащий все необходимые зависимости. Исполнимый файл будет создан в папке `published` в директории проекта.

## Структура кода и компоненты

### Основные компоненты

#### Установщик клиента (`InstallerClient.cs`)

Основная форма, которая управляет всем процессом установки. Реализует интерфейс пошагового помощника:

```csharp
public partial class Installer_Client : Form
{
    // Основные модули
    private File_Extraction Extraction_Module;
    private Language Language_Module;
    private Language_Mapping LanguageMapping_Module;
    private Social_Networks SocialNetworks_Module;

    // Элементы интерфейса
    private Label Description_Label, Status_Label;
    private Custom_ProgressBar Progress_Bar;
    private ListBox ExtractedFiles_List;
}
```

Основные функции и обязанности:

1. **Выбор языка**
   ```csharp
   private void CreateLanguage_Buttons()
   {
       // Создает сетку кнопок для выбора языка с флагами
       Panel Button_Panel = new Panel
       {
           AutoScroll = true,
           Dock = DockStyle.None,
           Location = new Point(0, 140),
           Width = this.ClientSize.Width,
           Height = this.ClientSize.Height - 140
       };
       
       // Динамическое создание кнопок с флагами
       for (int i = 0; i < Available_Languages.Count; i++)
       {
           var Language = Available_Languages[i];
           var Language_Button = CreateLanguage_Button(Language, Icon_Size, Button_Width, Button_Height, i, MaxButtons_PerRow, Padding);
           Button_Panel.Controls.Add(Language_Button);
       }
   }
   ```

2. **Выбор каталога установки**
   ```csharp
   private void Selecting_Folder()
   {
       // Диалог выбора папки с валидацией
       using var Dialog = new FolderBrowserDialog();
       if (Dialog.ShowDialog() == DialogResult.OK)
       {
           Selected_Path = Dialog.SelectedPath;
           // Проверка каталога установки GTA:SA
           if (Path.GetFileName(Selected_Path) != "Grand Theft Auto San Andreas")
           {
               Status_Label.Text = Translate("invalid_folder");
               Status_Label.ForeColor = Color.Red;
           }
       }
   }
   ```

3. **Процесс извлечения файлов**
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

4. **Окно с социальными сетями**
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

       // Создание кнопок для каждой социальной сети с иконками
       for (int i = 0; i < Social_Networks.Length; i++)
       {
           var Social_Button = CreateSocial_NetworkButton(Social_Networks[i], Icon_Size, Button_Width, Button_Height, i, Padding);
           Controls.Add(Social_Button);
       }
   }
   ```

### Сервисы

#### Сервис извлечения файлов (`FileExtraction.cs`)

Управляет безопасным извлечением файлов клиента SA:MP из встроенных ресурсов:

```csharp
public class File_Extraction
{
    public async Task<List<string>> ExtractClient_Files(string Target_Path, IProgress<(int progress, string fileName)> progress)
    {
        // Загружает встроенный ZIP-ресурс
        var Current_Assembly = Assembly.GetExecutingAssembly();
        var Zip_Resource = Current_Assembly.GetManifestResourceNames().FirstOrDefault(Res => Res.Contains("archives") && Res.EndsWith("samp-client-v.zip"));

        using var Zip_Archive = new ZipArchive(Temp_Buffer, ZipArchiveMode.Read);
        var Total_Files = Zip_Archive.Entries.Count;
        var Processed_Files = new List<string>();

        // Извлекает файлы с отчетом о прогрессе
        for (int File_Index = 0; File_Index < Total_Files; File_Index++)
        {
            var Current_Entry = Zip_Archive.Entries[File_Index];
            var File_Target_Path = Path.Combine(Target_Path, Current_Entry.FullName);

            // Отчитывает прогресс для обновлений интерфейса
            int Completion_Percent = (int)((File_Index + 1) * 100.0 / Total_Files);
            progress.Report((Completion_Percent, Current_Entry.FullName));
        }

        return Processed_Files;
    }
}
```

#### Поддержка языков (`Language.cs`)

Управляет системой поддержки нескольких языков с использованием XML-ресурсов:

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
        // Загружает и анализирует XML-файл перевода
        using var Resource_Stream = Current_Assembly.GetManifestResourceStream(Resource_Name);
        var XML_Document = XDocument.Load(Resource_Stream);

        Translation_Dictionary = XML_Document.Descendants("string").ToDictionary(Element => Element.Attribute("key")?.Value ?? string.Empty, Element => Element.Value);
    }
}
```

#### Сервис сопоставления языков (`LanguageMapping.cs`)

Управляет сопоставлением между названиями языков и их соответствующими кодами изображений флагов:

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
            // Дополнительные сопоставления языков...
        };
    }

    public string GetImage_Code(string Language_Name) =>
        LanguageTo_ImageCode.TryGetValue(Path.GetFileNameWithoutExtension(Language_Name), out var Code) ? Code : Language_Name.ToLower();
}
```

#### Сервис социальных сетей (`SocialNetworks.cs`)

Управляет открытием ссылок на социальные сети в стандартном браузере:

```csharp
public class Social_Networks
{
    public void OpenSocial_Network(string Network_Name)
    {
        string Network_Url = Network_Name switch
        {
            "Discord SPC" => "https://discord.gg/3fApZh66Tf",
            "YouTube" => "https://youtube.com/@spc-samp",
            // Дополнительные сопоставления сетей...
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

#### Компоненты пользовательского интерфейса

##### Индивидуальная полоса прогресса (`CustomProgressBar.cs`)

Высококастомизированная полоса прогресса с анимацией и современным стилем:

```csharp
public class Custom_ProgressBar : ProgressBar
{
    // Свойства кастомизации
    public Color GradientStart_Color { get; set; }
    public Color GradientEnd_Color { get; set; }
    public int Animation_Speed { get; set; }
    public int Corner_Radius { get; set; }
    public bool Show_Percentage { get; set; }

    protected override void OnPaint(PaintEventArgs e)
    {
        // Реализует рисование с градиентами и анимациями
        using (var Path = GetRounded_Rectangle(Progress_Rect, Corner_Radius_II))
        using (var Gradient = new LinearGradientBrush(Progress_Rect, GradientStart_Color_II, GradientEnd_Color_II, LinearGradientMode.Horizontal))
        {
            // Применяет смешивание цветов для плавных переходов
            ColorBlend Blend = new ColorBlend();
            Blend.Positions = Positions;
            Blend.Colors = Colors;
            Gradient.InterpolationColors = Blend;

            // Применяет анимацию вращения
            Matrix Matrix = new Matrix();
            Matrix.RotateAt(Animation_Step, new PointF(Progress_Rect.Left + Progress_Rect.Width / 2, Progress_Rect.Top + Progress_Rect.Height / 2));
            Gradient.MultiplyTransform(Matrix);

            e.Graphics.FillPath(Gradient, Path);
        }
    }
}
```

##### Цвета темы (`Colors.cs`)

Определяет цветовую схему приложения:

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

### Ресурсы безопасности

#### Административные привилегии

Установщик требует административных привилегий для правильной установки файлов SA:MP в директорию GTA:SA. Это управляется через файл `adm.manifest`:

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

Основные функции административного выполнения:
- Обеспечивает надлежащие разрешения для установки файлов
- Позволяет изменять защищенные системные директории
- Автоматически управляет запросами UAC (Контроль учетных записей пользователей)
- Требуется для изменений в реестре, если это необходимо

Для включения административного выполнения файл манифеста ссылается на файл проекта:

```xml
<PropertyGroup>
    <ApplicationManifest>adm.manifest</ApplicationManifest>
</PropertyGroup>
```

#### Подпись сборки

Проект поддерживает подпись с сильным именем для улучшенной безопасности. Это можно включить в файле проекта:

```xml
<PropertyGroup>
    <SignAssembly>true</SignAssembly>
    <AssemblyOriginatorKeyFile>MyKey.snk</AssemblyOriginatorKeyFile>
</PropertyGroup>
```

Для генерации ключа с сильным именем:

```bash
sn -k MyKey.snk
```

Преимущества подписи сборки:
- Обеспечивает целостность сборки
- Предотвращает подделку сборки
- Обеспечивает уникальную идентичность сборки
- Разрешает развертывание в GAC
- Поддерживает развертывание ClickOnce

> [!NOTE]
> Храните свой файл ключа с сильным именем (*.snk) в безопасности и никогда не передавайте его в систему контроля версий.

### Интернационализация

#### Система перевода

Переводы хранятся в XML-файлах со следующей структурой:

```xml
<translations>
  <string key="continue">Продолжить</string>
  <string key="cancel">Отменить</string>
  <string key="finish">Завершить</string>
  <string key="close">Закрыть</string>
  <!-- Дополнительные переводы -->
</strings>
```

Класс `Language` динамически загружает эти переводы:

```csharp
public string Translate(string Key) => 
    Translation_Dictionary.TryGetValue(Key, out var Value) ? Value : Key;
```

#### Иконки флагов

Флаги языков хранятся как встроенные ресурсы и загружаются динамически:

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

## Конфигурация проекта (.csproj)

Файл `.csproj` является важной частью проекта, определяющей основные настройки и свойства приложения. Ниже представлена детальная структура основных конфигураций, используемых в проекте:

### Основные настройки
```xml
<PropertyGroup>
    <OutputType>WinExe</OutputType>
    <TargetFramework>net9.0-windows</TargetFramework>
    <UseWindowsForms>true</UseWindowsForms>
    <ApplicationManifest>adm.manifest</ApplicationManifest>
    <ApplicationIcon>icons\social\ico-spc.ico</ApplicationIcon>
</PropertyGroup>
```

- `OutputType`: Определяет тип выходного файла как исполняемый файл для Windows
- `TargetFramework`: Указывает версию .NET Framework (9.0)
- `UseWindowsForms`: Включает использование Windows Forms для графического интерфейса
- `ApplicationManifest`: Указывает манифест приложения для административных привилегий
- `ApplicationIcon`: Указывает главный значок приложения

### Информация о версии и компании
```xml
<PropertyGroup>
    <AssemblyVersion>1.0.0.0</AssemblyVersion>
    <FileVersion>1.0.0.0</FileVersion>
    <Company>SA-MP Programming Community</Company>
    <Product>samp-client-v</Product>
    <Copyright>Copyright © SPC</Copyright>
    <Description>Установщик мода (San Andreas Multiplayer) версия 0.3.7 V.</Description>
</PropertyGroup>
```

- `AssemblyVersion`: Версия сборки проекта
- `FileVersion`: Версия исполняемого файла
- `Company`: Название компании/организации
- `Product`: Название продукта
- `Copyright`: Информация о праве собственности
- `Description`: Описание проекта

### Настройки времени выполнения
```xml
<PropertyGroup>
    <RollForward>LatestMajor</RollForward>
    <RuntimeFrameworkVersion>9.0.0</RuntimeFrameworkVersion>
</PropertyGroup>
```

- `RollForward`: Настроить поведение обновлений для времени выполнения
- `RuntimeFrameworkVersion`: Указывает точную версию времени выполнения .NET

### Встроенные ресурсы
```xml
<ItemGroup>
    <EmbeddedResource Include="archives\**\*" />
    <EmbeddedResource Include="icons\**\*" />
    <EmbeddedResource Include="translations\**\*" />
</ItemGroup>
```

Этот раздел определяет ресурсы, которые будут встроены в конечный исполняемый файл:
- `archives`: Файлы, необходимые для установщика
- `icons`: Иконки и визуальные ресурсы
- `translations`: Файлы перевода для различных языков

### Важные замечания

1. Проект настроен как исполняемый файл Windows Forms, подходящий для создания графического пользовательского интерфейса.
2. Приложение ориентировано на .NET 9.0, обеспечивая совместимость с последними функциями фреймворка.
3. Ресурсы, такие как иконки, файлы и переводы, встроены непосредственно в исполняемый файл, что упрощает распространение.
4. Настройки версии и информация о компании важны для идентификации программного обеспечения.

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

Ошибки:

![Error 1 Client - SPC](/screenshots/error_1.png)
![Error 2 Client - SPC](/screenshots/error_2.png)

## Лицензия

Copyright © **SA-MP Programming Community**

Данное программное обеспечение лицензируется в соответствии с условиями Apache License, Version 2.0 ("Лицензия"); вы не можете использовать это программное обеспечение, кроме как в соответствии с Лицензией. Копию Лицензии можно получить по адресу: [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)

### Условия использования

#### 1. Предоставляемые разрешения

Настоящая лицензия бесплатно предоставляет любому лицу, получающему копию данного программного обеспечения и связанных с ним файлов документации, следующие права:
* Использовать, копировать, изменять и распространять программное обеспечение на любом носителе или в любом формате, в любых целях, коммерческих или некоммерческих
* Объединять, публиковать, распространять, сублицензировать и/или продавать копии программного обеспечения
* Разрешать лицам, которым предоставляется программное обеспечение, делать то же самое

#### 2. Обязательные условия

Все распространения программного обеспечения или производных работ должны:
* Включать полную копию данной лицензии
* Четко указывать любые изменения, внесенные в исходный код
* Сохранять все уведомления об авторских правах, патентах, товарных знаках и атрибуции
* Предоставлять надлежащую документацию о внесенных изменениях
* Сохранять уведомление о лицензии и гарантии во всех копиях

#### 3. Ограничения

* Данная лицензия не предоставляет разрешения на использование товарных знаков, логотипов или торговых наименований **SA-MP Programming Community**
* Вклады в исходный код должны лицензироваться на тех же условиях, что и данная лицензия
* Использование имен участников для поддержки или продвижения производных продуктов требует предварительного специального разрешения

#### 4. Интеллектуальная собственность

Программное обеспечение и вся связанная документация защищены законами об авторских правах и международными договорами. **SA-MP Programming Community** сохраняет за собой все права, правовые титулы и интересы, прямо не предоставленные настоящей лицензией.

#### 5. Отказ от гарантий и ограничение ответственности

ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ ПРЕДОСТАВЛЯЕТСЯ "КАК ЕСТЬ", БЕЗ КАКИХ-ЛИБО ГАРАНТИЙ, ЯВНЫХ ИЛИ ПОДРАЗУМЕВАЕМЫХ, ВКЛЮЧАЯ, НО НЕ ОГРАНИЧИВАЯСЬ, ГАРАНТИИ КОММЕРЧЕСКОЙ ЦЕННОСТИ, ПРИГОДНОСТИ ДЛЯ КОНКРЕТНОЙ ЦЕЛИ И НЕНАРУШЕНИЯ ПРАВ.

НИ ПРИ КАКИХ ОБСТОЯТЕЛЬСТВАХ АВТОРЫ ИЛИ ПРАВООБЛАДАТЕЛИ НЕ НЕСУТ ОТВЕТСТВЕННОСТИ ЗА ЛЮБЫЕ ПРЕТЕНЗИИ, УБЫТКИ ИЛИ ИНУЮ ОТВЕТСТВЕННОСТЬ, БУДЬ ТО В СИЛУ ДОГОВОРА, ДЕЛИКТА ИЛИ ИНЫМ ОБРАЗОМ, ВОЗНИКАЮЩИЕ ИЗ, ИЛИ В СВЯЗИ С ПРОГРАММНЫМ ОБЕСПЕЧЕНИЕМ ИЛИ ИСПОЛЬЗОВАНИЕМ ИЛИ ИНЫМИ ДЕЙСТВИЯМИ С ПРОГРАММНЫМ ОБЕСПЕЧЕНИЕМ.

---

Для подробной информации об Apache License 2.0, посетите: http://www.apache.org/licenses/LICENSE-2.0