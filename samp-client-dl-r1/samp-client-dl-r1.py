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
class Client_Colori:
    background: str = '#1E1E1E'
    primary: str = '#3B8AFF'
    secondary: str = '#2C2C2C'
    text_primary: str = '#FFFFFF'
    text_secondary: str = '#A0A0A0'

class Samp_Client_DL_R1:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.Configurare_Radice()
        self.colors = Client_Colori()
        self.cartella_selezionata = tk.StringVar(value="Nessuna cartella ancora selezionata")
        self.file_estratti = []
        self.Configurare_Tema()
        self.Creare_Interfaccia_Iniziale()
        self.Configurare_IconaFinestra()

    def Configurare_IconaFinestra(self):
        base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
        icon_path = os.path.join(base_path, "icons", "spc.png")

        img = Image.open(icon_path)
        icon = ImageTk.PhotoImage(img)
        self.root.iconphoto(True, icon)

    def Configurare_Radice(self):
        self.root.title("Client DL R1 - SPC")
        self.root.geometry("700x500")
        self.root.resizable(True, True)

    def Configurare_Tema(self):
        sv_ttk.set_theme("dark")
        self.root.configure(bg=self.colors.background)

    def Pulire_Finestra(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def Creare_Etichetta_Stilizzata(
        self, 
        parent, 
        testo: str, 
        fonte: tuple = ('Segoe UI', 12), 
        colore: Optional[str] = None
    ) -> ttk.Label:
        return ttk.Label(
            parent, 
            text=testo, 
            font=fonte,
            foreground=colore or self.colors.text_secondary
        )

    def Creare_Bottone_Stilizzato(
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

    def Creare_Interfaccia_Iniziale(self):
        self.Pulire_Finestra()
        
        quadro_principale = ttk.Frame(self.root, padding="30 30 30 30")
        quadro_principale.pack(fill=tk.BOTH, expand=True)
        
        titolo = self.Creare_Etichetta_Stilizzata(
            quadro_principale, 
            "Installatore Client DL R1 SA:MP", 
            fonte=('Segoe UI', 20, 'bold'), 
            colore=self.colors.primary
        )
        titolo.pack(pady=(0, 30))
        
        sottotitolo = self.Creare_Etichetta_Stilizzata(
            quadro_principale, 
            "Installatore del mod SA:MP (San Andreas Multiplayer), versione 0.3 DL R1"
        )
        sottotitolo.pack(pady=(0, 20))
        
        frame_cartella = ttk.Frame(quadro_principale)
        frame_cartella.pack(fill=tk.X, pady=10)
        
        etichetta_cartella = ttk.Label(
            frame_cartella, 
            textvariable=self.cartella_selezionata, 
            font=('Consolas', 10), 
            wraplength=500,
            foreground=self.colors.text_primary
        )
        etichetta_cartella.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 10))
        
        bottone_seleziona = self.Creare_Bottone_Stilizzato(
            frame_cartella, 
            "Seleziona Cartella", 
            self.Scegliere_Cartella
        )
        bottone_seleziona.pack(side=tk.RIGHT)

    def Scegliere_Cartella(self):
        cartella = filedialog.askdirectory(
            title="Seleziona la cartella Grand Theft Auto San Andreas",
            initialdir=os.path.expanduser("~")
        )
        
        if cartella:
            self.cartella_selezionata.set(cartella)
            self.Creare_Interfaccia_VerificaCartellaCartella()

    def Creare_Interfaccia_VerificaCartellaCartella(self):
        self.Pulire_Finestra()
        
        quadro_principale = ttk.Frame(self.root, padding="30 30 30 30")
        quadro_principale.pack(fill=tk.BOTH, expand=True)
        
        titolo = self.Creare_Etichetta_Stilizzata(
            quadro_principale, 
            "Verificando Cartella", 
            fonte=('Segoe UI', 16, 'bold'), 
            colore=self.colors.primary
        )
        titolo.pack(pady=(0, 20))
        
        etichetta_stato = self.Creare_Etichetta_Stilizzata(
            quadro_principale, 
            "Verificando se questa e la cartella corretta del tuo GTA..."
        )
        etichetta_stato.pack(pady=20)
        
        etichetta_errore = ttk.Label(
            quadro_principale, 
            text="", 
            foreground="red", 
            font=('Segoe UI', 10)
        )
        etichetta_errore.pack(pady=10)
        
        barra_progresso = ttk.Progressbar(
            quadro_principale, 
            length=600, 
            mode='determinate', 
            maximum=100
        )
        barra_progresso.pack(pady=20)

        def Verifica_Completata():
            cartella = self.cartella_selezionata.get()
            
            for i in range(101):
                barra_progresso['value'] = i
                self.root.update_idletasks()
                time.sleep(0.05)
            
            def Mostra_Errore(messaggio):
                etichetta_errore.config(text=messaggio)
                bottone_riprova.pack()
            
            if not os.path.exists(cartella):
                Mostra_Errore("Errore: La cartella selezionata non esiste.")
                return

            if os.path.basename(cartella) != "Grand Theft Auto San Andreas":
                Mostra_Errore("Errore: Cartella non valida. Seleziona la cartella corretta di GTA San Andreas (Grand Theft Auto San Andreas).")
                return

            percorso_exe = os.path.join(cartella, "gta_sa.exe")
            if not os.path.isfile(percorso_exe):
                Mostra_Errore("Errore: Il file 'gta_sa.exe' non e stato trovato nella cartella.")
                return
            
            self.root.after(0, self.Creare_Interfaccia_ConfermaClient)

        def Riprova():
            bottone_riprova.pack_forget()
            etichetta_errore.config(text="")
            self.Creare_Interfaccia_Iniziale()

        bottone_riprova = self.Creare_Bottone_Stilizzato(
            quadro_principale, 
            "Riprova", 
            Riprova
        )

        threading.Thread(target=Verifica_Completata, daemon=True).start()

    def Creare_Interfaccia_ConfermaClient(self):
        self.Pulire_Finestra()
        
        quadro_principale = ttk.Frame(self.root, padding="30 30 30 30")
        quadro_principale.pack(fill=tk.BOTH, expand=True)
        
        titolo = self.Creare_Etichetta_Stilizzata(
            quadro_principale, 
            "Installa Client", 
            fonte=('Segoe UI', 16, 'bold'), 
            colore=self.colors.primary
        )
        titolo.pack(pady=(0, 20))
        
        sottotitolo = self.Creare_Etichetta_Stilizzata(
            quadro_principale, 
            "Cartella verificata con successo. Vuoi procedere con l'installazione\ndel Client DL R1?"
        )
        sottotitolo.pack(pady=20)
        
        frame_bottoni = ttk.Frame(quadro_principale)
        frame_bottoni.pack(pady=20)
        
        bottone_procedi = self.Creare_Bottone_Stilizzato(
            frame_bottoni, 
            "Procedi", 
            self.Iniziare_Installazione_Client, 
            'Accent.TButton'
        )
        bottone_procedi.pack(side=tk.LEFT, padx=10)
        
        bottone_annulla = self.Creare_Bottone_Stilizzato(
            frame_bottoni, 
            "Annulla", 
            self.Annullare_Installazione
        )
        bottone_annulla.pack(side=tk.LEFT, padx=10)

    def Iniziare_Installazione_Client(self):
        self.Pulire_Finestra()
        
        quadro_principale = ttk.Frame(self.root, padding="30 30 30 30")
        quadro_principale.pack(fill=tk.BOTH, expand=True)
        
        titolo = self.Creare_Etichetta_Stilizzata(
            quadro_principale, 
            "Installando Client DL R1", 
            fonte=('Segoe UI', 16, 'bold'), 
            colore=self.colors.primary
        )
        titolo.pack(pady=(0, 20))
        
        etichetta_stato = self.Creare_Etichetta_Stilizzata(
            quadro_principale, 
            "Installazione in corso, attendere..."
        )
        etichetta_stato.pack(pady=20)
        
        barra_progresso = ttk.Progressbar(
            quadro_principale, 
            length=600, 
            mode='determinate', 
            maximum=100
        )
        barra_progresso.pack(pady=20)
        
        etichetta_file = ttk.Label(
            quadro_principale, 
            text="", 
            font=('Consolas', 10),
            foreground=self.colors.text_primary
        )
        etichetta_file.pack(pady=10)

        def Installazione_Client():
            percorso_zip = getattr(sys, "_MEIPASS", os.path.abspath("."))
            file_zip = os.path.join(percorso_zip, "archives", "samp-client-dl-r1.zip")
            
            cartella_destinazione = self.cartella_selezionata.get()

            with zipfile.ZipFile(file_zip, 'r') as zip_ref:
                file = zip_ref.namelist()
                totale_file = len(file)
                
                for i, file_singolo in enumerate(file, start=1):
                    etichetta_file.config(text=f"Estraendo: {os.path.basename(file_singolo)}")
                    barra_progresso['value'] = (i / totale_file) * 100
                    self.root.update_idletasks()
                    
                    zip_ref.extract(file_singolo, cartella_destinazione)
                    self.file_estratti.append(file_singolo)
                    time.sleep(0.1)
            
            etichetta_file.config(text="Installazione completata!")
            barra_progresso['value'] = 100
            self.root.update_idletasks()
            time.sleep(1)
            
            self.root.after(0, self.Mostrare_RiepilogoInstallazione)
        
        threading.Thread(target=Installazione_Client, daemon=True).start()

    def Mostrare_RiepilogoInstallazione(self):
        self.Pulire_Finestra()
        
        quadro_principale = ttk.Frame(self.root, padding="30 30 30 30")
        quadro_principale.pack(fill=tk.BOTH, expand=True)
        
        titolo = self.Creare_Etichetta_Stilizzata(
            quadro_principale, 
            "File Estratti", 
            fonte=('Segoe UI', 16, 'bold'), 
            colore=self.colors.primary
        )
        titolo.pack(pady=(0, 20))
        
        frame_scorrimento = ttk.Frame(quadro_principale)
        frame_scorrimento.pack(fill=tk.BOTH, expand=True, pady=20)
        
        canvas = tk.Canvas(frame_scorrimento)
        scrollbar = ttk.Scrollbar(frame_scorrimento, orient="vertical", command=canvas.yview)
        frame_scorrevole = ttk.Frame(canvas)

        frame_scorrevole.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=frame_scorrevole, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        for file in self.file_estratti:
            etichetta_file = ttk.Label(
                frame_scorrevole, 
                text=file, 
                font=('Consolas', 10)
            )
            etichetta_file.pack(anchor='w', padx=10, pady=2)
        
        bottone_completato = self.Creare_Bottone_Stilizzato(
            quadro_principale, 
            "Completato", 
            self.Creare_Interfaccia_Social, 
            'Accent.TButton'
        )
        bottone_completato.pack(pady=20)

    def Creare_Interfaccia_Social(self):
        self.Pulire_Finestra()
        
        quadro_principale = ttk.Frame(self.root, padding="30 30 30 30")
        quadro_principale.pack(fill=tk.BOTH, expand=True)
        
        titolo = self.Creare_Etichetta_Stilizzata(
            quadro_principale, 
            "Social", 
            fonte=('Segoe UI', 24, 'bold'), 
            colore=self.colors.primary
        )
        titolo.pack(pady=(0, 40))
        
        links_sociali = [
            (" Discord SPC", "https://discord.gg/3fApZh66Tf", "discord.png"),
            (" Instagram", "https://www.instagram.com/spc.samp/", "instagram.png"),
            (" YouTube", "https://www.youtube.com/@spc-samp", "youtube.png"),
            (" TikTok", "https://www.tiktok.com/@spc.samp", "tiktok.png"),
            (" GitHub", "https://github.com/spc-samp", "github.png"),
        ]
        
        frame_bottoni = ttk.Frame(quadro_principale)
        frame_bottoni.pack(expand=True)
        
        def Aprire_Link(link):
            webbrowser.open(link, new=2)
        
        def ridimensionare_icona(percorso_icona, dimensione=(30, 30)):
            base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
            percorso_completo = os.path.join(base_path, percorso_icona)
            
            immagine = Image.open(percorso_completo)
            immagine_ridimensionata = immagine.resize(dimensione, Image.LANCZOS)
            return ImageTk.PhotoImage(immagine_ridimensionata)
        
        for i in range(0, len(links_sociali), 2):
            frame_riga = ttk.Frame(frame_bottoni)
            frame_riga.pack(fill=tk.X, pady=10)
            
            for j in range(2):
                if i + j < len(links_sociali):
                    nome, link, percorso_icona = links_sociali[i + j]
                    
                    icona = ridimensionare_icona(os.path.join('icons', percorso_icona))
                    
                    bottone_sociale = ttk.Button(
                        frame_riga, 
                        text=nome, 
                        image=icona, 
                        compound=tk.LEFT,
                        command=lambda l=link: Aprire_Link(l)
                    )
                    bottone_sociale.image = icona
                    bottone_sociale.pack(side=tk.LEFT, padx=10, expand=True, fill=tk.X)
        
        bottone_chiusura = ttk.Button(
            frame_bottoni, 
            text="Chiudi", 
            command=self.root.quit,
            style='Chiudi.TButton'
        )
        bottone_chiusura.pack(pady=10, padx=20, fill=tk.X)

        style = ttk.Style()
        style.configure(
            'Chiudi.TButton', 
            background='red', 
            foreground='white', 
            font=('Segoe UI', 12)
        )

    def Annullare_Installazione(self):
        self.Pulire_Finestra()
        
        quadro_principale = ttk.Frame(self.root, padding="30 30 30 30")
        quadro_principale.pack(fill=tk.BOTH, expand=True)
        
        titolo = self.Creare_Etichetta_Stilizzata(
            quadro_principale, 
            "Annullando Installazione", 
            fonte=('Segoe UI', 16, 'bold'), 
            colore=self.colors.primary
        )
        titolo.pack(pady=(0, 20))
        
        etichetta_stato = self.Creare_Etichetta_Stilizzata(
            quadro_principale, 
            "Attendere, tutte le operazioni verranno annullate..."
        )
        etichetta_stato.pack(pady=20)
        
        barra_progresso = ttk.Progressbar(
            quadro_principale, 
            length=600, 
            mode='determinate', 
            maximum=100
        )
        barra_progresso.pack(pady=20)

        def Annullamento():
            for i in range(101):
                barra_progresso['value'] = i
                self.root.update_idletasks()
                time.sleep(0.05)
            
            self.root.after(0, self.Creare_Interfaccia_Social)

        threading.Thread(target=Annullamento, daemon=True).start()

def main_client():
    root = tk.Tk()
    Samp_Client_DL_R1(root)
    root.mainloop()

if __name__ == "__main__":
    main_client()
