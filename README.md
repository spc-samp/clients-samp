# clients-samp

## 🌍

- **Português** > [README](https://github.com/spc-samp/clients-samp).
- **English** > [README](https://github.com/spc-samp/clients-samp/tree/English).
- **Español** > [README](https://github.com/spc-samp/clients-samp/tree/Espanol).
- **Polski** > [README](https://github.com/spc-samp/clients-samp/tree/Polski).
- **Türk** > [README](https://github.com/spc-samp/clients-samp/tree/Turk).
- **Deutsch** > [README](https://github.com/spc-samp/clients-samp/tree/Deutsch).
- **Русский** > [README](https://github.com/spc-samp/clients-samp/tree/Русский).
- **Italiano** > [README](https://github.com/spc-samp/clients-samp/tree/Italiano).
- **Svensk** > [README](https://github.com/spc-samp/clients-samp/tree/Svensk).

## Table des Matières

- [clients-samp](#clients-samp)
  - [🌍](#)
  - [Table des Matières](#table-des-matières)
  - [Introduction](#introduction)
  - [Structure du Projet](#structure-du-projet)
  - [Dépendances](#dépendances)
    - [Installation des Dépendances](#installation-des-dépendances)
    - [Dépendances Détaillées](#dépendances-détaillées)
  - [Installation](#installation)
    - [Méthode 1: Exécutable Pré-Compilé](#méthode-1-exécutable-pré-compilé)
    - [Méthode 2: Compilation Manuelle](#méthode-2-compilation-manuelle)
  - [Important](#important)
  - [Versions Disponibles](#versions-disponibles)
  - [Détails Techniques](#détails-techniques)
    - [Structure du Code](#structure-du-code)
      - [Classe de Couleurs](#classe-de-couleurs)
      - [Méthode de Création d'un Label Stylisé](#méthode-de-création-dun-label-stylisé)
    - [Méthodes Fondamentales](#méthodes-fondamentales)
      - [Vérification de Dossier](#vérification-de-dossier)
      - [Extraction de Fichiers](#extraction-de-fichiers)
  - [Configuration de PyInstaller](#configuration-de-pyinstaller)
    - [Exemple de Fichier Spec](#exemple-de-fichier-spec)
    - [Configurations Importantes](#configurations-importantes)

## Introduction

Le projet **clients-samp** est un ensemble d'installateurs pour le mod SA:MP (San Andreas Multiplayer), développé pour simplifier l'installation et la configuration du client de jeu.

## Structure du Projet

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

Chaque version du client suit une structure de répertoire standard:

```
samp-client-v/
│
├── archives/
│   └── samp-client-v.zip      # Fichiers compressés pour l'installation
│
├── icons/                      # Icônes et images de l'installateur
│   ├── spc.png
│   ├── discord.png
│   └── ...
│
├── samp-client-v.py           # Script principal en Python
└── samp-client-v.spec         # Configuration de PyInstaller
```

## Dépendances

### Installation des Dépendances

```bash
pip install pillow
pip install sv-ttk
```

### Dépendances Détaillées

| Bibliothèque | Version Recommandée | Objectif |
|-------------|---------------------|----------|
| `tkinter` | Défaut de Python | Interface graphique |
| `PIL` (Pillow) | 9.5.0+ | Traitement d'images |
| `sv_ttk` | 2.0.0+ | Thème moderne pour Tkinter |
| `threading` | Défaut de Python | Traitement asynchrone |
| `zipfile` | Défaut de Python | Extraction de fichiers |
| `webbrowser` | Défaut de Python | Ouverture de liens externes |

## Installation

### Méthode 1: Exécutable Pré-Compilé

1. Accédez à la section [releases](https://github.com/spc-samp/clients-samp/releases/tag/fr-1.0)
2. Téléchargez l'exécutable souhaité
3. Exécutez le fichier `.exe`

### Méthode 2: Compilation Manuelle

```bash
# Installez PyInstaller
pip install pyinstaller

# Naviguez vers le répertoire du client
cd samp-client-v

# Compilez le projet
pyinstaller samp-client-v.spec
```

## Important

**Attention:** 
- **NE PAS** compiler directement le fichier Python (`samp-client-v.py`)
- **TOUJOURS** compiler en utilisant le fichier `.spec` correspondant
- Exemple de compilation correct: `pyinstaller samp-client-v.spec`

**Pourquoi ?**
Le fichier `.spec` contient des configurations cruciales:
- Inclusion de fichiers statiques (icônes, fichiers ZIP)
- Configurations de l'icône de l'exécutable
- Définition des dépendances et ressources supplémentaires

> [!WARNING]
> La compilation directe du fichier Python **EXCLURA** des ressources essentielles comme des images et des fichiers d'installation, sauf si vous ajoutez les paramètres `--add-data "samp-client-v.zip;."` et `--icon="ico-spc.ico"`.

## Versions Disponibles

1. `samp-client-r1`
2. `samp-client-r1-voip` SAMPVOICE inclus
3. `samp-client-r2`
4. `samp-client-r3`
5. `samp-client-r3-voip` SAMPVOICE inclus
6. `samp-client-r4`
7. `samp-client-r5`

## Détails Techniques

### Structure du Code

#### Classe de Couleurs

```python
@dataclass
class Client_Couleurs:
    background: str = '#1E1E1E'
    primary: str = '#3B8AFF'
    secondary: str = '#2C2C2C'
    text_primary: str = '#FFFFFF'
    text_secondary: str = '#A0A0A0'
```

#### Méthode de Création d'un Label Stylisé

```python
def Creer_Bouton_Stylise(
    self, 
    parent, 
    texte: str, 
    commande: Callable, 
    style: str = 'Accent.TButton'
) -> ttk.Button:
    return ttk.Button(
        parent, 
        text=texte, 
        command=commande,
        style=style
    )
```

### Méthodes Fondamentales

#### Vérification de Dossier

```python
def Verification_Complete():
    dossier = self.dossier_selectionne.get()
    
    # Vérifications d'intégrité du dossier
    if not os.path.exists(dossier):
        Afficher_Erreur("Erreur: Le dossier sélectionné n'existe pas.")
        return

    if os.path.basename(dossier) != "Grand Theft Auto San Andreas":
        Afficher_Erreur("Erreur: Dossier invalide. Sélectionnez le dossier correct de GTA San Andreas (Grand Theft Auto San Andreas).")
        return

    # Vérification de l'exécutable
    chemin_exe = os.path.join(dossier, "gta_sa.exe")
    if not os.path.isfile(chemin_exe):
        Afficher_Erreur("Erreur: Le fichier 'gta_sa.exe' n'a pas été trouvé dans le dossier.")
        return
```

#### Extraction de Fichiers

```python
def Installation_Client():
    chemin_zip = getattr(sys, "_MEIPASS", os.path.abspath("."))
    fichier_zip = os.path.join(chemin_zip, "archives", "samp-client-v.zip")
    
    dossier_destination = self.dossier_selectionne.get()

    with zipfile.ZipFile(fichier_zip, 'r') as zip_ref:
        fichiers = zip_ref.namelist()
        total_fichiers = len(fichiers)
        
        for i, fichier in enumerate(fichiers, start=1):
            # Barre de progression et mise à jour du statut
            label_fichier.config(text=f"Extraction: {os.path.basename(fichier)}")
            barre_progression['value'] = (i / total_fichiers) * 100
            self.root.update_idletasks()
            
            zip_ref.extract(fichier, dossier_destination)
            self.fichiers_extraits.append(fichier)
```

## Configuration de PyInstaller

### Exemple de Fichier Spec

```python
datas = [
    ('archives/samp-client-v.zip', 'archives'),
    ('icons/spc.png', 'icons'),
    ('icons/youtube.png', 'icons'),
    # Autres fichiers statiques
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

### Configurations Importantes

- `datas`: Définit les fichiers supplémentaires à inclure
- `name`: Nom de l'exécutable final
- `icon`: Icône personnalisée pour l'exécutable
- `console=False`: Masque la fenêtre de console
