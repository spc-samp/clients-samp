# clients-samp

## 🌍

- **Português** > [README](https://github.com/spc-samp/clients-samp).
- **English** > [README](https://github.com/spc-samp/clients-samp/tree/English).
- **Español** > [README](https://github.com/spc-samp/clients-samp/tree/Espanol).
- **Türk** > [README](https://github.com/spc-samp/clients-samp/tree/Turk).
- **Deutsch** > [README](https://github.com/spc-samp/clients-samp/tree/Deutsch).
- **Русский** > [README](https://github.com/spc-samp/clients-samp/tree/Русский).
- **Français** > [README](https://github.com/spc-samp/clients-samp/tree/Francais).
- **Italiano** > [README](https://github.com/spc-samp/clients-samp/tree/Italiano).
- **Svenska** > [README](https://github.com/spc-samp/clients-samp/tree/Svenska).

## Spis treści

- [clients-samp](#clients-samp)
  - [🌍](#)
  - [Spis treści](#spis-treści)
  - [Wprowadzenie](#wprowadzenie)
  - [Struktura projektu](#struktura-projektu)
  - [Zależności](#zależności)
    - [Instalacja zależności](#instalacja-zależności)
    - [Szczegółowe zależności](#szczegółowe-zależności)
  - [Instalacja](#instalacja)
    - [Metoda 1: Wstępnie skompilowany plik wykonywalny](#metoda-1-wstępnie-skompilowany-plik-wykonywalny)
    - [Metoda 2: Ręczna kompilacja](#metoda-2-ręczna-kompilacja)
  - [Ważne](#ważne)
  - [Dostępne wersje](#dostępne-wersje)
  - [Szczegóły techniczne](#szczegóły-techniczne)
    - [Struktura kodu](#struktura-kodu)
      - [Klasa kolorów](#klasa-kolorów)
      - [Metoda tworzenia stylizowanej etykiety](#metoda-tworzenia-stylizowanej-etykiety)
    - [Podstawowe metody](#podstawowe-metody)
      - [Weryfikacja folderu](#weryfikacja-folderu)
      - [Wyodrębnianie plików](#wyodrębnianie-plików)
  - [Konfiguracje PyInstallera](#konfiguracje-pyinstallera)
    - [Przykładowy plik spec](#przykładowy-plik-spec)
    - [Ważne konfiguracje](#ważne-konfiguracje)

## Wprowadzenie

Projekt **clients-samp** to zestaw instalatorów dla moda SA:MP (San Andreas Multiplayer), stworzony w celu uproszczenia instalacji i konfiguracji klienta gry.

## Struktura projektu

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

Każda wersja klienta ma standardową strukturę katalogów:

```
samp-client-v/
│
├── archives/
│   └── samp-client-v.zip      # Skompresowane pliki do instalacji
│
├── icons/                      # Ikony i obrazy instalatora
│   ├── spc.png
│   ├── discord.png
│   └── ...
│
├── samp-client-v.py           # Główny skrypt w Pythonie
└── samp-client-v.spec         # Konfiguracja PyInstallera
```

## Zależności

### Instalacja zależności

```bash
pip install pillow
pip install sv-ttk
```

### Szczegółowe zależności

| Biblioteka | Zalecana wersja | Cel |
|-----------|------------------|-----|
| `tkinter` | Domyślna w Pythonie | Interfejs graficzny |
| `PIL` (Pillow) | 9.5.0+ | Przetwarzanie obrazów |
| `sv_ttk` | 2.0.0+ | Nowoczesny motyw dla Tkinter |
| `threading` | Domyślna w Pythonie | Przetwarzanie asynchroniczne |
| `zipfile` | Domyślna w Pythonie | Wyodrębnianie plików |
| `webbrowser` | Domyślna w Pythonie | Otwieranie linków zewnętrznych |

## Instalacja

### Metoda 1: Wstępnie skompilowany plik wykonywalny

1. Przejdź do sekcji [releases](https://github.com/spc-samp/clients-samp/releases/tag/pl-1.0)
2. Pobierz żądany plik wykonywalny
3. Uruchom plik `.exe`

### Metoda 2: Ręczna kompilacja

```bash
# Zainstaluj PyInstallera
pip install pyinstaller

# Przejdź do katalogu klienta
cd samp-client-v

# Skompiluj projekt
pyinstaller samp-client-v.spec
```

## Ważne

**Uwaga:** 
- **NIE** kompiluj pliku Python (`samp-client-v.py`)
- **ZAWSZE** kompiluj używając odpowiedniego pliku `.spec`
- Przykład poprawnej kompilacji: `pyinstaller samp-client-v.spec`

**Dlaczego?**
Plik `.spec` zawiera kluczowe konfiguracje:
- Dołączanie plików statycznych (ikony, pliki ZIP)
- Ustawienia ikony pliku wykonywalnego
- Definicja dodatkowych zależności i zasobów

> [!WARNING]
> Bezpośrednia kompilacja pliku Python **USUNIE** kluczowe zasoby, takie jak obrazy i pliki instalacyjne, chyba że dodasz parametry `--add-data "samp-client-v.zip;."` i `--icon="ico-spc.ico"`.

## Dostępne wersje

1. `samp-client-r1`
2. `samp-client-r1-voip` z dołączonym SAMPVOICE
3. `samp-client-r2`
4. `samp-client-r3`
5. `samp-client-r3-voip` z dołączonym SAMPVOICE
6. `samp-client-r4`
7. `samp-client-r5`

## Szczegóły techniczne

### Struktura kodu

#### Klasa kolorów

```python
@dataclass
class Client_Rdzenie:
    background: str = '#1E1E1E'
    primary: str = '#3B8AFF'
    secondary: str = '#2C2C2C'
    text_primary: str = '#FFFFFF'
    text_secondary: str = '#A0A0A0'
```

#### Metoda tworzenia stylizowanej etykiety

```python
def Utworz_Etykiete_Stylizowana(
    self, 
    parent, 
    tekst: str, 
    czcionka: tuple = ('Segoe UI', 12), 
    kolor: Optional[str] = None
) -> ttk.Label:
    return ttk.Label(
        parent, 
        text=tekst, 
        font=czcionka,
        foreground=kolor or self.colors.text_secondary
    )
```

### Podstawowe metody

#### Weryfikacja folderu

```python
def Weryfikacja_Zakonczona():
    folder = self.wybrana_folder.get()
    
    # Weryfikacja integralności folderu
    if not os.path.exists(folder):
        Wyswietl_Blad("Błąd: Wybrany folder nie istnieje.")
        return

    if os.path.basename(folder) != "Grand Theft Auto San Andreas":
        Wyswietl_Blad("Błąd: Nieprawidłowy folder. Wybierz właściwy folder GTA San Andreas.")
        return

    # Weryfikacja pliku wykonywalnego
    sciezka_exe = os.path.join(folder, "gta_sa.exe")
    if not os.path.isfile(sciezka_exe):
        Wyswietl_Blad("Błąd: Nie znaleziono pliku 'gta_sa.exe' w folderze.")
        return
```

#### Wyodrębnianie plików

```python
def Instalacja_Client():
    sciezka_zip = getattr(sys, "_MEIPASS", os.path.abspath("."))
    plik_zip = os.path.join(sciezka_zip, "archives", "samp-client-v.zip")
    
    folder_docelowy = self.wybrana_folder.get()

    with zipfile.ZipFile(plik_zip, 'r') as zip_ref:
        pliki = zip_ref.namelist()
        wszystkie_pliki = len(pliki)
        
        for i, plik in enumerate(pliki, start=1):
            # Pasek postępu i aktualizacja statusu
            etykieta_pliku.config(text=f"Wypakowywanie: {os.path.basename(plik)}")
            pasek_postepu['value'] = (i / wszystkie_pliki) * 100
            self.root.update_idletasks()
            
            zip_ref.extract(plik, folder_docelowy)
            self.wyodrebnione_pliki.append(plik)
```

## Konfiguracje PyInstallera

### Przykładowy plik spec

```python
datas = [
    ('archives/samp-client-v.zip', 'archives'),
    ('icons/spc.png', 'icons'),
    ('icons/youtube.png', 'icons'),
    # Inne pliki statyczne
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

### Ważne konfiguracje

- `datas`: Definiuje dodatkowe pliki do dołączenia
- `name`: Nazwa końcowego pliku wykonywalnego
- `icon`: Niestandardowa ikona dla pliku wykonywalnego
- `console=False`: Ukrywa okno konsoli
