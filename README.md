# clients-samp

## 🌍

- **Português** > [README](https://github.com/spc-samp/clients-samp).
- **English** > [README](https://github.com/spc-samp/clients-samp/tree/English).
- **Español** > [README](https://github.com/spc-samp/clients-samp/tree/Espanol).
- **Polski** > [README](https://github.com/spc-samp/clients-samp/tree/Polski).
- **Türk** > [README](https://github.com/spc-samp/clients-samp/tree/Turk).
- **Deutsch** > [README](https://github.com/spc-samp/clients-samp/tree/Deutsch).
- **Русский** > [README](https://github.com/spc-samp/clients-samp/tree/Русский).
- **Français** > [README](https://github.com/spc-samp/clients-samp/tree/Francais).
- **Svenska** > [README](https://github.com/spc-samp/clients-samp/tree/Svenska).

## Indice

- [clients-samp](#clients-samp)
  - [🌍](#)
  - [Indice](#indice)
  - [Introduzione](#introduzione)
  - [Struttura del Progetto](#struttura-del-progetto)
  - [Dipendenze](#dipendenze)
    - [Installazione delle Dipendenze](#installazione-delle-dipendenze)
    - [Dettagli delle Dipendenze](#dettagli-delle-dipendenze)
  - [Installazione](#installazione)
    - [Metodo 1: Eseguibile Pre-Compilato](#metodo-1-eseguibile-pre-compilato)
    - [Metodo 2: Compilazione Manuale](#metodo-2-compilazione-manuale)
  - [Importante](#importante)
  - [Versioni Disponibili](#versioni-disponibili)
  - [Dettagli Tecnici](#dettagli-tecnici)
    - [Struttura del Codice](#struttura-del-codice)
      - [Classe Colori](#classe-colori)
      - [Metodo di Creazione di un'Etichetta Stilizzata](#metodo-di-creazione-di-unetichetta-stilizzata)
    - [Metodi Fondamentali](#metodi-fondamentali)
      - [Verifica della Cartella](#verifica-della-cartella)
      - [Estrazione dei File](#estrazione-dei-file)
  - [Configurazioni di PyInstaller](#configurazioni-di-pyinstaller)
    - [Esempio di File Spec](#esempio-di-file-spec)
    - [Configurazioni Importanti](#configurazioni-importanti)

## Introduzione

Il progetto **clients-samp** è un insieme di programmi di installazione per il mod SA:MP (San Andreas Multiplayer), sviluppato per semplificare l'installazione e la configurazione del client di gioco.

## Struttura del Progetto

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

Ogni versione del client segue una struttura di directory standard:

```
samp-client-v/
│
├── archives/
│   └── samp-client-v.zip      # File compressi per l'installazione
│
├── icons/                      # Icone e immagini del programma di installazione
│   ├── spc.png
│   ├── discord.png
│   └── ...
│
├── samp-client-v.py           # Script principale in Python
└── samp-client-v.spec         # Configurazione di PyInstaller
```

## Dipendenze

### Installazione delle Dipendenze

```bash
pip install pillow
pip install sv-ttk
```

### Dettagli delle Dipendenze

| Libreria | Versione Consigliata | Scopo |
|----------|----------------------|-------|
| `tkinter` | Standard di Python | Interfaccia grafica |
| `PIL` (Pillow) | 9.5.0+ | Elaborazione immagini |
| `sv_ttk` | 2.0.0+ | Tema moderno per Tkinter |
| `threading` | Standard di Python | Elaborazione asincrona |
| `zipfile` | Standard di Python | Estrazione di file |
| `webbrowser` | Standard di Python | Apertura di link esterni |

## Installazione

### Metodo 1: Eseguibile Pre-Compilato

1. Accedi alla sezione [releases](https://github.com/spc-samp/clients-samp/releases/tag/it-1.0)
2. Scarica l'eseguibile desiderato
3. Esegui il file `.exe`

### Metodo 2: Compilazione Manuale

```bash
# Installa PyInstaller
pip install pyinstaller

# Vai alla directory del client
cd samp-client-v

# Compila il progetto
pyinstaller samp-client-v.spec
```

## Importante

**Attenzione:** 
- **NON** compilare direttamente il file Python (`samp-client-v.py`)
- **SEMPRE** compilare usando il file `.spec` corrispondente
- Esempio corretto di compilazione: `pyinstaller samp-client-v.spec`

**Perché?**
Il file `.spec` contiene impostazioni cruciali:
- Inclusione di file statici (icone, file ZIP)
- Configurazioni dell'icona dell'eseguibile
- Definizione di dipendenze e risorse aggiuntive

> [!WARNING]
> La compilazione diretta del file Python **ESCLUDERÀ** risorse essenziali come immagini e file di installazione, a meno che non si aggiungano i parametri `--add-data "samp-client-v.zip;."` e `--icon="ico-spc.ico"`.

## Versioni Disponibili

1. `samp-client-r1`
2. `samp-client-r1-voip` SAMPVOICE incluso
3. `samp-client-r2`
4. `samp-client-r3`
5. `samp-client-r3-voip` SAMPVOICE incluso
6. `samp-client-r4`
7. `samp-client-r5`

## Dettagli Tecnici

### Struttura del Codice

#### Classe Colori

```python
@dataclass
class Client_Colori:
    background: str = '#1E1E1E'
    primary: str = '#3B8AFF'
    secondary: str = '#2C2C2C'
    text_primary: str = '#FFFFFF'
    text_secondary: str = '#A0A0A0'
```

#### Metodo di Creazione di un'Etichetta Stilizzata

```python
def Crea_Bottone_Stilizzato(
    self, 
    parent, 
    testo: str, 
    comando: Callable, 
    stile: str = 'Accent.TButton'
) -> ttk.Button:
    return ttk.Button(
        parent, 
        text=testo, 
        command=comando,
        style=stile
    )
```

### Metodi Fondamentali

#### Verifica della Cartella

```python
def Verifica_Completata():
    cartella = self.cartella_selezionata.get()
    
    # Verifiche di integrità della cartella
    if not os.path.exists(cartella):
        Mostra_Errore("Errore: La cartella selezionata non esiste.")
        return

    if os.path.basename(cartella) != "Grand Theft Auto San Andreas":
        Mostra_Errore("Errore: Cartella non valida. Seleziona la cartella corretta di GTA San Andreas (Grand Theft Auto San Andreas).")
        return

    # Verifica dell'eseguibile
    percorso_exe = os.path.join(cartella, "gta_sa.exe")
    if not os.path.isfile(percorso_exe):
        Mostra_Errore("Errore: Il file 'gta_sa.exe' non è stato trovato nella cartella.")
        return
```

#### Estrazione dei File

```python
def Installazione_Client():
    percorso_zip = getattr(sys, "_MEIPASS", os.path.abspath("."))
    file_zip = os.path.join(percorso_zip, "archives", "samp-client-v.zip")
    
    cartella_destinazione = self.cartella_selezionata.get()

    with zipfile.ZipFile(file_zip, 'r') as zip_ref:
        file = zip_ref.namelist()
        totale_file = len(file)
        
        for i, file_singolo in enumerate(file, start=1):
            # Barra di progresso e aggiornamento dello stato
            etichetta_file.config(text=f"Estraendo: {os.path.basename(file_singolo)}")
            barra_progresso['value'] = (i / totale_file) * 100
            self.root.update_idletasks()
            
            zip_ref.extract(file_singolo, cartella_destinazione)
            self.file_estratti.append(file_singolo)
```

## Configurazioni di PyInstaller

### Esempio di File Spec

```python
datas = [
    ('archives/samp-client-v.zip', 'archives'),
    ('icons/spc.png', 'icons'),
    ('icons/youtube.png', 'icons'),
    # Altri file statici
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

### Configurazioni Importanti

- `datas`: Definisce file aggiuntivi da includere
- `name`: Nome dell'eseguibile finale
- `icon`: Icona personalizzata per l'eseguibile
- `console=False`: Nasconde la finestra della console
