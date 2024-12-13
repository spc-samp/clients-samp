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
class Client_Yadra:
    fon: str = '#1E1E1E'
    pervichnyi: str = '#3B8AFF'
    vtorichnyi: str = '#2C2C2C'
    tekst_pervichnyi: str = '#FFFFFF'
    tekst_vtorichnyi: str = '#A0A0A0'

class Samp_Client_R2:
    def __init__(self, koren: tk.Tk):
        self.koren = koren
        self.Nastroit_Koren()
        self.tsveta = Client_Yadra()
        self.vybrannaya_papka = tk.StringVar(value="Никакая папка еще не выбрана")
        self.izvlechennye_fayli = []
        self.Nastroit_Temu()
        self.Sozdat_Inicialnyy_Interfeys()
        self.Nastroit_Ikonu_Okna()

    def Nastroit_Ikonu_Okna(self):
        bazovyy_put = getattr(sys, '_MEIPASS', os.path.abspath("."))
        put_k_ikone = os.path.join(bazovyy_put, "icons", "spc.png")

        img = Image.open(put_k_ikone)
        ikona = ImageTk.PhotoImage(img)
        self.koren.iconphoto(True, ikona)

    def Nastroit_Koren(self):
        self.koren.title("Client R2 - SPC")
        self.koren.geometry("700x500")
        self.koren.resizable(True, True)

    def Nastroit_Temu(self):
        sv_ttk.set_theme("dark")
        self.koren.configure(bg=self.tsveta.fon)

    def Ochestit_Okno(self):
        for widget in self.koren.winfo_children():
            widget.destroy()

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

    def Sozdat_Knopku_Stilya(
        self, 
        roditel, 
        tekst: str, 
        komanda: Callable, 
        stil: str = 'Accent.TButton'
    ) -> ttk.Button:
        return ttk.Button(
            roditel, 
            text=tekst, 
            command=komanda,
            style=stil
        )

    def Sozdat_Inicialnyy_Interfeys(self):
        self.Ochestit_Okno()
        
        glavnyy_quadro = ttk.Frame(self.koren, padding="30 30 30 30")
        glavnyy_quadro.pack(fill=tk.BOTH, expand=True)
        
        zaglaviye = self.Sozdat_Etiketku_Stilya(
            glavnyy_quadro, 
            "Установщик Client R2 SA:MP", 
            shrift=('Segoe UI', 20, 'bold'), 
            tsvet=self.tsveta.pervichnyi
        )
        zaglaviye.pack(pady=(0, 30))
        
        podzaglaviye = self.Sozdat_Etiketku_Stilya(
            glavnyy_quadro, 
            "Установщик мода SA:MP (San Andreas Multiplayer), версия 0.3.7 R2"
        )
        podzaglaviye.pack(pady=(0, 20))
        
        frame_papki = ttk.Frame(glavnyy_quadro)
        frame_papki.pack(fill=tk.X, pady=10)
        
        papka_label = ttk.Label(
            frame_papki, 
            textvariable=self.vybrannaya_papka, 
            font=('Consolas', 10), 
            wraplength=500,
            foreground=self.tsveta.tekst_pervichnyi
        )
        papka_label.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 10))
        
        knopka_vybora = self.Sozdat_Knopku_Stilya(
            frame_papki, 
            "Выбрать Папку", 
            self.Vybrat_Papku
        )
        knopka_vybora.pack(side=tk.RIGHT)

    def Vybrat_Papku(self):
        papka = filedialog.askdirectory(
            title="Выберите папку Grand Theft Auto San Andreas",
            initialdir=os.path.expanduser("~")
        )
        
        if papka:
            self.vybrannaya_papka.set(papka)
            self.Sozdat_Interfeys_Proverki_Papki()

    def Sozdat_Interfeys_Proverki_Papki(self):
        self.Ochestit_Okno()
        
        glavnyy_quadro = ttk.Frame(self.koren, padding="30 30 30 30")
        glavnyy_quadro.pack(fill=tk.BOTH, expand=True)
        
        zaglaviye = self.Sozdat_Etiketku_Stilya(
            glavnyy_quadro, 
            "Проверка Папки", 
            shrift=('Segoe UI', 16, 'bold'), 
            tsvet=self.tsveta.pervichnyi
        )
        zaglaviye.pack(pady=(0, 20))
        
        status_label = self.Sozdat_Etiketku_Stilya(
            glavnyy_quadro, 
            "Проверка правильности папки GTA..."
        )
        status_label.pack(pady=20)
        
        error_label = ttk.Label(
            glavnyy_quadro, 
            text="", 
            foreground="red", 
            font=('Segoe UI', 10)
        )
        error_label.pack(pady=10)
        
        progress_bar = ttk.Progressbar(
            glavnyy_quadro, 
            length=600, 
            mode='determinate', 
            maximum=100
        )
        progress_bar.pack(pady=20)

        def Proverka_Zavershena():
            papka = self.vybrannaya_papka.get()
            
            for i in range(101):
                progress_bar['value'] = i
                self.koren.update_idletasks()
                time.sleep(0.05)
            
            def Pokazat_Oshibku(soobshchenie):
                error_label.config(text=soobshchenie)
                knopka_popytki_snova.pack()
            
            if not os.path.exists(papka):
                Pokazat_Oshibku("Ошибка: Выбранная папка не существует.")
                return

            if os.path.basename(papka) != "Grand Theft Auto San Andreas":
                Pokazat_Oshibku("Ошибка: Неверная папка. Выберите правильную папку GTA San Andreas (Grand Theft Auto San Andreas).")
                return

            put_k_exe = os.path.join(papka, "gta_sa.exe")
            if not os.path.isfile(put_k_exe):
                Pokazat_Oshibku("Ошибка: Файл 'gta_sa.exe' не найден в папке.")
                return
            
            self.koren.after(0, self.Sozdat_Interfeys_Podtverzhdenia_Client)

        def Popytka_Snova():
            knopka_popytki_snova.pack_forget()
            error_label.config(text="")
            self.Sozdat_Inicialnyy_Interfeys()

        knopka_popytki_snova = self.Sozdat_Knopku_Stilya(
            glavnyy_quadro, 
            "Попытаться Снова", 
            Popytka_Snova
        )

        threading.Thread(target=Proverka_Zavershena, daemon=True).start()

    def Sozdat_Interfeys_Podtverzhdenia_Client(self):
        self.Ochestit_Okno()
        
        glavnyy_quadro = ttk.Frame(self.koren, padding="30 30 30 30")
        glavnyy_quadro.pack(fill=tk.BOTH, expand=True)
        
        zaglaviye = self.Sozdat_Etiketku_Stilya(
            glavnyy_quadro, 
            "Установить Client", 
            shrift=('Segoe UI', 16, 'bold'), 
            tsvet=self.tsveta.pervichnyi
        )
        zaglaviye.pack(pady=(0, 20))
        
        podzaglaviye = self.Sozdat_Etiketku_Stilya(
            glavnyy_quadro, 
            "Папка успешно проверена. Вы хотите продолжить\nустановку Client R2?"
        )
        podzaglaviye.pack(pady=20)
        
        frame_knopok = ttk.Frame(glavnyy_quadro)
        frame_knopok.pack(pady=20)
        
        knopka_prodolzheniya = self.Sozdat_Knopku_Stilya(
            frame_knopok, 
            "Продолжить", 
            self.Nachat_Ustanovku_Client, 
            'Accent.TButton'
        )
        knopka_prodolzheniya.pack(side=tk.LEFT, padx=10)
        
        knopka_otmeny = self.Sozdat_Knopku_Stilya(
            frame_knopok, 
            "Отмена", 
            self.Otmenit_Ustanovku
        )
        knopka_otmeny.pack(side=tk.LEFT, padx=10)

    def Nachat_Ustanovku_Client(self):
        self.Ochestit_Okno()
        
        glavnyy_quadro = ttk.Frame(self.koren, padding="30 30 30 30")
        glavnyy_quadro.pack(fill=tk.BOTH, expand=True)
        
        zaglaviye = self.Sozdat_Etiketku_Stilya(
            glavnyy_quadro, 
            "Установка Client R2", 
            shrift=('Segoe UI', 16, 'bold'), 
            tsvet=self.tsveta.pervichnyi
        )
        zaglaviye.pack(pady=(0, 20))
        
        status_label = self.Sozdat_Etiketku_Stilya(
            glavnyy_quadro, 
            "Установка Client, пожалуйста, подождите..."
        )
        status_label.pack(pady=20)
        
        progress_bar = ttk.Progressbar(
            glavnyy_quadro, 
            length=600, 
            mode='determinate', 
            maximum=100
        )
        progress_bar.pack(pady=20)
        
        fayl_label = ttk.Label(
            glavnyy_quadro, 
            text="", 
            font=('Consolas', 10),
            foreground=self.tsveta.tekst_pervichnyi
        )
        fayl_label.pack(pady=10)

        def Ustanovka_Client():
            put_k_zipu = getattr(sys, "_MEIPASS", os.path.abspath("."))
            fayl_zip = os.path.join(put_k_zipu, "archives", "samp-client-r2.zip")
            
            papka_naznacheniya = self.vybrannaya_papka.get()

            with zipfile.ZipFile(fayl_zip, 'r') as zip_ref:
                fayli = zip_ref.namelist()
                vsego_faylov = len(fayli)
                
                for i, fayl in enumerate(fayli, start=1):
                    fayl_label.config(text=f"Извлечение: {os.path.basename(fayl)}")
                    progress_bar['value'] = (i / vsego_faylov) * 100
                    self.koren.update_idletasks()
                    
                    zip_ref.extract(fayl, papka_naznacheniya)
                    self.izvlechennye_fayli.append(fayl)
                    time.sleep(0.1)
            
            fayl_label.config(text="Установка завершена!")
            progress_bar['value'] = 100
            self.koren.update_idletasks()
            time.sleep(1)
            
            self.koren.after(0, self.Pokazat_Rezume_Ustanovki)
        
        threading.Thread(target=Ustanovka_Client, daemon=True).start()

    def Pokazat_Rezume_Ustanovki(self):
        self.Ochestit_Okno()
        
        glavnyy_quadro = ttk.Frame(self.koren, padding="30 30 30 30")
        glavnyy_quadro.pack(fill=tk.BOTH, expand=True)
        
        zaglaviye = self.Sozdat_Etiketku_Stilya(
            glavnyy_quadro, 
            "Извлеченные Файлы", 
            shrift=('Segoe UI', 16, 'bold'), 
            tsvet=self.tsveta.pervichnyi
        )
        zaglaviye.pack(pady=(0, 20))
        
        frame_prokrutki = ttk.Frame(glavnyy_quadro)
        frame_prokrutki.pack(fill=tk.BOTH, expand=True, pady=20)
        
        canvas = tk.Canvas(frame_prokrutki)
        scrollbar = ttk.Scrollbar(frame_prokrutki, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        for fayl in self.izvlechennye_fayli:
            label_fayla = ttk.Label(
                scrollable_frame, 
                text=fayl, 
                font=('Consolas', 10)
            )
            label_fayla.pack(anchor='w', padx=10, pady=2)
        
        knopka_zaversheno = self.Sozdat_Knopku_Stilya(
            glavnyy_quadro, 
            "Завершено", 
            self.Sozdat_Interfeys_Sotsialnyh, 
            'Accent.TButton'
        )
        knopka_zaversheno.pack(pady=20)

    def Sozdat_Interfeys_Sotsialnyh(self):
        self.Ochestit_Okno()
        
        glavnyy_quadro = ttk.Frame(self.koren, padding="30 30 30 30")
        glavnyy_quadro.pack(fill=tk.BOTH, expand=True)
        
        zaglaviye = self.Sozdat_Etiketku_Stilya(
            glavnyy_quadro, 
            "Социальные Сети", 
            shrift=('Segoe UI', 24, 'bold'), 
            tsvet=self.tsveta.pervichnyi
        )
        zaglaviye.pack(pady=(0, 40))
        
        sotsialnye_ssylki = [
            (" Discord SPC", "https://discord.gg/3fApZh66Tf", "discord.png"),
            (" Instagram", "https://www.instagram.com/spc.samp/", "instagram.png"),
            (" YouTube", "https://www.youtube.com/@spc-samp", "youtube.png"),
            (" TikTok", "https://www.tiktok.com/@spc.samp", "tiktok.png"),
            (" GitHub", "https://github.com/spc-samp", "github.png"),
        ]
        
        frame_knopok = ttk.Frame(glavnyy_quadro)
        frame_knopok.pack(expand=True)
        
        def Otkryt_Ssylku(ssylka):
            webbrowser.open(ssylka, new=2)
        
        def izmenit_razmer_ikony(put_k_ikone, razmer=(30, 30)):
            bazovyy_put = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
            polnyy_put = os.path.join(bazovyy_put, put_k_ikone)
            
            kartinka = Image.open(polnyy_put)
            kartinka_izmeneniya = kartinka.resize(razmer, Image.LANCZOS)
            return ImageTk.PhotoImage(kartinka_izmeneniya)
        
        for i in range(0, len(sotsialnye_ssylki), 2):
            frame_stroki = ttk.Frame(frame_knopok)
            frame_stroki.pack(fill=tk.X, pady=10)
            
            for j in range(2):
                if i + j < len(sotsialnye_ssylki):
                    imya, ssylka, put_k_ikone = sotsialnye_ssylki[i + j]
                    
                    ikona = izmenit_razmer_ikony(os.path.join('icons', put_k_ikone))
                    
                    knopka_sotsialnaya = ttk.Button(
                        frame_stroki, 
                        text=imya, 
                        image=ikona, 
                        compound=tk.LEFT,
                        command=lambda l=ssylka: Otkryt_Ssylku(l)
                    )
                    knopka_sotsialnaya.image = ikona
                    knopka_sotsialnaya.pack(side=tk.LEFT, padx=10, expand=True, fill=tk.X)
        
        knopka_zakrytiya = ttk.Button(
            frame_knopok, 
            text="Закрыть", 
            command=self.koren.quit,
            style='Zakryt.TButton'
        )
        knopka_zakrytiya.pack(pady=10, padx=20, fill=tk.X)

        stil = ttk.Style()
        stil.configure(
            'Zakryt.TButton', 
            background='red', 
            foreground='white', 
            font=('Segoe UI', 12)
        )

    def Otmenit_Ustanovku(self):
        self.Ochestit_Okno()
        
        glavnyy_quadro = ttk.Frame(self.koren, padding="30 30 30 30")
        glavnyy_quadro.pack(fill=tk.BOTH, expand=True)
        
        zaglaviye = self.Sozdat_Etiketku_Stilya(
            glavnyy_quadro, 
            "Отмена Установки", 
            shrift=('Segoe UI', 16, 'bold'), 
            tsvet=self.tsveta.pervichnyi
        )
        zaglaviye.pack(pady=(0, 20))
        
        status_label = self.Sozdat_Etiketku_Stilya(
            glavnyy_quadro, 
            "Пожалуйста, подождите, выполняется отмена операции..."
        )
        status_label.pack(pady=20)
        
        progress_bar = ttk.Progressbar(
            glavnyy_quadro, 
            length=600, 
            mode='determinate', 
            maximum=100
        )
        progress_bar.pack(pady=20)

        def Otmena():
            for i in range(101):
                progress_bar['value'] = i
                self.koren.update_idletasks()
                time.sleep(0.05)
            
            self.koren.after(0, self.Sozdat_Interfeys_Sotsialnyh)

        threading.Thread(target=Otmena, daemon=True).start()

def main_client():
    koren = tk.Tk()
    Samp_Client_R2(koren)
    koren.mainloop()

if __name__ == "__main__":
    main_client()