# clients-samp

## 🌍

- **Português** > [README](https://github.com/spc-samp/clients-samp).
- **English** > [README](https://github.com/spc-samp/clients-samp/tree/English).
- **Polski** > [README](https://github.com/spc-samp/clients-samp/tree/Polski).
- **Türk** > [README](https://github.com/spc-samp/clients-samp/tree/Turk).
- **Deutsch** > [README](https://github.com/spc-samp/clients-samp/tree/Deutsch).
- **Русский** > [README](https://github.com/spc-samp/clients-samp/tree/Русский).
- **Français** > [README](https://github.com/spc-samp/clients-samp/tree/Francais).
- **Italiano** > [README](https://github.com/spc-samp/clients-samp/tree/Italiano).
- **Svensk** > [README](https://github.com/spc-samp/clients-samp/tree/Svensk).

## Índice

- [clients-samp](#clients-samp)
  - [🌍](#)
  - [Índice](#índice)
  - [Introducción](#introducción)
  - [Estructura del Proyecto](#estructura-del-proyecto)
  - [Dependencias](#dependencias)
    - [Instalación de Dependencias](#instalación-de-dependencias)
    - [Dependencias Detalladas](#dependencias-detalladas)
  - [Instalación](#instalación)
    - [Método 1: Ejecutable Pre-compilado](#método-1-ejecutable-pre-compilado)
    - [Método 2: Compilación Manual](#método-2-compilación-manual)
  - [Importante](#importante)
  - [Versiones Disponibles](#versiones-disponibles)
  - [Detalles Técnicos](#detalles-técnicos)
    - [Estructura del Código](#estructura-del-código)
      - [Clase de Colores](#clase-de-colores)
      - [Método de Creación de Etiqueta Estilizada](#método-de-creación-de-etiqueta-estilizada)
    - [Métodos Fundamentales](#métodos-fundamentales)
      - [Verificación de Carpeta](#verificación-de-carpeta)
      - [Extracción de Archivos](#extracción-de-archivos)
  - [Configuraciones de PyInstaller](#configuraciones-de-pyinstaller)
    - [Ejemplo de Archivo Spec](#ejemplo-de-archivo-spec)
    - [Configuraciones Importantes](#configuraciones-importantes)

## Introducción

El proyecto **clients-samp** es un conjunto de instaladores para el mod SA:MP (San Andreas Multiplayer), desarrollado para simplificar la instalación y configuración del cliente de juego.

## Estructura del Proyecto

```
clients-samp/
│
├── samp-client-r1/
├── samp-client-r1-voip/
├── samp-client-r2/
├── samp-client-r3/
├── samp-client-r3-voip/
├── samp-client-r4/
└── samp-client-r5/
```

Cada versión del cliente sigue una estructura de directorio estándar:

```
samp-client-v/
│
├── archives/
│   └── samp-client-v.zip      # Archivos comprimidos para instalación
│
├── icons/                      # Íconos e imágenes del instalador
│   ├── spc.png
│   ├── discord.png
│   └── ...
│
├── samp-client-v.py           # Script principal en Python
└── samp-client-v.spec         # Configuración de PyInstaller
```

## Dependencias

### Instalación de Dependencias

```bash
pip install pillow
pip install sv-ttk
```

### Dependencias Detalladas

| Biblioteca | Versión Recomendada | Propósito |
|-----------|---------------------|-----------|
| `tkinter` | Predeterminado de Python | Interfaz gráfica |
| `PIL` (Pillow) | 9.5.0+ | Procesamiento de imágenes |
| `sv_ttk` | 2.0.0+ | Tema moderno para Tkinter |
| `threading` | Predeterminado de Python | Procesamiento asíncrono |
| `zipfile` | Predeterminado de Python | Extracción de archivos |
| `webbrowser` | Predeterminado de Python | Apertura de enlaces externos |

## Instalación

### Método 1: Ejecutable Pre-compilado

1. Accede a la sección de [releases](https://github.com/spc-samp/clients-samp/releases/tag/es-1.0)
2. Descarga el ejecutable que desees
3. Ejecuta el archivo `.exe`

### Método 2: Compilación Manual

```bash
# Instala PyInstaller
pip install pyinstaller

# Navega al directorio del cliente
cd samp-client-v

# Compila el proyecto
pyinstaller samp-client-v.spec
```

## Importante

**Atención:** 
- **NO** compiles el archivo Python (`samp-client-v.py`)
- **SIEMPRE** compile usando el archivo `.spec` correspondiente
- Ejemplo correcto de compilación: `pyinstaller samp-client-v.spec`

**¿Por qué?**
El archivo `.spec` contiene configuraciones cruciales:
- Inclusión de archivos estáticos (íconos, archivos ZIP)
- Configuraciones de ícono del ejecutable
- Definición de dependencias y recursos adicionales

> [!WARNING]
> La compilación directa del archivo Python **EXCLUIRÁ** recursos esenciales como imágenes y archivos de instalación, a menos que agregue los parámetros `--add-data "samp-client-v.zip;."` y `--icon="ico-spc.ico"`.

## Versiones Disponibles

1. `samp-client-r1`
2. `samp-client-r1-voip` SAMPVOICE incluido
3. `samp-client-r2`
4. `samp-client-r3`
5. `samp-client-r3-voip` SAMPVOICE incluido
6. `samp-client-r4`
7. `samp-client-r5`

## Detalles Técnicos

### Estructura del Código

#### Clase de Colores

```python
@dataclass
class Client_Colores:
    background: str = '#1E1E1E'
    primary: str = '#3B8AFF'
    secondary: str = '#2C2C2C'
    text_primary: str = '#FFFFFF'
    text_secondary: str = '#A0A0A0'
```

#### Método de Creación de Etiqueta Estilizada

```python
def Crear_Etiqueta_Estilizada(
    self, 
    parent, 
    texto: str, 
    fuente: tuple = ('Segoe UI', 12), 
    color: Optional[str] = None
) -> ttk.Label:
    return ttk.Label(
        parent, 
        text=texto, 
        font=fuente,
        foreground=color or self.colors.text_secondary
    )
```

### Métodos Fundamentales

#### Verificación de Carpeta

```python
def Verificacion_Completa():
    carpeta = self.carpeta_seleccionada.get()

    # Verificaciones de integridad de la carpeta
    if not os.path.exists(carpeta):
        Mostrar_Error("Error: La carpeta seleccionada no existe.")
        return

    if os.path.basename(carpeta) != "Grand Theft Auto San Andreas":
        Mostrar_Error("Error: Carpeta inválida. Seleccione la carpeta correcta de GTA San Andreas (Grand Theft Auto San Andreas).")
        return

    # Verificación del ejecutable
    ruta_exe = os.path.join(carpeta, "gta_sa.exe")
    if not os.path.isfile(ruta_exe):
        Mostrar_Error("Error: El archivo 'gta_sa.exe' no se encontró en la carpeta.")
        return
```

#### Extracción de Archivos

```python
def Instalacion_Client():
    ruta_zip = getattr(sys, "_MEIPASS", os.path.abspath("."))
    archivo_zip = os.path.join(ruta_zip, "archives", "samp-client-v.zip")
    
    carpeta_destino = self.carpeta_seleccionada.get()

    with zipfile.ZipFile(archivo_zip, 'r') as zip_ref:
        archivos = zip_ref.namelist()
        total_archivos = len(archivos)
        
        for i, archivo in enumerate(archivos, start=1):
            # Barra de progreso y actualización de estado
            archivo_label.config(text=f"Extrayendo: {os.path.basename(archivo)}")
            barra_progreso['value'] = (i / total_archivos) * 100
            self.root.update_idletasks()
            
            zip_ref.extract(archivo, carpeta_destino)
            self.archivos_extraidos.append(archivo)
```

## Configuraciones de PyInstaller

### Ejemplo de Archivo Spec

```python
datas = [
    ('archives/samp-client-v.zip', 'archives'),
    ('icons/spc.png', 'icons'),
    ('icons/youtube.png', 'icons'),
    # Otros archivos estáticos
]

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='samp-client-v',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon='icons/ico-spc.ico',
)
```

### Configuraciones Importantes

- `datas`: Define archivos adicionales a incluir
- `name`: Nombre del ejecutable final
- `icon`: Ícono personalizado para el ejecutable
- `console=False`: Oculta la ventana de consola
