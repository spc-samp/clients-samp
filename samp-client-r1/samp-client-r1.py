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
class Client_Farben:
    background: str = '#1E1E1E'
    primary: str = '#3B8AFF'
    secondary: str = '#2C2C2C'
    text_primary: str = '#FFFFFF'
    text_secondary: str = '#A0A0A0'

class Samp_Client_R1:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.Konfigurieren_Wurzel()
        self.colors = Client_Farben()
        self.ausgewahlter_ordner = tk.StringVar(value="Noch kein Ordner ausgewählt")
        self.extrahierte_dateien = []
        self.Konfigurieren_Thema()
        self.Erstellen_Anfangsschnittstelle()
        self.Konfigurieren_FensterIcon()

    def Konfigurieren_FensterIcon(self):
        base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
        icon_path = os.path.join(base_path, "icons", "spc.png")

        img = Image.open(icon_path)
        icon = ImageTk.PhotoImage(img)
        self.root.iconphoto(True, icon)

    def Konfigurieren_Wurzel(self):
        self.root.title("Client R1 - SPC")
        self.root.geometry("700x500")
        self.root.resizable(True, True)

    def Konfigurieren_Thema(self):
        sv_ttk.set_theme("dark")
        self.root.configure(bg=self.colors.background)

    def Leeren_Fenster(self):
        for widget in self.root.winfo_children():
            widget.destroy()

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

    def Erstellen_Taste_Stilisiert(
        self, 
        parent, 
        text: str, 
        befehl: Callable, 
        stil: str = 'Accent.TButton'
    ) -> ttk.Button:
        return ttk.Button(
            parent, 
            text=text, 
            command=befehl,
            style=stil
        )

    def Erstellen_Anfangsschnittstelle(self):
        self.Leeren_Fenster()
        
        hauptrahmen = ttk.Frame(self.root, padding="30 30 30 30")
        hauptrahmen.pack(fill=tk.BOTH, expand=True)
        
        titel = self.Erstellen_Beschriftung_Stilisiert(
            hauptrahmen, 
            "Installationsprogramm Client R1 SA:MP", 
            schrift=('Segoe UI', 20, 'bold'), 
            farbe=self.colors.primary
        )
        titel.pack(pady=(0, 30))
        
        untertitel = self.Erstellen_Beschriftung_Stilisiert(
            hauptrahmen, 
            "Installationsprogramm für SA:MP Mod (San Andreas Multiplayer), Version 0.3.7 R1"
        )
        untertitel.pack(pady=(0, 20))
        
        ordner_rahmen = ttk.Frame(hauptrahmen)
        ordner_rahmen.pack(fill=tk.X, pady=10)
        
        ordner_label = ttk.Label(
            ordner_rahmen, 
            textvariable=self.ausgewahlter_ordner, 
            font=('Consolas', 10), 
            wraplength=500,
            foreground=self.colors.text_primary
        )
        ordner_label.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 10))
        
        ordner_wahlen_taste = self.Erstellen_Taste_Stilisiert(
            ordner_rahmen, 
            "Ordner auswählen", 
            self.Ordner_Wahlen
        )
        ordner_wahlen_taste.pack(side=tk.RIGHT)

    def Ordner_Wahlen(self):
        ordner = filedialog.askdirectory(
            title="Wählen Sie den Ordner von Grand Theft Auto San Andreas",
            initialdir=os.path.expanduser("~")
        )
        
        if ordner:
            self.ausgewahlter_ordner.set(ordner)
            self.Erstellen_Schnittstelle_OrdnerUberprufung()

    def Erstellen_Schnittstelle_OrdnerUberprufung(self):
        self.Leeren_Fenster()
        
        hauptrahmen = ttk.Frame(self.root, padding="30 30 30 30")
        hauptrahmen.pack(fill=tk.BOTH, expand=True)
        
        titel = self.Erstellen_Beschriftung_Stilisiert(
            hauptrahmen, 
            "Ordner überprüfen", 
            schrift=('Segoe UI', 16, 'bold'), 
            farbe=self.colors.primary
        )
        titel.pack(pady=(0, 20))
        
        status_label = self.Erstellen_Beschriftung_Stilisiert(
            hauptrahmen, 
            "Überprüfe, ob dies der richtige Ordner ist..."
        )
        status_label.pack(pady=20)
        
        fehler_label = ttk.Label(
            hauptrahmen, 
            text="", 
            foreground="red", 
            font=('Segoe UI', 10)
        )
        fehler_label.pack(pady=10)
        
        fortschrittsbalken = ttk.Progressbar(
            hauptrahmen, 
            length=600, 
            mode='determinate', 
            maximum=100
        )
        fortschrittsbalken.pack(pady=20)

        def Uberprufung_Abgeschlossen():
            ordner = self.ausgewahlter_ordner.get()
            
            for i in range(101):
                fortschrittsbalken['value'] = i
                self.root.update_idletasks()
                time.sleep(0.05)
            
            def Fehler_Anzeigen(nachricht):
                fehler_label.config(text=nachricht)
                erneut_versuchen_taste.pack()
            
            if not os.path.exists(ordner):
                Fehler_Anzeigen("Fehler: Der ausgewählte Ordner existiert nicht.")
                return

            if os.path.basename(ordner) != "Grand Theft Auto San Andreas":
                Fehler_Anzeigen("Fehler: Ungültiger Ordner. Bitte wählen Sie den richtigen GTA San Andreas-Ordner.")
                return

            exe_pfad = os.path.join(ordner, "gta_sa.exe")
            if not os.path.isfile(exe_pfad):
                Fehler_Anzeigen("Fehler: Die Datei 'gta_sa.exe' wurde im Ordner nicht gefunden.")
                return
            
            self.root.after(0, self.Erstellen_Schnittstelle_ClientBestatigung)

        def Erneut_Versuchen():
            erneut_versuchen_taste.pack_forget()
            fehler_label.config(text="")
            self.Erstellen_Anfangsschnittstelle()

        erneut_versuchen_taste = self.Erstellen_Taste_Stilisiert(
            hauptrahmen, 
            "Erneut versuchen", 
            Erneut_Versuchen
        )

        threading.Thread(target=Uberprufung_Abgeschlossen, daemon=True).start()

    def Erstellen_Schnittstelle_ClientBestatigung(self):
        self.Leeren_Fenster()
        
        hauptrahmen = ttk.Frame(self.root, padding="30 30 30 30")
        hauptrahmen.pack(fill=tk.BOTH, expand=True)
        
        titel = self.Erstellen_Beschriftung_Stilisiert(
            hauptrahmen, 
            "Client installieren", 
            schrift=('Segoe UI', 16, 'bold'), 
            farbe=self.colors.primary
        )
        titel.pack(pady=(0, 20))
        
        untertitel = self.Erstellen_Beschriftung_Stilisiert(
            hauptrahmen, 
            "Ordner erfolgreich überprüft. Möchten Sie mit der Installation\ndes Client R1 fortfahren?"
        )
        untertitel.pack(pady=20)
        
        tasten_rahmen = ttk.Frame(hauptrahmen)
        tasten_rahmen.pack(pady=20)
        
        fortfahren_taste = self.Erstellen_Taste_Stilisiert(
            tasten_rahmen, 
            "Fortfahren", 
            self.Starten_ClientInstallation, 
            'Accent.TButton'
        )
        fortfahren_taste.pack(side=tk.LEFT, padx=10)
        
        abbrechen_taste = self.Erstellen_Taste_Stilisiert(
            tasten_rahmen, 
            "Abbrechen", 
            self.Abbrechen_Installation
        )
        abbrechen_taste.pack(side=tk.LEFT, padx=10)

    def Starten_ClientInstallation(self):
        self.Leeren_Fenster()
        
        hauptrahmen = ttk.Frame(self.root, padding="30 30 30 30")
        hauptrahmen.pack(fill=tk.BOTH, expand=True)
        
        titel = self.Erstellen_Beschriftung_Stilisiert(
            hauptrahmen, 
            "Client R1 installieren", 
            schrift=('Segoe UI', 16, 'bold'), 
            farbe=self.colors.primary
        )
        titel.pack(pady=(0, 20))
        
        status_label = self.Erstellen_Beschriftung_Stilisiert(
            hauptrahmen, 
            "Client wird installiert, bitte warten..."
        )
        status_label.pack(pady=20)
        
        fortschrittsbalken = ttk.Progressbar(
            hauptrahmen, 
            length=600, 
            mode='determinate', 
            maximum=100
        )
        fortschrittsbalken.pack(pady=20)
        
        datei_label = ttk.Label(
            hauptrahmen, 
            text="", 
            font=('Consolas', 10),
            foreground=self.colors.text_primary
        )
        datei_label.pack(pady=10)

        def Installation_Client():
            zip_pfad = getattr(sys, "_MEIPASS", os.path.abspath("."))
            zip_datei = os.path.join(zip_pfad, "archives", "samp-client-r1.zip")
            
            ziel_ordner = self.ausgewahlter_ordner.get()

            with zipfile.ZipFile(zip_datei, 'r') as zip_ref:
                dateien = zip_ref.namelist()
                gesamte_dateien = len(dateien)
                
                for i, datei in enumerate(dateien, start=1):
                    datei_label.config(text=f"Extrahiere: {os.path.basename(datei)}")
                    fortschrittsbalken['value'] = (i / gesamte_dateien) * 100
                    self.root.update_idletasks()
                    
                    zip_ref.extract(datei, ziel_ordner)
                    self.extrahierte_dateien.append(datei)
                    time.sleep(0.1)
            
            datei_label.config(text="Installation abgeschlossen!")
            fortschrittsbalken['value'] = 100
            self.root.update_idletasks()
            time.sleep(1)
            
            self.root.after(0, self.Anzeigen_InstallationszusammenfassungResumo)
        
        threading.Thread(target=Installation_Client, daemon=True).start()

    def Anzeigen_InstallationszusammenfassungResumo(self):
        self.Leeren_Fenster()
        
        hauptrahmen = ttk.Frame(self.root, padding="30 30 30 30")
        hauptrahmen.pack(fill=tk.BOTH, expand=True)
        
        titel = self.Erstellen_Beschriftung_Stilisiert(
            hauptrahmen, 
            "Extrahierte Dateien", 
            schrift=('Segoe UI', 16, 'bold'), 
            farbe=self.colors.primary
        )
        titel.pack(pady=(0, 20))
        
        rollendes_rahmen = ttk.Frame(hauptrahmen)
        rollendes_rahmen.pack(fill=tk.BOTH, expand=True, pady=20)
        
        leinwand = tk.Canvas(rollendes_rahmen)
        scrollleiste = ttk.Scrollbar(rollendes_rahmen, orient="vertical", command=leinwand.yview)
        rollbarer_rahmen = ttk.Frame(leinwand)

        rollbarer_rahmen.bind(
            "<Configure>",
            lambda e: leinwand.configure(scrollregion=leinwand.bbox("all"))
        )

        leinwand.create_window((0, 0), window=rollbarer_rahmen, anchor="nw")
        leinwand.configure(yscrollcommand=scrollleiste.set)

        leinwand.pack(side="left", fill="both", expand=True)
        scrollleiste.pack(side="right", fill="y")
        
        for datei in self.extrahierte_dateien:
            datei_label = ttk.Label(
                rollbarer_rahmen, 
                text=datei, 
                font=('Consolas', 10)
            )
            datei_label.pack(anchor='w', padx=10, pady=2)
        
        abschlieben_taste = self.Erstellen_Taste_Stilisiert(
            hauptrahmen, 
            "Abschließen", 
            self.Erstellen_Schnittstelle_Sozial, 
            'Accent.TButton'
        )
        abschlieben_taste.pack(pady=20)

    def Erstellen_Schnittstelle_Sozial(self):
        self.Leeren_Fenster()
        
        hauptrahmen = ttk.Frame(self.root, padding="30 30 30 30")
        hauptrahmen.pack(fill=tk.BOTH, expand=True)
        
        titel = self.Erstellen_Beschriftung_Stilisiert(
            hauptrahmen, 
            "Soziale Medien", 
            schrift=('Segoe UI', 24, 'bold'), 
            farbe=self.colors.primary
        )
        titel.pack(pady=(0, 40))
        
        soziale_links = [
            (" Discord SPC", "https://discord.gg/3fApZh66Tf", "discord.png"),
            (" Instagram", "https://www.instagram.com/spc.samp/", "instagram.png"),
            (" YouTube", "https://www.youtube.com/@spc-samp", "youtube.png"),
            (" TikTok", "https://www.tiktok.com/@spc.samp", "tiktok.png"),
            (" GitHub", "https://github.com/spc-samp", "github.png"),
        ]
        
        tasten_rahmen = ttk.Frame(hauptrahmen)
        tasten_rahmen.pack(expand=True)
        
        def Link_Offnen(link):
            webbrowser.open(link, new=2)
        
        def Icon_Grobe_Andern(icon_pfad, grobe=(30, 30)):
            basis_pfad = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
            vollständiger_pfad = os.path.join(basis_pfad, icon_pfad)
            
            bild = Image.open(vollständiger_pfad)
            grobe_geändert = bild.resize(grobe, Image.LANCZOS)
            return ImageTk.PhotoImage(grobe_geändert)
        
        for i in range(0, len(soziale_links), 2):
            zeilen_rahmen = ttk.Frame(tasten_rahmen)
            zeilen_rahmen.pack(fill=tk.X, pady=10)
            
            for j in range(2):
                if i + j < len(soziale_links):
                    name, link, icon_pfad = soziale_links[i + j]
                    
                    icon = Icon_Grobe_Andern(os.path.join('icons', icon_pfad))
                    
                    soziale_taste = ttk.Button(
                        zeilen_rahmen, 
                        text=name, 
                        image=icon, 
                        compound=tk.LEFT,
                        command=lambda l=link: Link_Offnen(l)
                    )
                    soziale_taste.image = icon
                    soziale_taste.pack(side=tk.LEFT, padx=10, expand=True, fill=tk.X)
        
        schlieben_taste = ttk.Button(
            tasten_rahmen, 
            text="Schließen", 
            command=self.root.quit,
            style='Schließen.TButton'
        )
        schlieben_taste.pack(pady=10, padx=20, fill=tk.X)

        stil = ttk.Style()
        stil.configure(
            'Schließen.TButton', 
            background='red', 
            foreground='white', 
            font=('Segoe UI', 12)
        )

    def Abbrechen_Installation(self):
        self.Leeren_Fenster()
        
        hauptrahmen = ttk.Frame(self.root, padding="30 30 30 30")
        hauptrahmen.pack(fill=tk.BOTH, expand=True)
        
        titel = self.Erstellen_Beschriftung_Stilisiert(
            hauptrahmen, 
            "Installation abbrechen", 
            schrift=('Segoe UI', 16, 'bold'), 
            farbe=self.colors.primary
        )
        titel.pack(pady=(0, 20))
        
        status_label = self.Erstellen_Beschriftung_Stilisiert(
            hauptrahmen, 
            "Bitte warten, der Vorgang wird abgebrochen..."
        )
        status_label.pack(pady=20)
        
        fortschrittsbalken = ttk.Progressbar(
            hauptrahmen, 
            length=600, 
            mode='determinate', 
            maximum=100
        )
        fortschrittsbalken.pack(pady=20)

        def Abbrechen():
            for i in range(101):
                fortschrittsbalken['value'] = i
                self.root.update_idletasks()
                time.sleep(0.05)
            
            self.root.after(0, self.Erstellen_Schnittstelle_Sozial)

        threading.Thread(target=Abbrechen, daemon=True).start()

def Haupt_Client():
    root = tk.Tk()
    Samp_Client_R1(root)
    root.mainloop()

if __name__ == "__main__":
    Haupt_Client()