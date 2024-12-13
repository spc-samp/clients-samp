# clients-samp

## 🌍

- **Português** > [README](https://github.com/spc-samp/clients-samp).
- **English** > [README](https://github.com/spc-samp/clients-samp/tree/English).
- **Español** > [README](https://github.com/spc-samp/clients-samp/tree/Espanol).
- **Polski** > [README](https://github.com/spc-samp/clients-samp/tree/Polski).
- **Türk** > [README](https://github.com/spc-samp/clients-samp/tree/Turk).
- **Deutsch** > [README](https://github.com/spc-samp/clients-samp/tree/Deutsch).
- **Français** > [README](https://github.com/spc-samp/clients-samp/tree/Francais).
- **Italiano** > [README](https://github.com/spc-samp/clients-samp/tree/Italiano).
- **Svenska** > [README](https://github.com/spc-samp/clients-samp/tree/Svensk).

## Содержание

- [clients-samp](#clients-samp)
  - [🌍](#)
  - [Содержание](#содержание)
  - [Введение](#введение)
  - [Структура проекта](#структура-проекта)
  - [Зависимости](#зависимости)
    - [Установка зависимостей](#установка-зависимостей)
    - [Подробности о зависимостях](#подробности-о-зависимостях)
  - [Установка](#установка)
    - [Метод 1: Предварительно скомпилированный исполняемый файл](#метод-1-предварительно-скомпилированный-исполняемый-файл)
    - [Метод 2: Ручная компиляция](#метод-2-ручная-компиляция)
  - [Важно](#важно)
  - [Доступные версии](#доступные-версии)
  - [Технические детали](#технические-детали)
    - [Структура кода](#структура-кода)
      - [Класс цветов](#класс-цветов)
      - [Метод создания стилизованной метки](#метод-создания-стилизованной-метки)
    - [Основные методы](#основные-методы)
      - [Проверка папки](#проверка-папки)
      - [Извлечение файлов](#извлечение-файлов)
  - [Настройки PyInstaller](#настройки-pyinstaller)
    - [Пример файла Spec](#пример-файла-spec)
    - [Важные настройки](#важные-настройки)

## Введение

Проект **clients-samp** представляет собой набор установщиков для мода SA:MP (San Andreas Multiplayer), разработанный для упрощения установки и настройки игрового клиента.

## Структура проекта

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

Каждая версия клиента следует стандартной структуре каталогов:

```
samp-client-v/
│
├── archives/
│   └── samp-client-v.zip      # Сжатые файлы для установки
│
├── icons/                      # Значки и изображения установщика
│   ├── spc.png
│   ├── discord.png
│   └── ...
│
├── samp-client-v.py           # Основной скрипт на Python
└── samp-client-v.spec         # Конфигурация PyInstaller
```

## Зависимости

### Установка зависимостей

```bash
pip install pillow
pip install sv-ttk
```

### Подробности о зависимостях

| Библиотека | Рекомендуемая версия | Назначение |
|-----------|---------------------|-----------|
| `tkinter` | Стандартный в Python | Графический интерфейс |
| `PIL` (Pillow) | 9.5.0+ | Обработка изображений |
| `sv_ttk` | 2.0.0+ | Современная тема для Tkinter |
| `threading` | Стандартный в Python | Асинхронная обработка |
| `zipfile` | Стандартный в Python | Извлечение файлов |
| `webbrowser` | Стандартный в Python | Открытие внешних ссылок |

## Установка

### Метод 1: Предварительно скомпилированный исполняемый файл

1. Перейдите в раздел [releases](https://github.com/spc-samp/clients-samp/releases/tag/ru-1.0)
2. Загрузите нужный исполняемый файл
3. Запустите файл `.exe`

### Метод 2: Ручная компиляция

```bash
# Установите PyInstaller
pip install pyinstaller

# Перейдите в каталог клиента
cd samp-client-v

# Скомпилируйте проект
pyinstaller samp-client-v.spec
```

## Важно

**Внимание:**
- **НЕ** компилируйте файл Python (`samp-client-v.py`)
- **ВСЕГДА** компилируйте с использованием соответствующего файла `.spec`
- Правильный пример компиляции: `pyinstaller samp-client-v.spec`

**Почему?**
Файл `.spec` содержит критически важные настройки:
- Включение статических файлов (значки, ZIP-файлы)
- Настройки значка исполняемого файла
- Определение дополнительных зависимостей и ресурсов

> [!WARNING]
> Прямая компиляция файла Python **ИСКЛЮЧИТ** важные ресурсы, такие как изображения и установочные файлы, если вы не добавите параметры `--add-data "samp-client-v.zip;."` и `--icon="ico-spc.ico"`.

## Доступные версии

1. `samp-client-r1`
2. `samp-client-r1-voip` с включенным SAMPVOICE
3. `samp-client-r2`
4. `samp-client-r3`
5. `samp-client-r3-voip` с включенным SAMPVOICE
6. `samp-client-r4`
7. `samp-client-r5`

## Технические детали

### Структура кода

#### Класс цветов

```python
@dataclass
class Client_Yadra:
    background: str = '#1E1E1E'
    primary: str = '#3B8AFF'
    secondary: str = '#2C2C2C'
    text_primary: str = '#FFFFFF'
    text_secondary: str = '#A0A0A0'
```

#### Метод создания стилизованной метки

```python
def Sozdat_Etiketku_Stilya(
    self, 
    roditel, 
    tekst: str, 
    shrift: tuple = ('Segoe UI', 12), 
    tsvet: Optional[str] = None
) -> ttk.Label:
    return ttk.Label(
        roditel, 
        text=tekst, 
        font=shrift,
        foreground=tsvet or self.tsveta.tekst_vtorichnyi
    )
```

### Основные методы

#### Проверка папки

```python
def Proverka_Zavershena():
    papka = self.vybrannaya_papka.get()
    
    # Проверки целостности папки
    if not os.path.exists(papka):
        Pokazat_Oshibku("Ошибка: Выбранная папка не существует.")
        return

    if os.path.basename(papka) != "Grand Theft Auto San Andreas":
        Pokazat_Oshibku("Ошибка: Неверная папка. Выберите правильную папку GTA San Andreas (Grand Theft Auto San Andreas).")
        return

    # Проверка исполняемого файла
    put_k_exe = os.path.join(papka, "gta_sa.exe")
    if not os.path.isfile(put_k_exe):
        Pokazat_Oshibku("Ошибка: Файл 'gta_sa.exe' не найден в папке.")
        return
```

#### Извлечение файлов

```python
def Ustanovka_Client():
    put_k_zipu = getattr(sys, "_MEIPASS", os.path.abspath("."))
    fayl_zip = os.path.join(put_k_zipu, "archives", "samp-client-v.zip")
    
    papka_naznacheniya = self.vybrannaya_papka.get()

    with zipfile.ZipFile(fayl_zip, 'r') as zip_ref:
        fayli = zip_ref.namelist()
        vsego_faylov = len(fayli)
        
        for i, fayl in enumerate(fayli, start=1):
            # Индикатор выполнения и обновление статуса
            fayl_label.config(text=f"Извлечение: {os.path.basename(fayl)}")
            progress_bar['value'] = (i / vsego_faylov) * 100
            self.koren.update_idletasks()
            
            zip_ref.extract(fayl, papka_naznacheniya)
            self.izvlechennye_fayli.append(fayl)
```

## Настройки PyInstaller

### Пример файла Spec

```python
datas = [
    ('archives/samp-client-v.zip', 'archives'),
    ('icons/spc.png', 'icons'),
    ('icons/youtube.png', 'icons'),
    # Другие статические файлы
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

### Важные настройки

- `datas`: Определяет дополнительные включаемые файлы
- `name`: Имя итогового исполняемого файла
- `icon`: Пользовательский значок для исполняемого файла
- `console=False`: Скрывает консольное окно
