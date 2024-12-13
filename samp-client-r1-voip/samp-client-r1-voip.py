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
class Client_Renkleri:
    background: str = '#1E1E1E'
    primary: str = '#3B8AFF'
    secondary: str = '#2C2C2C'
    text_primary: str = '#FFFFFF'
    text_secondary: str = '#A0A0A0'

class Samp_Client_R1_Voip:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.Koku_Yapilandirma()
        self.colors = Client_Renkleri()
        self.secilen_klasor = tk.StringVar(value="Henuz klasor secilmedi")
        self.cikarilan_dosyalar = []
        self.Tema_Yapilandirma()
        self.Baslangic_Arayuzu_Olustur()
        self.Pencere_Simgesi_Yapilandirma()

    def Pencere_Simgesi_Yapilandirma(self):
        base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
        icon_path = os.path.join(base_path, "icons", "spc.png")

        img = Image.open(icon_path)
        icon = ImageTk.PhotoImage(img)
        self.root.iconphoto(True, icon)

    def Koku_Yapilandirma(self):
        self.root.title("Client R1 Voip - SPC")
        self.root.geometry("700x500")
        self.root.resizable(True, True)

    def Tema_Yapilandirma(self):
        sv_ttk.set_theme("dark")
        self.root.configure(bg=self.colors.background)

    def Pencereyi_Temizle(self):
        for widget in self.root.winfo_children():
            widget.destroy()

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

    def Dugme_Olustur(
        self, 
        parent, 
        metin: str, 
        komut: Callable, 
        stil: str = 'Accent.TButton'
    ) -> ttk.Button:
        return ttk.Button(
            parent, 
            text=metin, 
            command=komut,
            style=stil
        )

    def Baslangic_Arayuzu_Olustur(self):
        self.Pencereyi_Temizle()
        
        ana_cerceve = ttk.Frame(self.root, padding="30 30 30 30")
        ana_cerceve.pack(fill=tk.BOTH, expand=True)
        
        baslik = self.Etiket_Olustur(
            ana_cerceve, 
            "Client R1 Voip SA:MP Yukleyici", 
            font=('Segoe UI', 20, 'bold'), 
            renk=self.colors.primary
        )
        baslik.pack(pady=(0, 30))
        
        alt_baslik = self.Etiket_Olustur(
            ana_cerceve, 
            "SA:MP (San Andreas Multiplayer) mod yukleyicisi, versiyon 0.3.7 R1 Voip"
        )
        alt_baslik.pack(pady=(0, 20))
        
        klasor_cercevesi = ttk.Frame(ana_cerceve)
        klasor_cercevesi.pack(fill=tk.X, pady=10)
        
        klasor_etiketi = ttk.Label(
            klasor_cercevesi, 
            textvariable=self.secilen_klasor, 
            font=('Consolas', 10), 
            wraplength=500,
            foreground=self.colors.text_primary
        )
        klasor_etiketi.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 10))
        
        klasor_sec_dugmesi = self.Dugme_Olustur(
            klasor_cercevesi, 
            "Klasor Sec", 
            self.Klasor_Sec
        )
        klasor_sec_dugmesi.pack(side=tk.RIGHT)

    def Klasor_Sec(self):
        klasor = filedialog.askdirectory(
            title="Grand Theft Auto San Andreas klasorunu secin",
            initialdir=os.path.expanduser("~")
        )
        
        if klasor:
            self.secilen_klasor.set(klasor)
            self.Klasor_Dogrulama_Arayuzu()

    def Klasor_Dogrulama_Arayuzu(self):
        self.Pencereyi_Temizle()
        
        ana_cerceve = ttk.Frame(self.root, padding="30 30 30 30")
        ana_cerceve.pack(fill=tk.BOTH, expand=True)
        
        baslik = self.Etiket_Olustur(
            ana_cerceve, 
            "Klasoru Dogrulama", 
            font=('Segoe UI', 16, 'bold'), 
            renk=self.colors.primary
        )
        baslik.pack(pady=(0, 20))
        
        durum_etiketi = self.Etiket_Olustur(
            ana_cerceve, 
            "GTA klasorunun dogru olup olmadigini kontrol ediliyor..."
        )
        durum_etiketi.pack(pady=20)
        
        hata_etiketi = ttk.Label(
            ana_cerceve, 
            text="", 
            foreground="red", 
            font=('Segoe UI', 10)
        )
        hata_etiketi.pack(pady=10)
        
        ilerleme_cubugu = ttk.Progressbar(
            ana_cerceve, 
            length=600, 
            mode='determinate', 
            maximum=100
        )
        ilerleme_cubugu.pack(pady=20)

        def Dogrulama_Tamamlandi():
            klasor = self.secilen_klasor.get()
            
            for i in range(101):
                ilerleme_cubugu['value'] = i
                self.root.update_idletasks()
                time.sleep(0.05)
            
            def Hatay_Goster(mesaj):
                hata_etiketi.config(text=mesaj)
                tekrar_dugmesi.pack()
            
            if not os.path.exists(klasor):
                Hatay_Goster("Hata: Secilen klasor mevcut degil.")
                return

            if os.path.basename(klasor) != "Grand Theft Auto San Andreas":
                Hatay_Goster("Hata: Gecersiz klasor. Lutfen dogru GTA San Andreas klasorunu secin.")
                return

            exe_yolu = os.path.join(klasor, "gta_sa.exe")
            if not os.path.isfile(exe_yolu):
                Hatay_Goster("Hata: 'gta_sa.exe' dosyasi klasorde bulunamadi.")
                return
            
            self.root.after(0, self.Client_Onay_Arayuzu)

        def Tekrar_Dene():
            tekrar_dugmesi.pack_forget()
            hata_etiketi.config(text="")
            self.Baslangic_Arayuzu_Olustur()

        tekrar_dugmesi = self.Dugme_Olustur(
            ana_cerceve, 
            "Tekrar Dene", 
            Tekrar_Dene
        )

        threading.Thread(target=Dogrulama_Tamamlandi, daemon=True).start()

    def Client_Onay_Arayuzu(self):
        self.Pencereyi_Temizle()
        
        ana_cerceve = ttk.Frame(self.root, padding="30 30 30 30")
        ana_cerceve.pack(fill=tk.BOTH, expand=True)
        
        baslik = self.Etiket_Olustur(
            ana_cerceve, 
            "Client'yi Kur", 
            font=('Segoe UI', 16, 'bold'), 
            renk=self.colors.primary
        )
        baslik.pack(pady=(0, 20))
        
        alt_baslik = self.Etiket_Olustur(
            ana_cerceve, 
            "Klasor basariyla dogrulandi. R1 Voip Client Sini yuklemek istiyor musunuz?"
        )
        alt_baslik.pack(pady=20)
        
        dugme_cercevesi = ttk.Frame(ana_cerceve)
        dugme_cercevesi.pack(pady=20)
        
        devam_dugmesi = self.Dugme_Olustur(
            dugme_cercevesi, 
            "Devam", 
            self.Client_Yuklemeye_Basla, 
            'Accent.TButton'
        )
        devam_dugmesi.pack(side=tk.LEFT, padx=10)
        
        iptal_dugmesi = self.Dugme_Olustur(
            dugme_cercevesi, 
            "Iptal", 
            self.Yuklemeyi_Iptal_Et
        )
        iptal_dugmesi.pack(side=tk.LEFT, padx=10)

    def Client_Yuklemeye_Basla(self):
        self.Pencereyi_Temizle()
        
        ana_cerceve = ttk.Frame(self.root, padding="30 30 30 30")
        ana_cerceve.pack(fill=tk.BOTH, expand=True)
        
        baslik = self.Etiket_Olustur(
            ana_cerceve, 
            "R1 Voip Client'si Yukleniyor", 
            font=('Segoe UI', 16, 'bold'), 
            renk=self.colors.primary
        )
        baslik.pack(pady=(0, 20))
        
        durum_etiketi = self.Etiket_Olustur(
            ana_cerceve, 
            "Client yukleniyor, lutfen bekleyin..."
        )
        durum_etiketi.pack(pady=20)
        
        ilerleme_cubugu = ttk.Progressbar(
            ana_cerceve, 
            length=600, 
            mode='determinate', 
            maximum=100
        )
        ilerleme_cubugu.pack(pady=20)
        
        dosya_etiketi = ttk.Label(
            ana_cerceve, 
            text="", 
            font=('Consolas', 10),
            foreground=self.colors.text_primary
        )
        dosya_etiketi.pack(pady=10)

        def Client_Yukleme():
            zip_yolu = getattr(sys, "_MEIPASS", os.path.abspath("."))
            zip_dosyasi = os.path.join(zip_yolu, "archives", "samp-client-r1-voip.zip")
            
            hedef_klasor = self.secilen_klasor.get()

            with zipfile.ZipFile(zip_dosyasi, 'r') as zip_ref:
                dosyalar = zip_ref.namelist()
                toplam_dosya = len(dosyalar)
                
                for i, dosya in enumerate(dosyalar, start=1):
                    dosya_etiketi.config(text=f"Cikartiliyor: {os.path.basename(dosya)}")
                    ilerleme_cubugu['value'] = (i / toplam_dosya) * 100
                    self.root.update_idletasks()
                    
                    zip_ref.extract(dosya, hedef_klasor)
                    self.cikarilan_dosyalar.append(dosya)
                    time.sleep(0.1)
            
            dosya_etiketi.config(text="Yukleme tamamlandi!")
            ilerleme_cubugu['value'] = 100
            self.root.update_idletasks()
            time.sleep(1)
            
            self.root.after(0, self.Yukleme_Ozeti_Goster)
        
        threading.Thread(target=Client_Yukleme, daemon=True).start()

    def Yukleme_Ozeti_Goster(self):
        self.Pencereyi_Temizle()
        
        ana_cerceve = ttk.Frame(self.root, padding="30 30 30 30")
        ana_cerceve.pack(fill=tk.BOTH, expand=True)
        
        baslik = self.Etiket_Olustur(
            ana_cerceve, 
            "Cikarilan Dosyalar", 
            font=('Segoe UI', 16, 'bold'), 
            renk=self.colors.primary
        )
        baslik.pack(pady=(0, 20))
        
        kaydirma_cercevesi = ttk.Frame(ana_cerceve)
        kaydirma_cercevesi.pack(fill=tk.BOTH, expand=True, pady=20)
        
        tuvali = tk.Canvas(kaydirma_cercevesi)
        kaydirma_cubugu = ttk.Scrollbar(kaydirma_cercevesi, orient="vertical", command=tuvali.yview)
        kaydirilanabilir_cerceve = ttk.Frame(tuvali)

        kaydirilanabilir_cerceve.bind(
            "<Configure>",
            lambda e: tuvali.configure(scrollregion=tuvali.bbox("all"))
        )

        tuvali.create_window((0, 0), window=kaydirilanabilir_cerceve, anchor="nw")
        tuvali.configure(yscrollcommand=kaydirma_cubugu.set)

        tuvali.pack(side="left", fill="both", expand=True)
        kaydirma_cubugu.pack(side="right", fill="y")
        
        for dosya in self.cikarilan_dosyalar:
            dosya_etiketi = ttk.Label(
                kaydirilanabilir_cerceve, 
                text=dosya, 
                font=('Consolas', 10)
            )
            dosya_etiketi.pack(anchor='w', padx=10, pady=2)
        
        tamamlandi_dugmesi = self.Dugme_Olustur(
            ana_cerceve, 
            "Tamamlandi", 
            self.Sosyal_Arayuzu_Olustur, 
            'Accent.TButton'
        )
        tamamlandi_dugmesi.pack(pady=20)

    def Sosyal_Arayuzu_Olustur(self):
        self.Pencereyi_Temizle()
        
        ana_cerceve = ttk.Frame(self.root, padding="30 30 30 30")
        ana_cerceve.pack(fill=tk.BOTH, expand=True)
        
        baslik = self.Etiket_Olustur(
            ana_cerceve, 
            "Sosyal Medya", 
            font=('Segoe UI', 24, 'bold'), 
            renk=self.colors.primary
        )
        baslik.pack(pady=(0, 40))
        
        sosyal_linkler = [
            (" Discord SPC", "https://discord.gg/3fApZh66Tf", "discord.png"),
            (" Instagram", "https://www.instagram.com/spc.samp/", "instagram.png"),
            (" YouTube", "https://www.youtube.com/@spc-samp", "youtube.png"),
            (" TikTok", "https://www.tiktok.com/@spc.samp", "tiktok.png"),
            (" GitHub", "https://github.com/spc-samp", "github.png"),
        ]
        
        dugme_cercevesi = ttk.Frame(ana_cerceve)
        dugme_cercevesi.pack(expand=True)
        
        def Linki_Ac(link):
            webbrowser.open(link, new=2)
        
        def Simgeyi_Yeniden_Boyutlandir(simge_yolu, boyut=(30, 30)):
            base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
            tam_yol = os.path.join(base_path, simge_yolu)
            
            resim = Image.open(tam_yol)
            yeniden_boyutlandirilmis_resim = resim.resize(boyut, Image.LANCZOS)
            return ImageTk.PhotoImage(yeniden_boyutlandirilmis_resim)
        
        for i in range(0, len(sosyal_linkler), 2):
            satir_cercevesi = ttk.Frame(dugme_cercevesi)
            satir_cercevesi.pack(fill=tk.X, pady=10)
            
            for j in range(2):
                if i + j < len(sosyal_linkler):
                    ad, link, simge_yolu = sosyal_linkler[i + j]
                    
                    simge = Simgeyi_Yeniden_Boyutlandir(os.path.join('icons', simge_yolu))
                    
                    sosyal_dugme = ttk.Button(
                        satir_cercevesi, 
                        text=ad, 
                        image=simge, 
                        compound=tk.LEFT,
                        command=lambda l=link: Linki_Ac(l)
                    )
                    sosyal_dugme.image = simge
                    sosyal_dugme.pack(side=tk.LEFT, padx=10, expand=True, fill=tk.X)
        
        kapat_dugmesi = ttk.Button(
            dugme_cercevesi, 
            text="Kapat", 
            command=self.root.quit,
            style='Kapat.TButton'
        )
        kapat_dugmesi.pack(pady=10, padx=20, fill=tk.X)

        stil = ttk.Style()
        stil.configure(
            'Kapat.TButton', 
            background='red', 
            foreground='white', 
            font=('Segoe UI', 12)
        )

    def Yuklemeyi_Iptal_Et(self):
        self.Pencereyi_Temizle()
        
        ana_cerceve = ttk.Frame(self.root, padding="30 30 30 30")
        ana_cerceve.pack(fill=tk.BOTH, expand=True)
        
        baslik = self.Etiket_Olustur(
            ana_cerceve, 
            "Yuklemeyi Iptal Et", 
            font=('Segoe UI', 16, 'bold'), 
            renk=self.colors.primary
        )
        baslik.pack(pady=(0, 20))
        
        durum_etiketi = self.Etiket_Olustur(
            ana_cerceve, 
            "Lutfen bekleyin, islem iptal ediliyor..."
        )
        durum_etiketi.pack(pady=20)
        
        ilerleme_cubugu = ttk.Progressbar(
            ana_cerceve, 
            length=600, 
            mode='determinate', 
            maximum=100
        )
        ilerleme_cubugu.pack(pady=20)

        def Iptal_Etme():
            for i in range(101):
                ilerleme_cubugu['value'] = i
                self.root.update_idletasks()
                time.sleep(0.05)
            
            self.root.after(0, self.Sosyal_Arayuzu_Olustur)

        threading.Thread(target=Iptal_Etme, daemon=True).start()

def main_client():
    root = tk.Tk()
    Samp_Client_R1_Voip(root)
    root.mainloop()

if __name__ == "__main__":
    main_client()