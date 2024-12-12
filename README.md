# clients-samp

## 🌍

- **English** > [README](https://github.com/spc-samp/clients-samp/tree/English).
- **Español** > [README](https://github.com/spc-samp/clients-samp/tree/Espanol).
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
  - [Introdução](#introdução)
  - [Estrutura do Projeto](#estrutura-do-projeto)
  - [Dependências](#dependências)
    - [Instalação das Dependências](#instalação-das-dependências)
    - [Dependências Detalhadas](#dependências-detalhadas)
  - [Instalação](#instalação)
    - [Método 1: Executável Pré-Compilado](#método-1-executável-pré-compilado)
    - [Método 2: Compilação Manual](#método-2-compilação-manual)
  - [Importante](#importante)
  - [Versões Disponíveis](#versões-disponíveis)
  - [Detalhes Técnicos](#detalhes-técnicos)
    - [Estrutura do Código](#estrutura-do-código)
      - [Classe de Cores](#classe-de-cores)
      - [Método de Criação de Label Estilizado](#método-de-criação-de-label-estilizado)
    - [Métodos Fundamentais](#métodos-fundamentais)
      - [Verificação de Pasta](#verificação-de-pasta)
      - [Extração de Arquivos](#extração-de-arquivos)
  - [Configurações do PyInstaller](#configurações-do-pyinstaller)
    - [Exemplo de Arquivo Spec](#exemplo-de-arquivo-spec)
    - [Configurações Importantes](#configurações-importantes)

## Introdução

O projeto **clients-samp** é um conjunto de instaladores para o mod SA:MP (San Andreas Multiplayer), desenvolvido para simplificar a instalação e configuração do client de jogo.

## Estrutura do Projeto

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

Cada versão do client segue uma estrutura de diretório padrão:

```
samp-client-rx/
│
├── archives/
│   └── samp-client-v.zip      # Arquivos compactados para instalação
│
├── icons/                      # Ícones e imagens do instalador
│   ├── spc.png
│   ├── discord.png
│   └── ...
│
├── samp-client-v.py           # Script principal em Python
└── samp-client-v.spec         # Configuração do PyInstaller
```

## Dependências

### Instalação das Dependências

```bash
pip install pillow
pip install sv-ttk
```

### Dependências Detalhadas

| Biblioteca | Versão Recomendada | Propósito |
|-----------|---------------------|-----------|
| `tkinter` | Padrão do Python | Interface gráfica |
| `PIL` (Pillow) | 9.5.0+ | Processamento de imagens |
| `sv_ttk` | 2.0.0+ | Tema moderno para Tkinter |
| `threading` | Padrão do Python | Processamento assíncrono |
| `zipfile` | Padrão do Python | Extração de arquivos |
| `webbrowser` | Padrão do Python | Abertura de links externos |

## Instalação

### Método 1: Executável Pré-Compilado

1. Acesse a seção de [releases](https://github.com/spc-samp/clients-samp/releases/tag/pt-1.0)
2. Baixe o executável que você quer
3. Execute o arquivo `.exe`

### Método 2: Compilação Manual

```bash
# Instale o PyInstaller
pip install pyinstaller

# Navegue até o diretório do client
cd samp-client-rx

# Compile o projeto
pyinstaller samp-client-v.spec
```

## Importante

**Atenção:** 
- **NÃO** compile o arquivo Python (`samp-client-v.py`)
- **SEMPRE** compile usando o arquivo `.spec` correspondente
- Exemplo correto de compilação: `pyinstaller samp-client-v.spec`

**Por quê?**
O arquivo `.spec` contém configurações cruciais:
- Inclusão de arquivos estáticos (ícones, arquivos ZIP)
- Configurações de ícone do executável
- Definição de dependências e recursos adicionais
- 
> [!WARNING]
> A compilação direta do arquivo Python **EXCLUIRÁ** recursos essenciais como imagens e arquivos de instalação, a não ser que você adicione os parâmetros `--add-data "samp-client-v.zip;."` e `--icon="ico-spc.ico"`.

## Versões Disponíveis

1. `samp-client-r1`
2. `samp-client-r1-voip` SAMPVOICE incluso
3. `samp-client-r2`
4. `samp-client-r3`
5. `samp-client-r3-voip` SAMPVOICE incluso
6. `samp-client-r4`
7. `samp-client-r5`

## Detalhes Técnicos

### Estrutura do Código

#### Classe de Cores

```python
@dataclass
class Client_Cores:
    background: str = '#1E1E1E'
    primary: str = '#3B8AFF'
    secondary: str = '#2C2C2C'
    text_primary: str = '#FFFFFF'
    text_secondary: str = '#A0A0A0'
```

#### Método de Criação de Label Estilizado

```python
def CriarLabel_Estilizado(
    self, 
    parent, 
    texto: str, 
    fonte: tuple = ('Segoe UI', 12), 
    cor: Optional[str] = None
) -> ttk.Label:
    return ttk.Label(
        parent, 
        text=texto, 
        font=fonte,
        foreground=cor or self.colors.text_secondary
    )
```

### Métodos Fundamentais

#### Verificação de Pasta

```python
def Verificacao_Completa(self):
    pasta = self.pasta_selecionada.get()
    
    # Verificações de integridade da pasta
    if not os.path.exists(pasta):
        Exibir_Erro("Erro: A pasta selecionada não existe.")
        return

    if os.path.basename(pasta) != "Grand Theft Auto San Andreas":
        Exibir_Erro("Erro: Pasta inválida.")
        return

    # Verificação do executável
    caminho_exe = os.path.join(pasta, "gta_sa.exe")
    if not os.path.isfile(caminho_exe):
        Exibir_Erro("Erro: Arquivo 'gta_sa.exe' não encontrado.")
        return
```

#### Extração de Arquivos

```python
def Instalacao_Client(self):
    caminho_zip = getattr(sys, "_MEIPASS", os.path.abspath("."))
    arquivo_zip = os.path.join(caminho_zip, "archives", "samp-client-x.zip")
    
    pasta_destino = self.pasta_selecionada.get()

    with zipfile.ZipFile(arquivo_zip, 'r') as zip_ref:
        arquivos = zip_ref.namelist()
        total_arquivos = len(arquivos)
        
        for i, arquivo in enumerate(arquivos, start=1):
            # Barra de progresso e atualização de status
            arquivo_label.config(text=f"Extraindo: {os.path.basename(arquivo)}")
            barra_progresso['value'] = (i / total_arquivos) * 100
            
            zip_ref.extract(arquivo, pasta_destino)
            self.arquivos_extraidos.append(arquivo)
```

## Configurações do PyInstaller

### Exemplo de Arquivo Spec

```python
datas = [
    ('archives/samp-client-v.zip', 'archives'),
    ('icons/spc.png', 'icons'),
    ('icons/youtube.png', 'icons'),
    # Outros arquivos estáticos
]

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='samp-client-x',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon='icons/ico-spc.ico',
)
```

### Configurações Importantes

- `datas`: Define arquivos adicionais a serem incluídos
- `name`: Nome do executável final
- `icon`: Ícone personalizado para o executável
- `console=False`: Oculta janela de console
