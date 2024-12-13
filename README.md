# clients-samp

## 🌍

- **Português** > [README](https://github.com/spc-samp/clients-samp)
- **English** > [README](https://github.com/spc-samp/clients-samp/tree/English)
- **Español** > [README](https://github.com/spc-samp/clients-samp/tree/Espanol)
- **Polski** > [README](https://github.com/spc-samp/clients-samp/tree/Polski)
- **Türk** > [README](https://github.com/spc-samp/clients-samp/tree/Turk)
- **Deutsch** > [README](https://github.com/spc-samp/clients-samp/tree/Deutsch)
- **Русский** > [README](https://github.com/spc-samp/clients-samp/tree/Русский)
- **Français** > [README](https://github.com/spc-samp/clients-samp/tree/Francais)
- **Italiano** > [README](https://github.com/spc-samp/clients-samp/tree/Italiano)

## Innehållsförteckning

- [clients-samp](#clients-samp)
  - [🌍](#)
  - [Innehållsförteckning](#innehållsförteckning)
  - [Introduktion](#introduktion)
  - [Projektstruktur](#projektstruktur)
  - [Beroenden](#beroenden)
    - [Installation av beroenden](#installation-av-beroenden)
    - [Detaljerade beroenden](#detaljerade-beroenden)
  - [Installation](#installation)
    - [Metod 1: Förkompilerad körbar fil](#metod-1-förkompilerad-körbar-fil)
    - [Metod 2: Manuell kompilering](#metod-2-manuell-kompilering)
  - [Viktigt](#viktigt)
  - [Tillgängliga versioner](#tillgängliga-versioner)
  - [Tekniska detaljer](#tekniska-detaljer)
    - [Kodstruktur](#kodstruktur)
      - [Färgklass](#färgklass)
      - [Metod för att skapa stiliserad etikett](#metod-för-att-skapa-stiliserad-etikett)
    - [Grundläggande metoder](#grundläggande-metoder)
      - [Mappverifiering](#mappverifiering)
      - [Filextrahering](#filextrahering)
  - [PyInstaller-konfigurationer](#pyinstaller-konfigurationer)
    - [Exempel på spec-fil](#exempel-på-spec-fil)
    - [Viktiga konfigurationer](#viktiga-konfigurationer)

## Introduktion

Projektet **clients-samp** är en samling installationsprogram för SA:MP-modden (San Andreas Multiplayer), utvecklat för att förenkla installationen och konfigurationen av spelets klient.

## Projektstruktur

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

Varje version av klienten följer en standardmappstruktur:

```
samp-client-v/
│
├── archives/
│   └── samp-client-v.zip      # Komprimerade filer för installation
│
├── icons/                      # Installationsprogram ikoner och bilder
│   ├── spc.png
│   ├── discord.png
│   └── ...
│
├── samp-client-v.py           # Huvudskript i Python
└── samp-client-v.spec         # PyInstaller-konfiguration
```

## Beroenden

### Installation av beroenden

```bash
pip install pillow
pip install sv-ttk
```

### Detaljerade beroenden

| Bibliotek | Rekommenderad version | Syfte |
|-----------|------------------------|--------|
| `tkinter` | Standard i Python | Grafiskt gränssnitt |
| `PIL` (Pillow) | 9.5.0+ | Bildbehandling |
| `sv_ttk` | 2.0.0+ | Modernt tema för Tkinter |
| `threading` | Standard i Python | Asynkron behandling |
| `zipfile` | Standard i Python | Filextrahering |
| `webbrowser` | Standard i Python | Öppna externa länkar |

## Installation

### Metod 1: Förkompilerad körbar fil

1. Gå till [releases](https://github.com/spc-samp/clients-samp/releases/tag/sv-1.0)
2. Ladda ner den körbara fil du vill ha
3. Kör `.exe`-filen

### Metod 2: Manuell kompilering

```bash
# Installera PyInstaller
pip install pyinstaller

# Navigera till klientmappen
cd samp-client-v

# Kompilera projekt
pyinstaller samp-client-v.spec
```

## Viktigt

**Observera:** 
- **KOMPILERA INTE** Python-filen (`samp-client-v.py`)
- **KOMPILERA ALLTID** med motsvarande `.spec`-fil
- Korrekt kompileringsexempel: `pyinstaller samp-client-v.spec`

**Varför?**
`.spec`-filen innehåller kritiska konfigurationer:
- Inkludering av statiska filer (ikoner, ZIP-filer)
- Konfigurationer för körbar filikoner
- Definition av ytterligare beroenden och resurser

> [!WARNING]
> Direkt kompilering av Python-filen kommer att **UTESLUTA** väsentliga resurser som bilder och installationsfiler, såvida du inte lägger till parametrarna `--add-data "samp-client-v.zip;."` och `--icon="ico-spc.ico"`.

## Tillgängliga versioner

1. `samp-client-r1`
2. `samp-client-r1-voip` SAMPVOICE inkluderad
3. `samp-client-r2`
4. `samp-client-r3`
5. `samp-client-r3-voip` SAMPVOICE inkluderad
6. `samp-client-r4`
7. `samp-client-r5`

## Tekniska detaljer

### Kodstruktur

#### Färgklass

```python
@dataclass
class Client_Farger:
    background: str = '#1E1E1E'
    primary: str = '#3B8AFF'
    secondary: str = '#2C2C2C'
    text_primary: str = '#FFFFFF'
    text_secondary: str = '#A0A0A0'
```

#### Metod för att skapa stiliserad etikett

```python
def Skapa_Stiliserad_Etikett(
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

### Grundläggande metoder

#### Mappverifiering

```python
def Verifiering_Slutford():
    mapp = self.vald_mapp.get()
    
    # Mappintegritetsverifieringar
    if not os.path.exists(mapp):
        Visa_Fel("Fel: Den valda mappen finns inte.")
        return

    if os.path.basename(mapp) != "Grand Theft Auto San Andreas":
        Visa_Fel("Fel: Ogiltig mapp. Välj rätt mapp för GTA San Andreas (Grand Theft Auto San Andreas).")
        return

    # Kontroll av körbar fil
    exe_stig = os.path.join(mapp, "gta_sa.exe")
    if not os.path.isfile(exe_stig):
        Visa_Fel("Fel: Filen 'gta_sa.exe' hittades inte i mappen.")
        return
```

#### Filextrahering

```python
def Client_Installation():
    zip_stig = getattr(sys, "_MEIPASS", os.path.abspath("."))
    arkiv_zip = os.path.join(zip_stig, "archives", "samp-client-v.zip")
    
    mapp_destination = self.vald_mapp.get()

    with zipfile.ZipFile(arkiv_zip, 'r') as zip_ref:
        arkiv = zip_ref.namelist()
        total_arkiv = len(arkiv)
        
        for i, arkiv_item in enumerate(arkiv, start=1):
            # Förloppsindikator och statusuppdatering
            arkiv_etikett.config(text=f"Extraherar: {os.path.basename(arkiv_item)}")
            framsteg_bar['value'] = (i / total_arkiv) * 100
            self.root.update_idletasks()
            
            zip_ref.extract(arkiv_item, mapp_destination)
            self.extraherade_filer.append(arkiv_item)
```

## PyInstaller-konfigurationer

### Exempel på spec-fil

```python
datas = [
    ('archives/samp-client-v.zip', 'archives'),
    ('icons/spc.png', 'icons'),
    ('icons/youtube.png', 'icons'),
    # Andra statiska filer
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

### Viktiga konfigurationer

- `datas`: Definierar ytterligare filer som ska inkluderas
- `name`: Namn på slutlig körbar fil
- `icon`: Anpassad ikon för körbar fil
- `console=False`: Döljer konsolfönster
