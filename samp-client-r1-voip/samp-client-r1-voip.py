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
class Client_Farger:
    background: str = '#1E1E1E'
    primary: str = '#3B8AFF'
    secondary: str = '#2C2C2C'
    text_primary: str = '#FFFFFF'
    text_secondary: str = '#A0A0A0'

class Samp_Client_R1_Voip:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.Konfigurera_Rot()
        self.colors = Client_Farger()
        self.vald_mapp = tk.StringVar(value="Ingen mapp har valts ännu")
        self.extraherade_filer = []
        self.Konfigurera_Tema()
        self.Skapa_Inledande_Granssnitt()
        self.Konfigurera_Fonsterikon()

    def Konfigurera_Fonsterikon(self):
        base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
        icon_path = os.path.join(base_path, "icons", "spc.png")

        img = Image.open(icon_path)
        icon = ImageTk.PhotoImage(img)
        self.root.iconphoto(True, icon)

    def Konfigurera_Rot(self):
        self.root.title("Client R1 Voip - SPC")
        self.root.geometry("700x500")
        self.root.resizable(True, True)

    def Konfigurera_Tema(self):
        sv_ttk.set_theme("dark")
        self.root.configure(bg=self.colors.background)

    def Rensa_Fonster(self):
        for widget in self.root.winfo_children():
            widget.destroy()

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

    def Skapa_Stiliserad_Knapp(
        self, 
        parent, 
        text: str, 
        kommando: Callable, 
        stil: str = 'Accent.TButton'
    ) -> ttk.Button:
        return ttk.Button(
            parent, 
            text=text, 
            command=kommando,
            style=stil
        )

    def Skapa_Inledande_Granssnitt(self):
        self.Rensa_Fonster()
        
        huvud_ram = ttk.Frame(self.root, padding="30 30 30 30")
        huvud_ram.pack(fill=tk.BOTH, expand=True)
        
        titel = self.Skapa_Stiliserad_Etikett(
            huvud_ram, 
            "Installationsprogram Client R1 Voip SA:MP", 
            font=('Segoe UI', 20, 'bold'), 
            color=self.colors.primary
        )
        titel.pack(pady=(0, 30))
        
        underrubrik = self.Skapa_Stiliserad_Etikett(
            huvud_ram, 
            "Installationsprogram for mod SA:MP (San Andreas Multiplayer), version 0.3.7 R1 Voip"
        )
        underrubrik.pack(pady=(0, 20))
        
        mapp_ram = ttk.Frame(huvud_ram)
        mapp_ram.pack(fill=tk.X, pady=10)
        
        mapp_etikett = ttk.Label(
            mapp_ram, 
            textvariable=self.vald_mapp, 
            font=('Consolas', 10), 
            wraplength=500,
            foreground=self.colors.text_primary
        )
        mapp_etikett.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 10))
        
        valj_mapp_knapp = self.Skapa_Stiliserad_Knapp(
            mapp_ram, 
            "Valj Mapp", 
            self.Valj_Mapp
        )
        valj_mapp_knapp.pack(side=tk.RIGHT)

    def Valj_Mapp(self):
        mapp = filedialog.askdirectory(
            title="Valj Grand Theft Auto San Andreas mapp",
            initialdir=os.path.expanduser("~")
        )
        
        if mapp:
            self.vald_mapp.set(mapp)
            self.Skapa_Granssnitt_Mappverifiering()

    def Skapa_Granssnitt_Mappverifiering(self):
        self.Rensa_Fonster()
        
        huvud_ram = ttk.Frame(self.root, padding="30 30 30 30")
        huvud_ram.pack(fill=tk.BOTH, expand=True)
        
        titel = self.Skapa_Stiliserad_Etikett(
            huvud_ram, 
            "Verifierar Mapp", 
            font=('Segoe UI', 16, 'bold'), 
            color=self.colors.primary
        )
        titel.pack(pady=(0, 20))
        
        status_etikett = self.Skapa_Stiliserad_Etikett(
            huvud_ram, 
            "Kontrollerar om detta ar ratt mapp for din GTA..."
        )
        status_etikett.pack(pady=20)
        
        fel_etikett = ttk.Label(
            huvud_ram, 
            text="", 
            foreground="red", 
            font=('Segoe UI', 10)
        )
        fel_etikett.pack(pady=10)
        
        framsteg_bar = ttk.Progressbar(
            huvud_ram, 
            length=600, 
            mode='determinate', 
            maximum=100
        )
        framsteg_bar.pack(pady=20)

        def Verifiering_Slutford():
            mapp = self.vald_mapp.get()
            
            for i in range(101):
                framsteg_bar['value'] = i
                self.root.update_idletasks()
                time.sleep(0.05)
            
            def Visa_Fel(meddelande):
                fel_etikett.config(text=meddelande)
                prova_igen_knapp.pack()
            
            if not os.path.exists(mapp):
                Visa_Fel("Fel: Den valda mappen finns inte.")
                return

            if os.path.basename(mapp) != "Grand Theft Auto San Andreas":
                Visa_Fel("Fel: Ogiltig mapp. Valj ratt mapp for GTA San Andreas (Grand Theft Auto San Andreas).")
                return

            exe_stig = os.path.join(mapp, "gta_sa.exe")
            if not os.path.isfile(exe_stig):
                Visa_Fel("Fel: Filen 'gta_sa.exe' hittades inte i mappen.")
                return
            
            self.root.after(0, self.Skapa_Granssnitt_Client_Bekraftelse)

        def Prova_Igen():
            prova_igen_knapp.pack_forget()
            fel_etikett.config(text="")
            self.Skapa_Inledande_Granssnitt()

        prova_igen_knapp = self.Skapa_Stiliserad_Knapp(
            huvud_ram, 
            "Prova Igen", 
            Prova_Igen
        )

        threading.Thread(target=Verifiering_Slutford, daemon=True).start()

    def Skapa_Granssnitt_Client_Bekraftelse(self):
        self.Rensa_Fonster()
        
        huvud_ram = ttk.Frame(self.root, padding="30 30 30 30")
        huvud_ram.pack(fill=tk.BOTH, expand=True)
        
        titel = self.Skapa_Stiliserad_Etikett(
            huvud_ram, 
            "Installera Client", 
            font=('Segoe UI', 16, 'bold'), 
            color=self.colors.primary
        )
        titel.pack(pady=(0, 20))
        
        underrubrik = self.Skapa_Stiliserad_Etikett(
            huvud_ram, 
            "Mappen verifierad. Vill du fortsatta med installationen\nav Client R1 Voip?"
        )
        underrubrik.pack(pady=20)
        
        knapp_ram = ttk.Frame(huvud_ram)
        knapp_ram.pack(pady=20)
        
        fortsatt_knapp = self.Skapa_Stiliserad_Knapp(
            knapp_ram, 
            "Fortsatt", 
            self.Starta_Client_Installation, 
            'Accent.TButton'
        )
        fortsatt_knapp.pack(side=tk.LEFT, padx=10)
        
        avbryt_knapp = self.Skapa_Stiliserad_Knapp(
            knapp_ram, 
            "Avbryt", 
            self.Avbryt_Installation
        )
        avbryt_knapp.pack(side=tk.LEFT, padx=10)

    def Starta_Client_Installation(self):
        self.Rensa_Fonster()
        
        huvud_ram = ttk.Frame(self.root, padding="30 30 30 30")
        huvud_ram.pack(fill=tk.BOTH, expand=True)
        
        titel = self.Skapa_Stiliserad_Etikett(
            huvud_ram, 
            "Installerar Client R1 Voip", 
            font=('Segoe UI', 16, 'bold'), 
            color=self.colors.primary
        )
        titel.pack(pady=(0, 20))
        
        status_etikett = self.Skapa_Stiliserad_Etikett(
            huvud_ram, 
            "Installerar Client, vara vanlig..."
        )
        status_etikett.pack(pady=20)
        
        framsteg_bar = ttk.Progressbar(
            huvud_ram, 
            length=600, 
            mode='determinate', 
            maximum=100
        )
        framsteg_bar.pack(pady=20)
        
        arkiv_etikett = ttk.Label(
            huvud_ram, 
            text="", 
            font=('Consolas', 10),
            foreground=self.colors.text_primary
        )
        arkiv_etikett.pack(pady=10)

        def Client_Installation():
            zip_stig = getattr(sys, "_MEIPASS", os.path.abspath("."))
            arkiv_zip = os.path.join(zip_stig, "archives", "samp-client-r1-voip.zip")
            
            mapp_destination = self.vald_mapp.get()

            with zipfile.ZipFile(arkiv_zip, 'r') as zip_ref:
                arkiv = zip_ref.namelist()
                total_arkiv = len(arkiv)
                
                for i, arkiv_item in enumerate(arkiv, start=1):
                    arkiv_etikett.config(text=f"Extraherar: {os.path.basename(arkiv_item)}")
                    framsteg_bar['value'] = (i / total_arkiv) * 100
                    self.root.update_idletasks()
                    
                    zip_ref.extract(arkiv_item, mapp_destination)
                    self.extraherade_filer.append(arkiv_item)
                    time.sleep(0.1)
            
            arkiv_etikett.config(text="Installation slutford!")
            framsteg_bar['value'] = 100
            self.root.update_idletasks()
            time.sleep(1)
            
            self.root.after(0, self.Visa_Installations_Sammanfattning)
        
        threading.Thread(target=Client_Installation, daemon=True).start()

    def Visa_Installations_Sammanfattning(self):
        self.Rensa_Fonster()
        
        huvud_ram = ttk.Frame(self.root, padding="30 30 30 30")
        huvud_ram.pack(fill=tk.BOTH, expand=True)
        
        titel = self.Skapa_Stiliserad_Etikett(
            huvud_ram, 
            "Extraherade Filer", 
            font=('Segoe UI', 16, 'bold'), 
            color=self.colors.primary
        )
        titel.pack(pady=(0, 20))
        
        rulle_ram = ttk.Frame(huvud_ram)
        rulle_ram.pack(fill=tk.BOTH, expand=True, pady=20)
        
        canvas = tk.Canvas(rulle_ram)
        scrollbar = ttk.Scrollbar(rulle_ram, orient="vertical", command=canvas.yview)
        rulningsbar_ram = ttk.Frame(canvas)

        rulningsbar_ram.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=rulningsbar_ram, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        for arkiv in self.extraherade_filer:
            arkiv_etikett = ttk.Label(
                rulningsbar_ram, 
                text=arkiv, 
                font=('Consolas', 10)
            )
            arkiv_etikett.pack(anchor='w', padx=10, pady=2)
        
        slutford_knapp = self.Skapa_Stiliserad_Knapp(
            huvud_ram, 
            "Slutford", 
            self.Skapa_Granssnitt_Sociala, 
            'Accent.TButton'
        )
        slutford_knapp.pack(pady=20)
    
    def Skapa_Granssnitt_Sociala(self):
        self.Rensa_Fonster()
        
        huvud_ram = ttk.Frame(self.root, padding="30 30 30 30")
        huvud_ram.pack(fill=tk.BOTH, expand=True)
        
        titel = self.Skapa_Stiliserad_Etikett(
            huvud_ram, 
            "Sociala", 
            font=('Segoe UI', 24, 'bold'), 
            color=self.colors.primary
        )
        titel.pack(pady=(0, 40))
        
        sociala_lankar = [
            (" Discord SPC", "https://discord.gg/3fApZh66Tf", "discord.png"),
            (" Instagram", "https://www.instagram.com/spc.samp/", "instagram.png"),
            (" YouTube", "https://www.youtube.com/@spc-samp", "youtube.png"),
            (" TikTok", "https://www.tiktok.com/@spc.samp", "tiktok.png"),
            (" GitHub", "https://github.com/spc-samp", "github.png"),
        ]
        
        knapp_ram = ttk.Frame(huvud_ram)
        knapp_ram.pack(expand=True)
        
        def Oppna_Lank(lank):
            webbrowser.open(lank, new=2)
        
        def ommaskala_ikon(ikon_stig, storlek=(30, 30)):
            bas_stig = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
            full_stig = os.path.join(bas_stig, ikon_stig)
            
            bild = Image.open(full_stig)
            omskalad_bild = bild.resize(storlek, Image.LANCZOS)
            return ImageTk.PhotoImage(omskalad_bild)
        
        for i in range(0, len(sociala_lankar), 2):
            rad_ram = ttk.Frame(knapp_ram)
            rad_ram.pack(fill=tk.X, pady=10)
            
            for j in range(2):
                if i + j < len(sociala_lankar):
                    namn, lank, ikon_path = sociala_lankar[i + j]
                    
                    ikon = ommaskala_ikon(os.path.join('icons', ikon_path))
                    
                    social_knapp = ttk.Button(
                        rad_ram, 
                        text=namn, 
                        image=ikon, 
                        compound=tk.LEFT,
                        command=lambda l=lank: Oppna_Lank(l)
                    )
                    social_knapp.image = ikon
                    social_knapp.pack(side=tk.LEFT, padx=10, expand=True, fill=tk.X)
        
        stang_knapp = ttk.Button(
            knapp_ram, 
            text="Stang", 
            command=self.root.quit,
            style='Stang.TButton'
        )
        stang_knapp.pack(pady=10, padx=20, fill=tk.X)

        stil = ttk.Style()
        stil.configure(
            'Stang.TButton', 
            background='red', 
            foreground='white', 
            font=('Segoe UI', 12)
        )

    def Avbryt_Installation(self):
        self.Rensa_Fonster()
        
        huvud_ram = ttk.Frame(self.root, padding="30 30 30 30")
        huvud_ram.pack(fill=tk.BOTH, expand=True)
        
        titel = self.Skapa_Stiliserad_Etikett(
            huvud_ram, 
            "Avbryter Installation", 
            font=('Segoe UI', 16, 'bold'), 
            color=self.colors.primary
        )
        titel.pack(pady=(0, 20))
        
        status_etikett = self.Skapa_Stiliserad_Etikett(
            huvud_ram, 
            "Vara vanlig, alla operationer avbryts..."
        )
        status_etikett.pack(pady=20)
        
        framsteg_bar = ttk.Progressbar(
            huvud_ram, 
            length=600, 
            mode='determinate', 
            maximum=100
        )
        framsteg_bar.pack(pady=20)

        def Avbrytande():
            for i in range(101):
                framsteg_bar['value'] = i
                self.root.update_idletasks()
                time.sleep(0.05)
            
            self.root.after(0, self.Skapa_Granssnitt_Sociala)

        threading.Thread(target=Avbrytande, daemon=True).start()

def main_client():
    root = tk.Tk()
    Samp_Client_R1_Voip(root)
    root.mainloop()

if __name__ == "__main__":
    main_client()