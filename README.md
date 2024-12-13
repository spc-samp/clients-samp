# clients-samp

## 🌍

- **Português** > [README](https://github.com/spc-samp/clients-samp).
- **English** > [README](https://github.com/spc-samp/clients-samp/tree/English).
- **Español** > [README](https://github.com/spc-samp/clients-samp/tree/Espanol).
- **Polski** > [README](https://github.com/spc-samp/clients-samp/tree/Polski).
- **Deutsch** > [README](https://github.com/spc-samp/clients-samp/tree/Deutsch).
- **Русский** > [README](https://github.com/spc-samp/clients-samp/tree/Русский).
- **Français** > [README](https://github.com/spc-samp/clients-samp/tree/Francais).
- **Italiano** > [README](https://github.com/spc-samp/clients-samp/tree/Italiano).
- **Svenska** > [README](https://github.com/spc-samp/clients-samp/tree/Svensk).

## İçindekiler

- [clients-samp](#clients-samp)
  - [🌍](#)
  - [İçindekiler](#i̇çindekiler)
  - [Giriş](#giriş)
  - [Proje Yapısı](#proje-yapısı)
  - [Bağımlılıklar](#bağımlılıklar)
    - [Bağımlılıkların Kurulumu](#bağımlılıkların-kurulumu)
    - [Detaylı Bağımlılıklar](#detaylı-bağımlılıklar)
  - [Kurulum](#kurulum)
    - [Yöntem 1: Önceden Derlenmiş Yürütülebilir](#yöntem-1-önceden-derlenmiş-yürütülebilir)
    - [Yöntem 2: Manuel Derleme](#yöntem-2-manuel-derleme)
  - [Önemli](#önemli)
  - [Mevcut Sürümler](#mevcut-sürümler)
  - [Teknik Detaylar](#teknik-detaylar)
    - [Kod Yapısı](#kod-yapısı)
      - [Renk Sınıfı](#renk-sınıfı)
      - [Stil Etiket Oluşturma Yöntemi](#stil-etiket-oluşturma-yöntemi)
    - [Temel Metodlar](#temel-metodlar)
      - [Klasör Doğrulaması](#klasör-doğrulaması)
      - [Dosya Çıkarma](#dosya-çıkarma)
  - [PyInstaller Ayarları](#pyinstaller-ayarları)
    - [Spec Dosyası Örneği](#spec-dosyası-örneği)
    - [Önemli Ayarlar](#önemli-ayarlar)

## Giriş

**clients-samp** projesi, oyun istemcisinin kurulum ve yapılandırmasını basitleştirmek için geliştirilen SA:MP (San Andreas Multiplayer) mod yükleyicileri topluluğudur.

## Proje Yapısı

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

Her istemci sürümü standart bir dizin yapısına sahiptir:

```
samp-client-v/
│
├── archives/
│   └── samp-client-v.zip      # Kurulum için sıkıştırılmış dosyalar
│
├── icons/                      # Yükleyici simgeleri ve görüntüleri
│   ├── spc.png
│   ├── discord.png
│   └── ...
│
├── samp-client-v.py           # Ana Python betiği
└── samp-client-v.spec         # PyInstaller yapılandırması
```

## Bağımlılıklar

### Bağımlılıkların Kurulumu

```bash
pip install pillow
pip install sv-ttk
```

### Detaylı Bağımlılıklar

| Kütüphane | Önerilen Versiyon | Amaç |
|-----------|-------------------|------|
| `tkinter` | Python Varsayılan | Grafik arayüz |
| `PIL` (Pillow) | 9.5.0+ | Görüntü işleme |
| `sv_ttk` | 2.0.0+ | Tkinter için modern tema |
| `threading` | Python Varsayılan | Asenkron işleme |
| `zipfile` | Python Varsayılan | Dosya çıkarma |
| `webbrowser` | Python Varsayılan | Dış bağlantıları açma |

## Kurulum

### Yöntem 1: Önceden Derlenmiş Yürütülebilir

1. [releases](https://github.com/spc-samp/clients-samp/releases/tag/tr-1.0) bölümüne gidin
2. İstediğiniz yürütülebilir dosyayı indirin
3. `.exe` dosyasını çalıştırın

### Yöntem 2: Manuel Derleme

```bash
# PyInstaller'ı yükleyin
pip install pyinstaller

# İstemci dizinine gidin
cd samp-client-v

# Projeyi derleyin
pyinstaller samp-client-v.spec
```

## Önemli

**Dikkat:** 
- Python dosyasını (`samp-client-v.py`) **DERLEMEYİN**
- Her zaman ilgili `.spec` dosyasını kullanarak derleyin
- Doğru derleme örneği: `pyinstaller samp-client-v.spec`

**Neden?**
`.spec` dosyası kritik ayarları içerir:
- Statik dosyaların dahil edilmesi (simgeler, ZIP dosyaları)
- Yürütülebilir simge ayarları
- Ek bağımlılıkların ve kaynakların tanımlanması

> [!WARNING]
> Doğrudan Python dosyasını derlemek, görüntüler ve kurulum dosyaları gibi temel kaynakları **ÇIKARACAKTIR**, aksi takdirde `--add-data "samp-client-v.zip;."` ve `--icon="ico-spc.ico"` parametrelerini ekleyeceksiniz.

## Mevcut Sürümler

1. `samp-client-r1`
2. `samp-client-r1-voip` SAMPVOICE dahil
3. `samp-client-r2`
4. `samp-client-r3`
5. `samp-client-r3-voip` SAMPVOICE dahil
6. `samp-client-r4`
7. `samp-client-r5`

## Teknik Detaylar

### Kod Yapısı

#### Renk Sınıfı

```python
@dataclass
class Client_Renkleri:
    background: str = '#1E1E1E'
    primary: str = '#3B8AFF'
    secondary: str = '#2C2C2C'
    text_primary: str = '#FFFFFF'
    text_secondary: str = '#A0A0A0'
```

#### Stil Etiket Oluşturma Yöntemi

```python
def Etiket_Olustur(
    self, 
    parent, 
    metin: str, 
    font: tuple = ('Segoe UI', 12), 
    renk: Optional[str] = None
) -> ttk.Label:
    return ttk.Label(
        parent, 
        text=metin, 
        font=font,
        foreground=renk or self.colors.text_secondary
    )
```

### Temel Metodlar

#### Klasör Doğrulaması

```python
def Dogrulama_Tamamlandi():
    klasor = self.secilen_klasor.get()
    
    # Klasör bütünlük kontrolleri
    if not os.path.exists(klasor):
        Hatay_Goster("Hata: Seçilen klasör mevcut değil.")
        return

    if os.path.basename(klasor) != "Grand Theft Auto San Andreas":
        Hatay_Goster("Hata: Geçersiz klasör. Lütfen doğru GTA San Andreas klasörünü seçin.")
        return

    # Yürütülebilir dosya kontrolü
    exe_yolu = os.path.join(klasor, "gta_sa.exe")
    if not os.path.isfile(exe_yolu):
        Hatay_Goster("Hata: 'gta_sa.exe' dosyası klasörde bulunamadı.")
        return
```

#### Dosya Çıkarma

```python
def Client_Yukleme():
    zip_yolu = getattr(sys, "_MEIPASS", os.path.abspath("."))
    zip_dosyasi = os.path.join(zip_yolu, "archives", "samp-client-v.zip")
    
    hedef_klasor = self.secilen_klasor.get()

    with zipfile.ZipFile(zip_dosyasi, 'r') as zip_ref:
        dosyalar = zip_ref.namelist()
        toplam_dosya = len(dosyalar)
        
        for i, dosya in enumerate(dosyalar, start=1):
            # İlerleme çubuğu ve durum güncellemesi
            dosya_etiketi.config(text=f"Çıkartılıyor: {os.path.basename(dosya)}")
            ilerleme_cubugu['value'] = (i / toplam_dosya) * 100
            self.root.update_idletasks()
            
            zip_ref.extract(dosya, hedef_klasor)
            self.cikarilan_dosyalar.append(dosya)
```

## PyInstaller Ayarları

### Spec Dosyası Örneği

```python
datas = [
    ('archives/samp-client-v.zip', 'archives'),
    ('icons/spc.png', 'icons'),
    ('icons/youtube.png', 'icons'),
    # Diğer statik dosyalar
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

### Önemli Ayarlar

- `datas`: Eklenecek ek dosyaları tanımlar
- `name`: Son yürütülebilir dosyanın adı
- `icon`: Yürütülebilir için özel simge
- `console=False`: Konsol penceresini gizler
