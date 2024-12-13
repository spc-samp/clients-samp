# clients-samp

## 🌍

- **Português** > [README](https://github.com/spc-samp/clients-samp)
- **Español** > [README](https://github.com/spc-samp/clients-samp/tree/Espanol)
- **Polski** > [README](https://github.com/spc-samp/clients-samp/tree/Polski)
- **Türk** > [README](https://github.com/spc-samp/clients-samp/tree/Turk)
- **Deutsch** > [README](https://github.com/spc-samp/clients-samp/tree/Deutsch)
- **Русский** > [README](https://github.com/spc-samp/clients-samp/tree/Русский)
- **Français** > [README](https://github.com/spc-samp/clients-samp/tree/Francais)
- **Italiano** > [README](https://github.com/spc-samp/clients-samp/tree/Italiano)
- **Svenska** > [README](https://github.com/spc-samp/clients-samp/tree/Svensk)

## Table of Contents

- [clients-samp](#clients-samp)
  - [🌍](#)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Project Structure](#project-structure)
  - [Dependencies](#dependencies)
    - [Dependencies Installation](#dependencies-installation)
    - [Detailed Dependencies](#detailed-dependencies)
  - [Installation](#installation)
    - [Method 1: Pre-Compiled Executable](#method-1-pre-compiled-executable)
    - [Method 2: Manual Compilation](#method-2-manual-compilation)
  - [Important](#important)
  - [Available Versions](#available-versions)
  - [Technical Details](#technical-details)
    - [Code Structure](#code-structure)
      - [Color Class](#color-class)
      - [Styled Label Creation Method](#styled-label-creation-method)
    - [Fundamental Methods](#fundamental-methods)
      - [Folder Verification](#folder-verification)
      - [File Extraction](#file-extraction)
  - [PyInstaller Configuration](#pyinstaller-configuration)
    - [Spec File Example](#spec-file-example)
    - [Important Configurations](#important-configurations)

## Introduction

The **clients-samp** project is a set of installers for the SA:MP (San Andreas Multiplayer) mod, developed to simplify the game client installation and configuration.

## Project Structure

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

Each client version follows a standard directory structure:

```
samp-client-v/
│
├── archives/
│   └── samp-client-v.zip      # Compressed files for installation
│
├── icons/                      # Installer icons and images
│   ├── spc.png
│   ├── discord.png
│   └── ...
│
├── samp-client-v.py           # Main Python script
└── samp-client-v.spec         # PyInstaller configuration
```

## Dependencies

### Dependencies Installation

```bash
pip install pillow
pip install sv-ttk
```

### Detailed Dependencies

| Library | Recommended Version | Purpose |
|---------|---------------------|---------|
| `tkinter` | Python default | Graphical interface |
| `PIL` (Pillow) | 9.5.0+ | Image processing |
| `sv_ttk` | 2.0.0+ | Modern Tkinter theme |
| `threading` | Python default | Asynchronous processing |
| `zipfile` | Python default | File extraction |
| `webbrowser` | Python default | Opening external links |

## Installation

### Method 1: Pre-Compiled Executable

1. Access the [releases](https://github.com/spc-samp/clients-samp/releases/tag/en-1.0) section
2. Download the executable you want
3. Run the `.exe` file

### Method 2: Manual Compilation

```bash
# Install PyInstaller
pip install pyinstaller

# Navigate to the client directory
cd samp-client-v

# Compile the project
pyinstaller samp-client-v.spec
```

## Important

**Attention:**
- **DO NOT** compile the Python file (`samp-client-v.py`)
- **ALWAYS** compile using the corresponding `.spec` file
- Correct compilation example: `pyinstaller samp-client-v.spec`

**Why?**
The `.spec` file contains crucial configurations:
- Inclusion of static files (icons, ZIP files)
- Executable icon settings
- Definition of additional dependencies and resources

> [!WARNING]
> Direct compilation of the Python file will **EXCLUDE** essential resources like images and installation files, unless you add the parameters `--add-data "samp-client-v.zip;."` and `--icon="ico-spc.ico"`.

## Available Versions

1. `samp-client-r1`
2. `samp-client-r1-voip` SAMPVOICE included
3. `samp-client-r2`
4. `samp-client-r3`
5. `samp-client-r3-voip` SAMPVOICE included
6. `samp-client-r4`
7. `samp-client-r5`

## Technical Details

### Code Structure

#### Color Class

```python
@dataclass
class Client_Colors:
    background: str = '#1E1E1E'
    primary: str = '#3B8AFF'
    secondary: str = '#2C2C2C'
    text_primary: str = '#FFFFFF'
    text_secondary: str = '#A0A0A0'
```

#### Styled Label Creation Method

```python
def Create_Styled_Label(
    self, 
    parent, 
    text: str, 
    font: tuple = ('Segoe UI', 12), 
    color: Optional[str] = None
) -> ttk.Label:
    return ttk.Label(
        parent, 
        text=text, 
        font=font,
        foreground=color or self.colors.text_secondary
    )
```

### Fundamental Methods

#### Folder Verification

```python
def Verification_Complete():
    folder = self.selected_folder.get()
    
    # Folder integrity checks
    if not os.path.exists(folder):
        Show_Error("Error: The selected folder does not exist.")
        return

    if os.path.basename(folder) != "Grand Theft Auto San Andreas":
        Show_Error("Error: Invalid folder. Please select the correct GTA San Andreas folder.")
        return

    # Executable verification
    exe_path = os.path.join(folder, "gta_sa.exe")
    if not os.path.isfile(exe_path):
        Show_Error("Error: 'gta_sa.exe' file not found in the folder.")
        return
```

#### File Extraction

```python
def Client_Installation():
    zip_path = getattr(sys, "_MEIPASS", os.path.abspath("."))
    zip_file = os.path.join(zip_path, "archives", "samp-client-v.zip")
    
    destination_folder = self.selected_folder.get()

    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        files = zip_ref.namelist()
        total_files = len(files)
        
        for i, file in enumerate(files, start=1):
            # Progress bar and status update
            file_label.config(text=f"Extracting: {os.path.basename(file)}")
            progress_bar['value'] = (i / total_files) * 100
            self.root.update_idletasks()
            
            zip_ref.extract(file, destination_folder)
            self.extracted_files.append(file)
```

## PyInstaller Configuration

### Spec File Example

```python
datas = [
    ('archives/samp-client-v.zip', 'archives'),
    ('icons/spc.png', 'icons'),
    ('icons/youtube.png', 'icons'),
    # Other static files
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

### Important Configurations

- `datas`: Defines additional files to be included
- `name`: Final executable name
- `icon`: Custom executable icon
- `console=False`: Hides console window
