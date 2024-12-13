# clients-samp

## 🌍

- **Português** > [README](https://github.com/spc-samp/clients-samp)
- **English** > [README](https://github.com/spc-samp/clients-samp/tree/English)
- **Español** > [README](https://github.com/spc-samp/clients-samp/tree/Espanol)
- **Polski** > [README](https://github.com/spc-samp/clients-samp/tree/Polski)
- **Türk** > [README](https://github.com/spc-samp/clients-samp/tree/Turk)
- **Русский** > [README](https://github.com/spc-samp/clients-samp/tree/Русский)
- **Français** > [README](https://github.com/spc-samp/clients-samp/tree/Francais)
- **Italiano** > [README](https://github.com/spc-samp/clients-samp/tree/Italiano)
- **Svenska** > [README](https://github.com/spc-samp/clients-samp/tree/Svensk)

## Inhaltsverzeichnis

- [clients-samp](#clients-samp)
  - [🌍](#)
  - [Inhaltsverzeichnis](#inhaltsverzeichnis)
  - [Einführung](#einführung)
  - [Projektstruktur](#projektstruktur)
  - [Abhängigkeiten](#abhängigkeiten)
    - [Installation der Abhängigkeiten](#installation-der-abhängigkeiten)
    - [Detaillierte Abhängigkeiten](#detaillierte-abhängigkeiten)
  - [Installation](#installation)
    - [Methode 1: Vorkompilierte ausführbare Datei](#methode-1-vorkompilierte-ausführbare-datei)
    - [Methode 2: Manuelle Kompilierung](#methode-2-manuelle-kompilierung)
  - [Wichtig](#wichtig)
  - [Verfügbare Versionen](#verfügbare-versionen)
  - [Technische Details](#technische-details)
    - [Codestruktur](#codestruktur)
      - [Farbklasse](#farbklasse)
      - [Methode zur Erstellung eines stilisierten Labels](#methode-zur-erstellung-eines-stilisierten-labels)
    - [Grundlegende Methoden](#grundlegende-methoden)
      - [Ordnerüberprüfung](#ordnerüberprüfung)
      - [Dateiextraktion](#dateiextraktion)
  - [PyInstaller-Konfigurationen](#pyinstaller-konfigurationen)
    - [Beispiel für eine Spec-Datei](#beispiel-für-eine-spec-datei)
    - [Wichtige Konfigurationen](#wichtige-konfigurationen)

## Einführung

Das Projekt **clients-samp** ist eine Sammlung von Installationsprogrammen für den SA:MP-Mod (San Andreas Multiplayer), entwickelt, um die Installation und Konfiguration des Spielclients zu vereinfachen.

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

Jede Client-Version folgt einer Standardverzeichnisstruktur:

```
samp-client-v/
│
├── archives/
│   └── samp-client-v.zip      # Komprimierte Installationsdateien
│
├── icons/                      # Installer-Symbole und Bilder
│   ├── spc.png
│   ├── discord.png
│   └── ...
│
├── samp-client-v.py           # Hauptskript in Python
└── samp-client-v.spec         # PyInstaller-Konfiguration
```

## Abhängigkeiten

### Installation der Abhängigkeiten

```bash
pip install pillow
pip install sv-ttk
```

### Detaillierte Abhängigkeiten

| Bibliothek | Empfohlene Version | Zweck |
|-----------|---------------------|--------|
| `tkinter` | Standard von Python | Grafische Benutzeroberfläche |
| `PIL` (Pillow) | 9.5.0+ | Bildverarbeitung |
| `sv_ttk` | 2.0.0+ | Modernes Tkinter-Theme |
| `threading` | Standard von Python | Asynchrone Verarbeitung |
| `zipfile` | Standard von Python | Dateiextraktion |
| `webbrowser` | Standard von Python | Öffnen externer Links |

## Installation

### Methode 1: Vorkompilierte ausführbare Datei

1. Gehen Sie zum [releases](https://github.com/spc-samp/clients-samp/releases/tag/de-1.0)
2. Laden Sie die gewünschte ausführbare Datei herunter
3. Führen Sie die `.exe`-Datei aus

### Methode 2: Manuelle Kompilierung

```bash
# PyInstaller installieren
pip install pyinstaller

# In das Client-Verzeichnis wechseln
cd samp-client-v

# Projekt kompilieren
pyinstaller samp-client-v.spec
```

## Wichtig

**Achtung:**
- Kompilieren Sie **NICHT** direkt die Python-Datei (`samp-client-v.py`)
- Verwenden Sie **IMMER** die entsprechende `.spec`-Datei
- Korrektes Kompilierungsbeispiel: `pyinstaller samp-client-v.spec`

**Warum?**
Die `.spec`-Datei enthält wichtige Konfigurationen:
- Einbinden statischer Dateien (Symbole, ZIP-Dateien)
- Konfiguration des Ausführbar-Symbols
- Definition von Abhängigkeiten und zusätzlichen Ressourcen

> [!WARNING]
> Die direkte Kompilierung der Python-Datei wird **WESENTLICHE** Ressourcen wie Bilder und Installationsdateien ausschließen, es sei denn, Sie fügen Parameter wie `--add-data "samp-client-v.zip;."` und `--icon="ico-spc.ico"` hinzu.

## Verfügbare Versionen

1. `samp-client-r1`
2. `samp-client-r1-voip` mit SAMPVOICE
3. `samp-client-r2`
4. `samp-client-r3`
5. `samp-client-r3-voip` mit SAMPVOICE
6. `samp-client-r4`
7. `samp-client-r5`

## Technische Details

### Codestruktur

#### Farbklasse

```python
@dataclass
class Client_Farben:
    background: str = '#1E1E1E'
    primary: str = '#3B8AFF'
    secondary: str = '#2C2C2C'
    text_primary: str = '#FFFFFF'
    text_secondary: str = '#A0A0A0'
```

#### Methode zur Erstellung eines stilisierten Labels

```python
def Erstellen_Beschriftung_Stilisiert(
    self, 
    parent, 
    text: str, 
    schrift: tuple = ('Segoe UI', 12), 
    farbe: Optional[str] = None
) -> ttk.Label:
    return ttk.Label(
        parent, 
        text=text, 
        font=schrift,
        foreground=farbe or self.colors.text_secondary
    )
```

### Grundlegende Methoden

#### Ordnerüberprüfung

```python
def Uberprufung_Abgeschlossen():
    ordner = self.ausgewahlter_ordner.get()
    
    # Überprüfung der Ordnerintegrität
    if not os.path.exists(ordner):
        Fehler_Anzeigen("Fehler: Der ausgewählte Ordner existiert nicht.")
        return

    if os.path.basename(ordner) != "Grand Theft Auto San Andreas":
        Fehler_Anzeigen("Fehler: Ungültiger Ordner. Bitte wählen Sie den richtigen GTA San Andreas-Ordner.")
        return

    # Überprüfung der ausführbaren Datei
    exe_pfad = os.path.join(ordner, "gta_sa.exe")
    if not os.path.isfile(exe_pfad):
        Fehler_Anzeigen("Fehler: Die Datei 'gta_sa.exe' wurde im Ordner nicht gefunden.")
        return
```

#### Dateiextraktion

```python
def Installation_Client():
    zip_pfad = getattr(sys, "_MEIPASS", os.path.abspath("."))
    zip_datei = os.path.join(zip_pfad, "archives", "samp-client-v.zip")
    
    ziel_ordner = self.ausgewahlter_ordner.get()

    with zipfile.ZipFile(zip_datei, 'r') as zip_ref:
        dateien = zip_ref.namelist()
        gesamte_dateien = len(dateien)
        
        for i, datei in enumerate(dateien, start=1):
            # Fortschrittsleiste und Statusaktualisierung
            datei_label.config(text=f"Extrahiere: {os.path.basename(datei)}")
            fortschrittsbalken['value'] = (i / gesamte_dateien) * 100
            self.root.update_idletasks()
            
            zip_ref.extract(datei, ziel_ordner)
            self.extrahierte_dateien.append(datei)
```

## PyInstaller-Konfigurationen

### Beispiel für eine Spec-Datei

```python
datas = [
    ('archives/samp-client-v.zip', 'archives'),
    ('icons/spc.png', 'icons'),
    ('icons/youtube.png', 'icons'),
    # Andere statische Dateien
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

### Wichtige Konfigurationen

- `datas`: Definiert zusätzlich einzubindende Dateien
- `name`: Name der finalen ausführbaren Datei
- `icon`: Benutzerdefiniertes Symbol für die ausführbare Datei
- `console=False`: Blendet Konsolenfenster aus
