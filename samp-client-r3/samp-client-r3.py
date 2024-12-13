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
class Client_Rdzenie:
    background: str = '#1E1E1E'
    primary: str = '#3B8AFF'
    secondary: str = '#2C2C2C'
    text_primary: str = '#FFFFFF'
    text_secondary: str = '#A0A0A0'

class Samp_Client_R3:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.Konfiguruj_Korzen()
        self.colors = Client_Rdzenie()
        self.wybrana_folder = tk.StringVar(value="Nie wybrano folderu")
        self.wyodrebnione_pliki = []
        self.Konfiguruj_Motyw()
        self.Utworz_Interfejs_Poczatkowy()
        self.Konfiguruj_IkonOkna()

    def Konfiguruj_IkonOkna(self):
        base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
        icon_path = os.path.join(base_path, "icons", "spc.png")

        img = Image.open(icon_path)
        icon = ImageTk.PhotoImage(img)
        self.root.iconphoto(True, icon)

    def Konfiguruj_Korzen(self):
        self.root.title("Client R3 - SPC")
        self.root.geometry("700x500")
        self.root.resizable(True, True)

    def Konfiguruj_Motyw(self):
        sv_ttk.set_theme("dark")
        self.root.configure(bg=self.colors.background)

    def Wyczysc_Okno(self):
        for widget in self.root.winfo_children():
            widget.destroy()

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

    def Utworz_Przycisk_Stylizowany(
        self, 
        parent, 
        tekst: str, 
        komenda: Callable, 
        styl: str = 'Accent.TButton'
    ) -> ttk.Button:
        return ttk.Button(
            parent, 
            text=tekst, 
            command=komenda,
            style=styl
        )

    def Utworz_Interfejs_Poczatkowy(self):
        self.Wyczysc_Okno()
        
        glowna_ramka = ttk.Frame(self.root, padding="30 30 30 30")
        glowna_ramka.pack(fill=tk.BOTH, expand=True)
        
        tytul = self.Utworz_Etykiete_Stylizowana(
            glowna_ramka, 
            "Instalator Client R3 SA:MP", 
            czcionka=('Segoe UI', 20, 'bold'), 
            kolor=self.colors.primary
        )
        tytul.pack(pady=(0, 30))
        
        podtytul = self.Utworz_Etykiete_Stylizowana(
            glowna_ramka, 
            "Instalator moda SA:MP (San Andreas Multiplayer), wersja 0.3.7 R3"
        )
        podtytul.pack(pady=(0, 20))
        
        ramka_folderu = ttk.Frame(glowna_ramka)
        ramka_folderu.pack(fill=tk.X, pady=10)
        
        etykieta_folderu = ttk.Label(
            ramka_folderu, 
            textvariable=self.wybrana_folder, 
            font=('Consolas', 10), 
            wraplength=500,
            foreground=self.colors.text_primary
        )
        etykieta_folderu.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 10))
        
        przycisk_wyboru = self.Utworz_Przycisk_Stylizowany(
            ramka_folderu, 
            "Wybierz Folder", 
            self.Wybierz_Folder
        )
        przycisk_wyboru.pack(side=tk.RIGHT)

    def Wybierz_Folder(self):
        folder = filedialog.askdirectory(
            title="Wybierz folder Grand Theft Auto San Andreas",
            initialdir=os.path.expanduser("~")
        )
        
        if folder:
            self.wybrana_folder.set(folder)
            self.Utworz_Interfejs_SprawdzenieFolderu()

    def Utworz_Interfejs_SprawdzenieFolderu(self):
        self.Wyczysc_Okno()
        
        glowna_ramka = ttk.Frame(self.root, padding="30 30 30 30")
        glowna_ramka.pack(fill=tk.BOTH, expand=True)
        
        tytul = self.Utworz_Etykiete_Stylizowana(
            glowna_ramka, 
            "Sprawdzanie Folderu", 
            czcionka=('Segoe UI', 16, 'bold'), 
            kolor=self.colors.primary
        )
        tytul.pack(pady=(0, 20))
        
        etykieta_statusu = self.Utworz_Etykiete_Stylizowana(
            glowna_ramka, 
            "Sprawdzanie, czy to jest prawidłowy folder GTA..."
        )
        etykieta_statusu.pack(pady=20)
        
        etykieta_bledu = ttk.Label(
            glowna_ramka, 
            text="", 
            foreground="red", 
            font=('Segoe UI', 10)
        )
        etykieta_bledu.pack(pady=10)
        
        pasek_postepu = ttk.Progressbar(
            glowna_ramka, 
            length=600, 
            mode='determinate', 
            maximum=100
        )
        pasek_postepu.pack(pady=20)

        def Weryfikacja_Zakonczona():
            folder = self.wybrana_folder.get()
            
            for i in range(101):
                pasek_postepu['value'] = i
                self.root.update_idletasks()
                time.sleep(0.05)
            
            def Wyswietl_Blad(wiadomosc):
                etykieta_bledu.config(text=wiadomosc)
                przycisk_ponow = self.Utworz_Przycisk_Stylizowany(
                    glowna_ramka, 
                    "Spróbuj Ponownie", 
                    Sprobuj_Ponownie
                )
                przycisk_ponow.pack()
            
            if not os.path.exists(folder):
                Wyswietl_Blad("Błąd: Wybrany folder nie istnieje.")
                return

            if os.path.basename(folder) != "Grand Theft Auto San Andreas":
                Wyswietl_Blad("Błąd: Nieprawidłowy folder. Wybierz właściwy folder GTA San Andreas.")
                return

            sciezka_exe = os.path.join(folder, "gta_sa.exe")
            if not os.path.isfile(sciezka_exe):
                Wyswietl_Blad("Błąd: Nie znaleziono pliku 'gta_sa.exe' w folderze.")
                return
            
            self.root.after(0, self.Utworz_Interfejs_PotwierdzeniemClient)

        def Sprobuj_Ponownie():
            etykieta_bledu.config(text="")
            self.Utworz_Interfejs_Poczatkowy()

        threading.Thread(target=Weryfikacja_Zakonczona, daemon=True).start()

    def Utworz_Interfejs_PotwierdzeniemClient(self):
        self.Wyczysc_Okno()
        
        glowna_ramka = ttk.Frame(self.root, padding="30 30 30 30")
        glowna_ramka.pack(fill=tk.BOTH, expand=True)
        
        tytul = self.Utworz_Etykiete_Stylizowana(
            glowna_ramka, 
            "Instaluj Client", 
            czcionka=('Segoe UI', 16, 'bold'), 
            kolor=self.colors.primary
        )
        tytul.pack(pady=(0, 20))
        
        podtytul = self.Utworz_Etykiete_Stylizowana(
            glowna_ramka, 
            "Folder zweryfikowany pomyślnie. Czy chcesz kontynuować\ninstalację Client R3?"
        )
        podtytul.pack(pady=20)
        
        ramka_przycisku = ttk.Frame(glowna_ramka)
        ramka_przycisku.pack(pady=20)
        
        przycisk_kontynuuj = self.Utworz_Przycisk_Stylizowany(
            ramka_przycisku, 
            "Kontynuuj", 
            self.RozpocznijInstalacjeClient, 
            'Accent.TButton'
        )
        przycisk_kontynuuj.pack(side=tk.LEFT, padx=10)
        
        przycisk_anuluj = self.Utworz_Przycisk_Stylizowany(
            ramka_przycisku, 
            "Anuluj", 
            self.AnulujInstalacje
        )
        przycisk_anuluj.pack(side=tk.LEFT, padx=10)

    def RozpocznijInstalacjeClient(self):
        self.Wyczysc_Okno()
        
        glowna_ramka = ttk.Frame(self.root, padding="30 30 30 30")
        glowna_ramka.pack(fill=tk.BOTH, expand=True)
        
        tytul = self.Utworz_Etykiete_Stylizowana(
            glowna_ramka, 
            "Instalowanie Client R3", 
            czcionka=('Segoe UI', 16, 'bold'), 
            kolor=self.colors.primary
        )
        tytul.pack(pady=(0, 20))
        
        etykieta_statusu = self.Utworz_Etykiete_Stylizowana(
            glowna_ramka, 
            "Instalowanie Client, proszę czekać..."
        )
        etykieta_statusu.pack(pady=20)
        
        pasek_postepu = ttk.Progressbar(
            glowna_ramka, 
            length=600, 
            mode='determinate', 
            maximum=100
        )
        pasek_postepu.pack(pady=20)
        
        etykieta_pliku = ttk.Label(
            glowna_ramka, 
            text="", 
            font=('Consolas', 10),
            foreground=self.colors.text_primary
        )
        etykieta_pliku.pack(pady=10)

        def Instalacja_Client():
            sciezka_zip = getattr(sys, "_MEIPASS", os.path.abspath("."))
            plik_zip = os.path.join(sciezka_zip, "archives", "samp-client-r3.zip")
            
            folder_docelowy = self.wybrana_folder.get()

            with zipfile.ZipFile(plik_zip, 'r') as zip_ref:
                pliki = zip_ref.namelist()
                wszystkie_pliki = len(pliki)
                
                for i, plik in enumerate(pliki, start=1):
                    etykieta_pliku.config(text=f"Wypakowywanie: {os.path.basename(plik)}")
                    pasek_postepu['value'] = (i / wszystkie_pliki) * 100
                    self.root.update_idletasks()
                    
                    zip_ref.extract(plik, folder_docelowy)
                    self.wyodrebnione_pliki.append(plik)
                    time.sleep(0.1)
            
            etykieta_pliku.config(text="Instalacja zakończona!")
            pasek_postepu['value'] = 100
            self.root.update_idletasks()
            time.sleep(1)
            
            self.root.after(0, self.WyswietlPosumowanieInstalacji)
        
        threading.Thread(target=Instalacja_Client, daemon=True).start()

    def WyswietlPosumowanieInstalacji(self):
        self.Wyczysc_Okno()
        
        glowna_ramka = ttk.Frame(self.root, padding="30 30 30 30")
        glowna_ramka.pack(fill=tk.BOTH, expand=True)
        
        tytul = self.Utworz_Etykiete_Stylizowana(
            glowna_ramka, 
            "Wyodrębnione Pliki", 
            czcionka=('Segoe UI', 16, 'bold'), 
            kolor=self.colors.primary
        )
        tytul.pack(pady=(0, 20))
        
        ramka_przewijania = ttk.Frame(glowna_ramka)
        ramka_przewijania.pack(fill=tk.BOTH, expand=True, pady=20)
        
        canvas = tk.Canvas(ramka_przewijania)
        scrollbar = ttk.Scrollbar(ramka_przewijania, orient="vertical", command=canvas.yview)
        przewijana_ramka = ttk.Frame(canvas)

        przewijana_ramka.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=przewijana_ramka, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        for plik in self.wyodrebnione_pliki:
            etykieta_pliku = ttk.Label(
                przewijana_ramka, 
                text=plik, 
                font=('Consolas', 10)
            )
            etykieta_pliku.pack(anchor='w', padx=10, pady=2)
        
        przycisk_zakoncz = self.Utworz_Przycisk_Stylizowany(
            glowna_ramka, 
            "Zakończ", 
            self.Utworz_Interfejs_Spolecznosci, 
            'Accent.TButton'
        )
        przycisk_zakoncz.pack(pady=20)

    def Utworz_Interfejs_Spolecznosci(self):
        self.Wyczysc_Okno()
        
        glowna_ramka = ttk.Frame(self.root, padding="30 30 30 30")
        glowna_ramka.pack(fill=tk.BOTH, expand=True)
        
        tytul = self.Utworz_Etykiete_Stylizowana(
            glowna_ramka, 
            "Społeczność", 
            czcionka=('Segoe UI', 24, 'bold'), 
            kolor=self.colors.primary
        )
        tytul.pack(pady=(0, 40))
        
        linki_spolecznosci = [
            (" Discord SPC", "https://discord.gg/3fApZh66Tf", "discord.png"),
            (" Instagram", "https://www.instagram.com/spc.samp/", "instagram.png"),
            (" YouTube", "https://www.youtube.com/@spc-samp", "youtube.png"),
            (" TikTok", "https://www.tiktok.com/@spc.samp", "tiktok.png"),
            (" GitHub", "https://github.com/spc-samp", "github.png"),
        ]
        
        ramka_przyciskow = ttk.Frame(glowna_ramka)
        ramka_przyciskow.pack(expand=True)
        
        def Otworz_Link(link):
            webbrowser.open(link, new=2)
        
        def Zmien_Rozmiar_Ikony(sciezka_ikony, rozmiar=(30, 30)):
            base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
            sciezka_pelna = os.path.join(base_path, sciezka_ikony)
            
            obraz = Image.open(sciezka_pelna)
            obraz_zmieniony = obraz.resize(rozmiar, Image.LANCZOS)
            return ImageTk.PhotoImage(obraz_zmieniony)
        
        for i in range(0, len(linki_spolecznosci), 2):
            ramka_wiersza = ttk.Frame(ramka_przyciskow)
            ramka_wiersza.pack(fill=tk.X, pady=10)
            
            for j in range(2):
                if i + j < len(linki_spolecznosci):
                    nazwa, link, sciezka_ikony = linki_spolecznosci[i + j]
                    
                    ikona = Zmien_Rozmiar_Ikony(os.path.join('icons', sciezka_ikony))
                    
                    przycisk_spoleczny = ttk.Button(
                        ramka_wiersza, 
                        text=nazwa, 
                        image=ikona, 
                        compound=tk.LEFT,
                        command=lambda l=link: Otworz_Link(l)
                    )
                    przycisk_spoleczny.image = ikona
                    przycisk_spoleczny.pack(side=tk.LEFT, padx=10, expand=True, fill=tk.X)
        
        przycisk_zamknij = ttk.Button(
            ramka_przyciskow, 
            text="Zamknij", 
            command=self.root.quit,
            style='Zamknij.TButton'
        )
        przycisk_zamknij.pack(pady=10, padx=20, fill=tk.X)

        styl = ttk.Style()
        styl.configure(
            'Zamknij.TButton', 
            background='red', 
            foreground='white', 
            font=('Segoe UI', 12)
        )

    def AnulujInstalacje(self):
        self.Wyczysc_Okno()
        
        glowna_ramka = ttk.Frame(self.root, padding="30 30 30 30")
        glowna_ramka.pack(fill=tk.BOTH, expand=True)
        
        tytul = self.Utworz_Etykiete_Stylizowana(
            glowna_ramka, 
            "Anulowanie Instalacji", 
            czcionka=('Segoe UI', 16, 'bold'), 
            kolor=self.colors.primary
        )
        tytul.pack(pady=(0, 20))
        
        etykieta_statusu = self.Utworz_Etykiete_Stylizowana(
            glowna_ramka, 
            "Proszę czekać, operacja jest anulowana..."
        )
        etykieta_statusu.pack(pady=20)
        
        pasek_postepu = ttk.Progressbar(
            glowna_ramka, 
            length=600, 
            mode='determinate', 
            maximum=100
        )
        pasek_postepu.pack(pady=20)

        def Anulowanie():
            for i in range(101):
                pasek_postepu['value'] = i
                self.root.update_idletasks()
                time.sleep(0.05)
            
            self.root.after(0, self.Utworz_Interfejs_Spolecznosci)

        threading.Thread(target=Anulowanie, daemon=True).start()

def glowna_aplikacja():
    root = tk.Tk()
    Samp_Client_R3(root)
    root.mainloop()

if __name__ == "__main__":
    glowna_aplikacja()