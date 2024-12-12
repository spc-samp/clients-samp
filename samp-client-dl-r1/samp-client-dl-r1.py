from PIL import Image, ImageTk
import os
import sys
import zipfile
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading
import time
import sv_ttk
from dataclasses import dataclass
from typing import Dict, Optional, Callable
import webbrowser

@dataclass
class Client_Cores:
    background: str = '#1E1E1E'
    primary: str = '#3B8AFF'
    secondary: str = '#2C2C2C'
    text_primary: str = '#FFFFFF'
    text_secondary: str = '#A0A0A0'

class Samp_Client_DL_R1:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.Configurar_Raiz()
        self.colors = Client_Cores()
        self.pasta_selecionada = tk.StringVar(value="Nenhuma pasta foi selecionada, ainda")
        self.arquivos_extraidos = []
        self.Configurar_Tema()
        self.CriarInterface_Inicial()
        self.Configurar_IconJanela()

    def Configurar_IconJanela(self):
        base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
        icon_path = os.path.join(base_path, "icons", "spc.png")

        img = Image.open(icon_path)
        icon = ImageTk.PhotoImage(img)
        self.root.iconphoto(True, icon)

    def Configurar_Raiz(self):
        self.root.title("Client DL R1 - SPC")
        self.root.geometry("700x500")
        self.root.resizable(True, True)

    def Configurar_Tema(self):
        sv_ttk.set_theme("dark")
        self.root.configure(bg=self.colors.background)

    def Limpar_Janela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

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

    def CriarBotao_Estilizado(
        self, 
        parent, 
        texto: str, 
        comando: Callable, 
        estilo: str = 'Accent.TButton'
    ) -> ttk.Button:
        return ttk.Button(
            parent, 
            text=texto, 
            command=comando,
            style=estilo
        )

    def CriarInterface_Inicial(self):
        self.Limpar_Janela()
        
        quadro_principal = ttk.Frame(self.root, padding="30 30 30 30")
        quadro_principal.pack(fill=tk.BOTH, expand=True)
        
        titulo = self.CriarLabel_Estilizado(
            quadro_principal, 
            "Instalador Client Dl R1 SA:MP", 
            fonte=('Segoe UI', 20, 'bold'), 
            cor=self.colors.primary
        )
        titulo.pack(pady=(0, 30))
        
        subtitulo = self.CriarLabel_Estilizado(
            quadro_principal, 
            "Instalador do mod SA:MP (San Andreas Multiplayer), versão 0.3.7 DL R1"
        )
        subtitulo.pack(pady=(0, 20))
        
        frame_pasta = ttk.Frame(quadro_principal)
        frame_pasta.pack(fill=tk.X, pady=10)
        
        pasta_label = ttk.Label(
            frame_pasta, 
            textvariable=self.pasta_selecionada, 
            font=('Consolas', 10), 
            wraplength=500,
            foreground=self.colors.text_primary
        )
        pasta_label.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 10))
        
        botao_selecionar = self.CriarBotao_Estilizado(
            frame_pasta, 
            "Selecionar Pasta", 
            self.Escolher_Pasta
        )
        botao_selecionar.pack(side=tk.RIGHT)

    def Escolher_Pasta(self):
        pasta = filedialog.askdirectory(
            title="Selecione a pasta Grand Theft Auto San Andreas",
            initialdir=os.path.expanduser("~")
        )
        
        if pasta:
            self.pasta_selecionada.set(pasta)
            self.CriarInterface_VerificacaoPasta()

    def CriarInterface_VerificacaoPasta(self):
        self.Limpar_Janela()
        
        quadro_principal = ttk.Frame(self.root, padding="30 30 30 30")
        quadro_principal.pack(fill=tk.BOTH, expand=True)
        
        titulo = self.CriarLabel_Estilizado(
            quadro_principal, 
            "Verificando Pasta", 
            fonte=('Segoe UI', 16, 'bold'), 
            cor=self.colors.primary
        )
        titulo.pack(pady=(0, 20))
        
        status_label = self.CriarLabel_Estilizado(
            quadro_principal, 
            "Verificando se esta é a pasta correta do seu GTA..."
        )
        status_label.pack(pady=20)
        
        erro_label = ttk.Label(
            quadro_principal, 
            text="", 
            foreground="red", 
            font=('Segoe UI', 10)
        )
        erro_label.pack(pady=10)
        
        barra_progresso = ttk.Progressbar(
            quadro_principal, 
            length=600, 
            mode='determinate', 
            maximum=100
        )
        barra_progresso.pack(pady=20)

        def Verificacao_Completa():
            pasta = self.pasta_selecionada.get()
            
            for i in range(101):
                barra_progresso['value'] = i
                self.root.update_idletasks()
                time.sleep(0.05)
            
            def Exibir_Erro(mensagem):
                erro_label.config(text=mensagem)
                botao_tentar_novamente.pack()
            
            if not os.path.exists(pasta):
                Exibir_Erro("Erro: A pasta selecionada não existe.")
                return

            if os.path.basename(pasta) != "Grand Theft Auto San Andreas":
                Exibir_Erro("Erro: Pasta inválida. Selecione a pasta correta do GTA San Andreas (Grand Theft Auto San Andreas).")
                return

            caminho_exe = os.path.join(pasta, "gta_sa.exe")
            if not os.path.isfile(caminho_exe):
                Exibir_Erro("Erro: O arquivo 'gta_sa.exe' não foi encontrado na pasta.")
                return
            
            self.root.after(0, self.CriarInterface_ConfirmacaoClient)

        def Tentar_Novamente():
            botao_tentar_novamente.pack_forget()
            erro_label.config(text="")
            self.CriarInterface_Inicial()

        botao_tentar_novamente = self.CriarBotao_Estilizado(
            quadro_principal, 
            "Tentar Novamente", 
            Tentar_Novamente
        )

        threading.Thread(target=Verificacao_Completa, daemon=True).start()

    def CriarInterface_ConfirmacaoClient(self):
        self.Limpar_Janela()
        
        quadro_principal = ttk.Frame(self.root, padding="30 30 30 30")
        quadro_principal.pack(fill=tk.BOTH, expand=True)
        
        titulo = self.CriarLabel_Estilizado(
            quadro_principal, 
            "Instalar Client", 
            fonte=('Segoe UI', 16, 'bold'), 
            cor=self.colors.primary
        )
        titulo.pack(pady=(0, 20))
        
        subtitulo = self.CriarLabel_Estilizado(
            quadro_principal, 
            "Pasta verificada com sucesso. Deseja prosseguir com a instalação\ndo Client DL R1?"
        )
        subtitulo.pack(pady=20)
        
        frame_botoes = ttk.Frame(quadro_principal)
        frame_botoes.pack(pady=20)
        
        botao_prosseguir = self.CriarBotao_Estilizado(
            frame_botoes, 
            "Prosseguir", 
            self.IniciarInstalacao_Client, 
            'Accent.TButton'
        )
        botao_prosseguir.pack(side=tk.LEFT, padx=10)
        
        botao_cancelar = self.CriarBotao_Estilizado(
            frame_botoes, 
            "Cancelar", 
            self.Cancelar_Instalacao
        )
        botao_cancelar.pack(side=tk.LEFT, padx=10)

    def IniciarInstalacao_Client(self):
        self.Limpar_Janela()
        
        quadro_principal = ttk.Frame(self.root, padding="30 30 30 30")
        quadro_principal.pack(fill=tk.BOTH, expand=True)
        
        titulo = self.CriarLabel_Estilizado(
            quadro_principal, 
            "Instalando Client DL R1", 
            fonte=('Segoe UI', 16, 'bold'), 
            cor=self.colors.primary
        )
        titulo.pack(pady=(0, 20))
        
        status_label = self.CriarLabel_Estilizado(
            quadro_principal, 
            "Instalando Client, aguarde..."
        )
        status_label.pack(pady=20)
        
        barra_progresso = ttk.Progressbar(
            quadro_principal, 
            length=600, 
            mode='determinate', 
            maximum=100
        )
        barra_progresso.pack(pady=20)
        
        arquivo_label = ttk.Label(
            quadro_principal, 
            text="", 
            font=('Consolas', 10),
            foreground=self.colors.text_primary
        )
        arquivo_label.pack(pady=10)

        def Instalacao_Client():
            caminho_zip = getattr(sys, "_MEIPASS", os.path.abspath("."))
            arquivo_zip = os.path.join(caminho_zip, "archives", "samp-client-dl-r1.zip")
            
            pasta_destino = self.pasta_selecionada.get()

            with zipfile.ZipFile(arquivo_zip, 'r') as zip_ref:
                arquivos = zip_ref.namelist()
                total_arquivos = len(arquivos)
                
                for i, arquivo in enumerate(arquivos, start=1):
                    arquivo_label.config(text=f"Extraindo: {os.path.basename(arquivo)}")
                    barra_progresso['value'] = (i / total_arquivos) * 100
                    self.root.update_idletasks()
                    
                    zip_ref.extract(arquivo, pasta_destino)
                    self.arquivos_extraidos.append(arquivo)
                    time.sleep(0.1)
            
            arquivo_label.config(text="Instalação concluída!")
            barra_progresso['value'] = 100
            self.root.update_idletasks()
            time.sleep(1)
            
            self.root.after(0, self.MostrarResumoInstalacao)
        
        threading.Thread(target=Instalacao_Client, daemon=True).start()

    def MostrarResumoInstalacao(self):
        self.Limpar_Janela()
        
        quadro_principal = ttk.Frame(self.root, padding="30 30 30 30")
        quadro_principal.pack(fill=tk.BOTH, expand=True)
        
        titulo = self.CriarLabel_Estilizado(
            quadro_principal, 
            "Arquivos Extraídos", 
            fonte=('Segoe UI', 16, 'bold'), 
            cor=self.colors.primary
        )
        titulo.pack(pady=(0, 20))
        
        frame_rolagem = ttk.Frame(quadro_principal)
        frame_rolagem.pack(fill=tk.BOTH, expand=True, pady=20)
        
        canvas = tk.Canvas(frame_rolagem)
        scrollbar = ttk.Scrollbar(frame_rolagem, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        for arquivo in self.arquivos_extraidos:
            label_arquivo = ttk.Label(
                scrollable_frame, 
                text=arquivo, 
                font=('Consolas', 10)
            )
            label_arquivo.pack(anchor='w', padx=10, pady=2)
        
        botao_concluido = self.CriarBotao_Estilizado(
            quadro_principal, 
            "Concluído", 
            self.CriarInterface_Sociais, 
            'Accent.TButton'
        )
        botao_concluido.pack(pady=20)

    def CriarInterface_Sociais(self):
        self.Limpar_Janela()
        
        quadro_principal = ttk.Frame(self.root, padding="30 30 30 30")
        quadro_principal.pack(fill=tk.BOTH, expand=True)
        
        titulo = self.CriarLabel_Estilizado(
            quadro_principal, 
            "Sociais", 
            fonte=('Segoe UI', 24, 'bold'), 
            cor=self.colors.primary
        )
        titulo.pack(pady=(0, 40))
        
        links_sociais = [
            (" Discord SPC", "https://discord.gg/3fApZh66Tf", "discord.png"),
            (" Instagram", "https://www.instagram.com/spc.samp/", "instagram.png"),
            (" YouTube", "https://www.youtube.com/@spc-samp", "youtube.png"),
            (" TikTok", "https://www.tiktok.com/@spc.samp", "tiktok.png"),
            (" GitHub", "https://github.com/spc-samp", "github.png"),
        ]
        
        frame_botoes = ttk.Frame(quadro_principal)
        frame_botoes.pack(expand=True)
        
        def Abrir_Link(link):
            webbrowser.open(link, new=2)
        
        def redimensionar_icone(caminho_icone, tamanho=(30, 30)):
            base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
            caminho_completo = os.path.join(base_path, caminho_icone)
            
            imagem = Image.open(caminho_completo)
            imagem_redimensionada = imagem.resize(tamanho, Image.LANCZOS)
            return ImageTk.PhotoImage(imagem_redimensionada)
        
        for i in range(0, len(links_sociais), 2):
            frame_linha = ttk.Frame(frame_botoes)
            frame_linha.pack(fill=tk.X, pady=10)
            
            for j in range(2):
                if i + j < len(links_sociais):
                    nome, link, icone_path = links_sociais[i + j]
                    
                    icone = redimensionar_icone(os.path.join('icons', icone_path))
                    
                    botao_social = ttk.Button(
                        frame_linha, 
                        text=nome, 
                        image=icone, 
                        compound=tk.LEFT,
                        command=lambda l=link: Abrir_Link(l)
                    )
                    botao_social.image = icone
                    botao_social.pack(side=tk.LEFT, padx=10, expand=True, fill=tk.X)
        
        botao_fechar = ttk.Button(
            frame_botoes, 
            text="Fechar", 
            command=self.root.quit,
            style='Fechar.TButton'
        )
        botao_fechar.pack(pady=10, padx=20, fill=tk.X)

        style = ttk.Style()
        style.configure(
            'Fechar.TButton', 
            background='red', 
            foreground='white', 
            font=('Segoe UI', 12)
        )

    def Cancelar_Instalacao(self):
        self.Limpar_Janela()
        
        quadro_principal = ttk.Frame(self.root, padding="30 30 30 30")
        quadro_principal.pack(fill=tk.BOTH, expand=True)
        
        titulo = self.CriarLabel_Estilizado(
            quadro_principal, 
            "Cancelando Instalação", 
            fonte=('Segoe UI', 16, 'bold'), 
            cor=self.colors.primary
        )
        titulo.pack(pady=(0, 20))
        
        status_label = self.CriarLabel_Estilizado(
            quadro_principal, 
            "Aguarde, toda a operação está sendo cancelada..."
        )
        status_label.pack(pady=20)
        
        barra_progresso = ttk.Progressbar(
            quadro_principal, 
            length=600, 
            mode='determinate', 
            maximum=100
        )
        barra_progresso.pack(pady=20)

        def Cancelamento():
            for i in range(101):
                barra_progresso['value'] = i
                self.root.update_idletasks()
                time.sleep(0.05)
            
            self.root.after(0, self.CriarInterface_Sociais)

        threading.Thread(target=Cancelamento, daemon=True).start()

def main_client():
    root = tk.Tk()
    Samp_Client_DL_R1(root)
    root.mainloop()

if __name__ == "__main__":
    main_client()