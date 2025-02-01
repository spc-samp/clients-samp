# clients-samp

[![Licença](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![C#](https://img.shields.io/badge/C%23-11.0-blue.svg)](https://docs.microsoft.com/en-us/dotnet/csharp/)
[![.NET](https://img.shields.io/badge/.NET-9.0-purple.svg)](https://dotnet.microsoft.com/)
[![Windows Forms](https://img.shields.io/badge/Windows%20Forms-net9.0--windows-blue)](https://docs.microsoft.com/en-us/dotnet/desktop/winforms/)

Este repositorio contiene el código fuente de varios instaladores de Client SA:MP (San Andreas Multiplayer) desarrollados por la SPC (SA-MP Programming Community). Estos instaladores fueron creados para proporcionar alternativas seguras y confiables a los instaladores originales del mod, que ya no se consideran confiables.

## Idiomas

- Português: [README](../../)
- Deutsch: [README](../Deutsch/README.md)
- English: [README](../English/README.md)
- Français: [README](../Francais/README.md)
- Italiano: [README](../Italiano/README.md)
- Polski: [README](../Polski/README.md)
- Русский: [README](../Русский/README.md)
- Svenska: [README](../Svenska/README.md)
- Türkçe: [README](../Turkce/README.md)

## Índice

- [clients-samp](#clients-samp)
  - [Idiomas](#idiomas)
  - [Índice](#índice)
  - [Visión General](#visión-general)
  - [Versiones Disponibles](#versiones-disponibles)
  - [Estructura del Proyecto](#estructura-del-proyecto)
  - [Funcionalidades](#funcionalidades)
  - [Instalación](#instalación)
  - [Compilación](#compilación)
    - [Requisitos previos](#requisitos-previos)
    - [Cómo compilar](#cómo-compilar)
  - [Estructura del Código y Componentes](#estructura-del-código-y-componentes)
    - [Componentes Principales](#componentes-principales)
      - [Cliente Instalador (`InstallerClient.cs`)](#cliente-instalador-installerclientcs)
    - [Servicios](#servicios)
      - [Servicio de Extracción de Archivos (`FileExtraction.cs`)](#servicio-de-extracción-de-archivos-fileextractioncs)
      - [Soporte de Idiomas (`Language.cs`)](#soporte-de-idiomas-languagecs)
      - [Servicio de Mapeo de Idiomas (`LanguageMapping.cs`)](#servicio-de-mapeo-de-idiomas-languagemappingcs)
      - [Servicio de Redes Sociales (`SocialNetworks.cs`)](#servicio-de-redes-sociales-socialnetworkscs)
      - [Componentes de Interfaz Personalizados](#componentes-de-interfaz-personalizados)
        - [Barra de Progreso (`CustomProgressBar.cs`)](#barra-de-progreso-customprogressbarcs)
        - [Colores del Tema (`Colors.cs`)](#colores-del-tema-colorscs)
    - [Recursos de Seguridad](#recursos-de-seguridad)
      - [Privilegios Administrativos](#privilegios-administrativos)
      - [Firma del Ensamblaje](#firma-del-ensamblaje)
    - [Internacionalización](#internacionalización)
      - [Sistema de Traducción](#sistema-de-traducción)
      - [Iconos de Banderas](#iconos-de-banderas)
  - [Configuración del Proyecto (.csproj)](#configuración-del-proyecto-csproj)
    - [Configuraciones Básicas](#configuraciones-básicas)
    - [Información de Versión y Empresa](#información-de-versión-y-empresa)
    - [Configuraciones de Runtime](#configuraciones-de-runtime)
    - [Recursos Incorporados](#recursos-incorporados)
    - [Observaciones Importantes](#observaciones-importantes)
  - [Screenshots](#screenshots)
  - [Licencia](#licencia)
    - [Términos y Condiciones de Uso](#términos-y-condiciones-de-uso)
      - [1. Permisos Concedidos](#1-permisos-concedidos)
      - [2. Condiciones Obligatorias](#2-condiciones-obligatorias)
      - [3. Restricciones y Limitaciones](#3-restricciones-y-limitaciones)
      - [4. Propiedad Intelectual](#4-propiedad-intelectual)
      - [5. Exención de Garantías y Limitación de Responsabilidad](#5-exención-de-garantías-y-limitación-de-responsabilidad)

## Visión General

El proyecto tiene como objetivo proporcionar instaladores seguros y confiables para diferentes versiones del mod SA:MP. Cada instalador está desarrollado en C# utilizando Windows Forms, ofreciendo una interfaz moderna y amigable con soporte para múltiples idiomas y una ventana con las redes sociales.

## Versiones Disponibles

El repositorio incluye las siguientes versiones de Client:

- `samp-client-dl-r1`: Instalador del Client DL R1
- `samp-client-r1`: Instalador del Client R1
- `samp-client-r1-voip`: Client R1 con integración SAMPVOICE
- `samp-client-r2`: Instalador del Client R2
- `samp-client-r3`: Instalador del Client R3
- `samp-client-r3-voip`: Client R3 con integración SAMPVOICE
- `samp-client-r4`: Instalador del Client R4
- `samp-client-r5`: Instalador del Client R5

## Estructura del Proyecto

Cada versión del Client sigue una estructura de proyecto consistente:

```
clients-samp/
└── samp-client-v/
    ├── archives/
    │   └── samp-client-{v}.zip
    ├── icons/
    │   ├── languages/
    │   │   └── [íconos de banderas de los idiomas]
    │   └── social/
    │       └── [íconos de redes sociales]
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
    │   └── [30 archivos XML de idiomas]
    ├── adm.manifest
    ├── compile.bat
    ├── Main.cs
    └── samp-client-{v}.csproj
```

## Funcionalidades

- Soporte para múltiples idiomas (30 idiomas)
- Interfaz de usuario moderna e intuitiva
- Extracción e instalación segura de archivos
- Validación del directorio del juego
- Seguimiento del progreso en tiempo real
- Ventana con redes sociales
- Firma de ensamblado opcional para mayor seguridad
- Barra de progreso personalizada con animaciones
- Esquema de colores y estilo consistentes

## Instalación

1. Accede a la página de [releases](https://github.com/spc-samp/clients-samp/releases) del proyecto
2. Descarga la versión más reciente del Client ya compilada
3. Ejecuta y continúa con los procedimientos

## Compilación

### Requisitos previos

- SDK .NET 9.0 o superior
- Sistema operativo Windows
- Visual Studio 2022 o superior (opcional)
- Visual Studio Code (opcional)

### Cómo compilar

La forma más fácil de compilar cualquier versión del Client es utilizando el archivo batch proporcionado:

1. Abre una terminal en el directorio de la versión del Client
2. Ejecuta el comando de compilación:
```bash
.\compile
```

También puedes compilar directamente utilizando la CLI de .NET:
```bash
dotnet publish -c Release -r win-x64 --self-contained true -p:PublishSingleFile=true -p:EnableCompressionInSingleFile=true -o ./published
```

> [!NOTE]
> Este comando generará un archivo ejecutable único y optimizado para Windows 64-bit, que contendrá todas las dependencias necesarias. El ejecutable se creará dentro de la carpeta `published` en el directorio del proyecto.

## Estructura del Código y Componentes

### Componentes Principales

#### Cliente Instalador (`InstallerClient.cs`)

El formulario principal que gestiona todo el proceso de instalación. Implementa una interfaz de asistente paso a paso:

```csharp
public partial class Installer_Client : Form
{
    // Módulos principales
    private File_Extraction Extraction_Module;
    private Language Language_Module;
    private Language_Mapping LanguageMapping_Module;
    private Social_Networks SocialNetworks_Module;

    // Elementos de la interfaz
    private Label Description_Label, Status_Label;
    private Custom_ProgressBar Progress_Bar;
    private ListBox ExtractedFiles_List;
}
```

Principales características y responsabilidades:

1. **Selección de Idioma**
   ```csharp
   private void CreateLanguage_Buttons()
   {
       // Crea una cuadrícula de botones de idioma con banderas
       Panel Button_Panel = new Panel
       {
           AutoScroll = true,
           Dock = DockStyle.None,
           Location = new Point(0, 140),
           Width = this.ClientSize.Width,
           Height = this.ClientSize.Height - 140
       };
       
       // Creación dinámica de botones con banderas
       for (int i = 0; i < Available_Languages.Count; i++)
       {
           var Language = Available_Languages[i];
           var Language_Button = CreateLanguage_Button(Language, Icon_Size, Button_Width, Button_Height, i, MaxButtons_PerRow, Padding);
           Button_Panel.Controls.Add(Language_Button);
       }
   }
   ```

2. **Selección del Directorio de Instalación**
   ```csharp
   private void Selecting_Folder()
   {
       // Diálogo de selección de carpeta con validación
       using var Dialog = new FolderBrowserDialog();
       if (Dialog.ShowDialog() == DialogResult.OK)
       {
           Selected_Path = Dialog.SelectedPath;
           // Valida el directorio de instalación de GTA:SA
           if (Path.GetFileName(Selected_Path) != "Grand Theft Auto San Andreas")
           {
               Status_Label.Text = Translate("invalid_folder");
               Status_Label.ForeColor = Color.Red;
           }
       }
   }
   ```

3. **Proceso de Extracción de Archivos**
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

4. **Ventana con las Redes Sociales**
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

       // Crea botones para cada red social con íconos
       for (int i = 0; i < Social_Networks.Length; i++)
       {
           var Social_Button = CreateSocial_NetworkButton(Social_Networks[i], Icon_Size, Button_Width, Button_Height, i, Padding);
           Controls.Add(Social_Button);
       }
   }
   ```

### Servicios

#### Servicio de Extracción de Archivos (`FileExtraction.cs`)

Gestiona la extracción segura de los archivos del Cliente SA:MP de los recursos integrados:

```csharp
public class File_Extraction
{
    public async Task<List<string>> ExtractClient_Files(string Target_Path, IProgress<(int progress, string fileName)> progress)
    {
        // Carga el recurso ZIP integrado
        var Current_Assembly = Assembly.GetExecutingAssembly();
        var Zip_Resource = Current_Assembly.GetManifestResourceNames().FirstOrDefault(Res => Res.Contains("archives") && Res.EndsWith("samp-client-v.zip"));

        using var Zip_Archive = new ZipArchive(Temp_Buffer, ZipArchiveMode.Read);
        var Total_Files = Zip_Archive.Entries.Count;
        var Processed_Files = new List<string>();

        // Extrae archivos con reporte de progreso
        for (int File_Index = 0; File_Index < Total_Files; File_Index++)
        {
            var Current_Entry = Zip_Archive.Entries[File_Index];
            var File_Target_Path = Path.Combine(Target_Path, Current_Entry.FullName);

            // Informa el progreso para actualizaciones de la interfaz
            int Completion_Percent = (int)((File_Index + 1) * 100.0 / Total_Files);
            progress.Report((Completion_Percent, Current_Entry.FullName));
        }

        return Processed_Files;
    }
}
```

#### Soporte de Idiomas (`Language.cs`)

Gestiona el sistema de soporte a múltiples idiomas utilizando recursos XML:

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
        // Carga y analiza el archivo XML de traducción
        using var Resource_Stream = Current_Assembly.GetManifestResourceStream(Resource_Name);
        var XML_Document = XDocument.Load(Resource_Stream);

        Translation_Dictionary = XML_Document.Descendants("string").ToDictionary(Element => Element.Attribute("key")?.Value ?? string.Empty, Element => Element.Value);
    }
}
```

#### Servicio de Mapeo de Idiomas (`LanguageMapping.cs`)

Gestiona el mapeo entre nombres de idiomas y sus códigos de imagen de bandera correspondientes:

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
            // Mapeos adicionales de idiomas...
        };
    }

    public string GetImage_Code(string Language_Name) =>
        LanguageTo_ImageCode.TryGetValue(Path.GetFileNameWithoutExtension(Language_Name), out var Code) ? Code : Language_Name.ToLower();
}
```

#### Servicio de Redes Sociales (`SocialNetworks.cs`)

Gestiona la apertura de enlaces de redes sociales en el navegador predeterminado:

```csharp
public class Social_Networks
{
    public void OpenSocial_Network(string Network_Name)
    {
        string Network_Url = Network_Name switch
        {
            "Discord SPC" => "https://discord.gg/3fApZh66Tf",
            "YouTube" => "https://youtube.com/@spc-samp",
            // Mapeos adicionales de redes...
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

#### Componentes de Interfaz Personalizados

##### Barra de Progreso (`CustomProgressBar.cs`)

Una barra de progreso altamente personalizada con animaciones y estilo moderno:

```csharp
public class Custom_ProgressBar : ProgressBar
{
    // Propiedades de personalización
    public Color GradientStart_Color { get; set; }
    public Color GradientEnd_Color { get; set; }
    public int Animation_Speed { get; set; }
    public int Corner_Radius { get; set; }
    public bool Show_Percentage { get; set; }

    protected override void OnPaint(PaintEventArgs e)
    {
        // Implementa dibujo personalizado con gradientes y animaciones
        using (var Path = GetRounded_Rectangle(Progress_Rect, Corner_Radius_II))
        using (var Gradient = new LinearGradientBrush(Progress_Rect, GradientStart_Color_II, GradientEnd_Color_II, LinearGradientMode.Horizontal))
        {
            // Aplica mezcla de colores para transiciones suaves
            ColorBlend Blend = new ColorBlend();
            Blend.Positions = Positions;
            Blend.Colors = Colors;
            Gradient.InterpolationColors = Blend;

            // Aplica animación de rotación
            Matrix Matrix = new Matrix();
            Matrix.RotateAt(Animation_Step, new PointF(Progress_Rect.Left + Progress_Rect.Width / 2, Progress_Rect.Top + Progress_Rect.Height / 2));
            Gradient.MultiplyTransform(Matrix);

            e.Graphics.FillPath(Gradient, Path);
        }
    }
}
```

##### Colores del Tema (`Colors.cs`)

Define el esquema de colores de la aplicación:

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

### Recursos de Seguridad

#### Privilegios Administrativos

El instalador requiere privilegios administrativos para instalar correctamente los archivos de SA:MP en el directorio de GTA:SA. Esto se gestiona a través del archivo `adm.manifest`:

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

Principales características de la ejecución administrativa:
- Garantiza permisos adecuados de archivo para la instalación
- Permite la modificación de directorios protegidos del sistema
- Gestiona automáticamente los avisos de UAC (Control de Cuenta de Usuario)
- Necesario para modificaciones en el registro, si es necesario

Para habilitar la ejecución administrativa, se referencia el archivo de manifiesto en el archivo del proyecto:

```xml
<PropertyGroup>
    <ApplicationManifest>adm.manifest</ApplicationManifest>
</PropertyGroup>
```

#### Firma del Ensamblaje

El proyecto soporta la firma de nombre fuerte para una mayor seguridad. Esto se puede habilitar en el archivo del proyecto:

```xml
<PropertyGroup>
    <SignAssembly>true</SignAssembly>
    <AssemblyOriginatorKeyFile>MyKey.snk</AssemblyOriginatorKeyFile>
</PropertyGroup>
```

Para generar una clave de nombre fuerte:

```bash
sn -k MyKey.snk
```

Beneficios de la firma del ensamblaje:
- Garantiza la integridad del ensamblaje
- Previene la adulteración del ensamblaje
- Proporciona una identidad única al ensamblaje
- Permite la implementación en el GAC
- Soporta la implementación ClickOnce

> [!NOTE]
> Mantenga su archivo de clave de nombre fuerte (*.snk) seguro y nunca lo envíe al control de versiones.

### Internacionalización

#### Sistema de Traducción

Las traducciones se almacenan en archivos XML con la siguiente estructura:

```xml
<translations>
  <string key="continue">Continuar</string>
  <string key="cancel">Cancelar</string>
  <string key="finish">Finalizar</string>
  <string key="close">Cerrar</string>
  <!-- Traducciones adicionales -->
</translations>
```

La clase `Language` carga estas traducciones de manera dinámica:

```csharp
public string Translate(string Key) => 
    Translation_Dictionary.TryGetValue(Key, out var Value) ? Value : Key;
```

#### Iconos de Banderas

Las banderas de los idiomas se almacenan como recursos integrados y se cargan dinámicamente:

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

## Configuración del Proyecto (.csproj)

El archivo `.csproj` es un componente crucial del proyecto, que define las configuraciones y propiedades fundamentales de la aplicación. A continuación se muestra la estructura detallada de las principales configuraciones utilizadas:

### Configuraciones Básicas
```xml
<PropertyGroup>
    <OutputType>WinExe</OutputType>
    <TargetFramework>net9.0-windows</TargetFramework>
    <UseWindowsForms>true</UseWindowsForms>
    <ApplicationManifest>adm.manifest</ApplicationManifest>
    <ApplicationIcon>icons\social\ico-spc.ico</ApplicationIcon>
</PropertyGroup>
```

- `OutputType`: Define el tipo de salida como un ejecutable de Windows
- `TargetFramework`: Especifica la versión del .NET Framework utilizada (9.0)
- `UseWindowsForms`: Habilita el uso de Windows Forms para la interfaz gráfica
- `ApplicationManifest`: Define el manifiesto de la aplicación para permisos administrativos
- `ApplicationIcon`: Define el icono principal de la aplicación

### Información de Versión y Empresa
```xml
<PropertyGroup>
    <AssemblyVersion>1.0.0.0</AssemblyVersion>
    <FileVersion>1.0.0.0</FileVersion>
    <Company>SA-MP Programming Community</Company>
    <Product>samp-client-rvv1</Product>
    <Copyright>Copyright © SPC</Copyright>
    <Description>Instalador del mod (San Andreas Multiplayer) versión 0.3.7 V.</Description>
</PropertyGroup>
```

- `AssemblyVersion`: Versión del ensamblaje del proyecto
- `FileVersion`: Versión del archivo ejecutable
- `Company`: Nombre de la empresa/organización
- `Product`: Nombre del producto
- `Copyright`: Información de derechos de autor
- `Description`: Descripción del proyecto

### Configuraciones de Runtime
```xml
<PropertyGroup>
    <RollForward>LatestMajor</RollForward>
    <RuntimeFrameworkVersion>9.0.0</RuntimeFrameworkVersion>
</PropertyGroup>
```

- `RollForward`: Configura el comportamiento de actualización del runtime
- `RuntimeFrameworkVersion`: Especifica la versión exacta del runtime de .NET

### Recursos Incorporados
```xml
<ItemGroup>
    <EmbeddedResource Include="archives\**\*" />
    <EmbeddedResource Include="icons\**\*" />
    <EmbeddedResource Include="translations\**\*" />
</ItemGroup>
```

Esta sección define los recursos que se incorporarán en el ejecutable final:
- `archives`: Archivos necesarios para el instalador
- `icons`: Iconos y recursos visuales
- `translations`: Archivos de traducción para diferentes idiomas

### Observaciones Importantes

1. El proyecto está configurado como un ejecutable de Windows Forms, adecuado para crear una interfaz gráfica de usuario.
2. La aplicación está orientada a .NET 9.0, garantizando compatibilidad con las últimas funcionalidades del framework.
3. Recursos como iconos, archivos y traducciones están incorporados directamente en el ejecutable, facilitando la distribución.
4. Las configuraciones de versión e información de la empresa son importantes para la identificación del software.

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

Errores:

![Error 1 Client - SPC](/screenshots/error_1.png)
![Error 2 Client - SPC](/screenshots/error_2.png)

## Licencia

Copyright © **SA-MP Programming Community**

Este software está licenciado bajo los términos de la Licencia Apache, Versión 2.0 ("Licencia"); no puede utilizar este software excepto en conformidad con la Licencia. Puede obtener una copia de la Licencia en: [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)

### Términos y Condiciones de Uso

#### 1. Permisos Concedidos

La presente licencia otorga, de forma gratuita, a cualquier persona que obtenga una copia de este software y archivos de documentación asociados, los siguientes derechos:

* Utilizar, copiar, modificar y distribuir el software en cualquier medio o formato, para cualquier finalidad, comercial o no comercial
* Fusionar, publicar, distribuir, sublicenciar y/o vender copias del software
* Permitir que las personas a quienes se les proporciona el software hagan lo mismo

#### 2. Condiciones Obligatorias

Todas las distribuciones del software o trabajos derivados deben:

* Incluir una copia completa de esta licencia
* Indicar claramente cualquier modificación realizada en el código fuente original
* Preservar todos los avisos de derechos de autor, patentes, marcas registradas y atribuciones
* Proporcionar documentación adecuada de los cambios implementados
* Mantener el aviso de licencia y garantía en todas las copias

#### 3. Restricciones y Limitaciones

* Esta licencia no otorga permiso para usar marcas registradas, logotipos o nombres comerciales de la **SA-MP Programming Community**
* Las contribuciones al código fuente deben ser licenciadas bajo los mismos términos de esta licencia
* El uso de nombres de los contribuyentes para respaldar o promover productos derivados de este software requiere permiso previo específico

#### 4. Propiedad Intelectual

El software y toda la documentación asociada están protegidos por leyes de derechos de autor y tratados internacionales. La **SA-MP Programming Community** retiene todos los derechos, títulos e intereses no expresamente otorgados por esta licencia.

#### 5. Exención de Garantías y Limitación de Responsabilidad

EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍAS DE NINGÚN TIPO, EXPRESAS O IMPLÍCITAS, INCLUYENDO, PERO NO LIMITÁNDOSE A, GARANTÍAS DE COMERCIABILIDAD, IDONEIDAD PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN.

EN NINGÚN CASO LOS AUTORES O TITULARES DE LOS DERECHOS DE AUTOR SERÁN RESPONSABLES POR CUALQUIER RECLAMACIÓN, DAÑOS U OTRAS RESPONSABILIDADES, YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O DE OTRO TIPO, QUE SURJA DE, O EN CONEXIÓN CON EL SOFTWARE O EL USO U OTROS TRATOS EN EL SOFTWARE.

---

Para información detallada sobre la Licencia Apache 2.0, consulte: http://www.apache.org/licenses/LICENSE-2.0