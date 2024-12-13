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
class Client_Couleurs:
    background: str = '#1E1E1E'
    primary: str = '#3B8AFF'
    secondary: str = '#2C2C2C'
    text_primary: str = '#FFFFFF'
    text_secondary: str = '#A0A0A0'

class Samp_Client_R1_Voip:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.Configurer_Racine()
        self.colors = Client_Couleurs()
        self.dossier_selectionne = tk.StringVar(value="Aucun dossier n'a ete selectionne")
        self.fichiers_extraits = []
        self.Configurer_Theme()
        self.Creer_Interface_Initiale()
        self.Configurer_IconeFenetre()

    def Configurer_IconeFenetre(self):
        base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
        icon_path = os.path.join(base_path, "icons", "spc.png")

        img = Image.open(icon_path)
        icon = ImageTk.PhotoImage(img)
        self.root.iconphoto(True, icon)

    def Configurer_Racine(self):
        self.root.title("Client R1 Voip - SPC")
        self.root.geometry("700x500")
        self.root.resizable(True, True)

    def Configurer_Theme(self):
        sv_ttk.set_theme("dark")
        self.root.configure(bg=self.colors.background)

    def Nettoyer_Fenetre(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def Creer_Label_Stylise(
        self, 
        parent, 
        texte: str, 
        fonte: tuple = ('Segoe UI', 12), 
        couleur: Optional[str] = None
    ) -> ttk.Label:
        return ttk.Label(
            parent, 
            text=texte, 
            font=fonte,
            foreground=couleur or self.colors.text_secondary
        )

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

    def Creer_Interface_Initiale(self):
        self.Nettoyer_Fenetre()
        
        cadre_principal = ttk.Frame(self.root, padding="30 30 30 30")
        cadre_principal.pack(fill=tk.BOTH, expand=True)
        
        titre = self.Creer_Label_Stylise(
            cadre_principal, 
            "Installateur Client R1 Voip SA:MP", 
            fonte=('Segoe UI', 20, 'bold'), 
            couleur=self.colors.primary
        )
        titre.pack(pady=(0, 30))
        
        sous_titre = self.Creer_Label_Stylise(
            cadre_principal, 
            "Installateur du mod SA:MP (San Andreas Multiplayer), version 0.3.7 R1 Voip"
        )
        sous_titre.pack(pady=(0, 20))
        
        frame_dossier = ttk.Frame(cadre_principal)
        frame_dossier.pack(fill=tk.X, pady=10)
        
        label_dossier = ttk.Label(
            frame_dossier, 
            textvariable=self.dossier_selectionne, 
            font=('Consolas', 10), 
            wraplength=500,
            foreground=self.colors.text_primary
        )
        label_dossier.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 10))
        
        bouton_selectionner = self.Creer_Bouton_Stylise(
            frame_dossier, 
            "Selectionner Dossier", 
            self.Choisir_Dossier
        )
        bouton_selectionner.pack(side=tk.RIGHT)

    def Choisir_Dossier(self):
        dossier = filedialog.askdirectory(
            title="Selectionnez le dossier Grand Theft Auto San Andreas",
            initialdir=os.path.expanduser("~")
        )
        
        if dossier:
            self.dossier_selectionne.set(dossier)
            self.Creer_Interface_VerificationDossier()

    def Creer_Interface_VerificationDossier(self):
        self.Nettoyer_Fenetre()
        
        cadre_principal = ttk.Frame(self.root, padding="30 30 30 30")
        cadre_principal.pack(fill=tk.BOTH, expand=True)
        
        titre = self.Creer_Label_Stylise(
            cadre_principal, 
            "Verification du Dossier", 
            fonte=('Segoe UI', 16, 'bold'), 
            couleur=self.colors.primary
        )
        titre.pack(pady=(0, 20))
        
        label_statut = self.Creer_Label_Stylise(
            cadre_principal, 
            "Verification si c'est le bon dossier de votre GTA..."
        )
        label_statut.pack(pady=20)
        
        label_erreur = ttk.Label(
            cadre_principal, 
            text="", 
            foreground="red", 
            font=('Segoe UI', 10)
        )
        label_erreur.pack(pady=10)
        
        barre_progression = ttk.Progressbar(
            cadre_principal, 
            length=600, 
            mode='determinate', 
            maximum=100
        )
        barre_progression.pack(pady=20)

        def Verification_Complete():
            dossier = self.dossier_selectionne.get()
            
            for i in range(101):
                barre_progression['value'] = i
                self.root.update_idletasks()
                time.sleep(0.05)
            
            def Afficher_Erreur(message):
                label_erreur.config(text=message)
                bouton_reessayer.pack()
            
            if not os.path.exists(dossier):
                Afficher_Erreur("Erreur: Le dossier selectionne n'existe pas.")
                return

            if os.path.basename(dossier) != "Grand Theft Auto San Andreas":
                Afficher_Erreur("Erreur: Dossier invalide. Selectionnez le dossier correct de GTA San Andreas (Grand Theft Auto San Andreas).")
                return

            chemin_exe = os.path.join(dossier, "gta_sa.exe")
            if not os.path.isfile(chemin_exe):
                Afficher_Erreur("Erreur: Le fichier 'gta_sa.exe' n'a pas ete trouve dans le dossier.")
                return
            
            self.root.after(0, self.Creer_Interface_ConfirmationClient)

        def Reessayer():
            bouton_reessayer.pack_forget()
            label_erreur.config(text="")
            self.Creer_Interface_Initiale()

        bouton_reessayer = self.Creer_Bouton_Stylise(
            cadre_principal, 
            "Reessayer", 
            Reessayer
        )

        threading.Thread(target=Verification_Complete, daemon=True).start()

    def Creer_Interface_ConfirmationClient(self):
        self.Nettoyer_Fenetre()
        
        cadre_principal = ttk.Frame(self.root, padding="30 30 30 30")
        cadre_principal.pack(fill=tk.BOTH, expand=True)
        
        titre = self.Creer_Label_Stylise(
            cadre_principal, 
            "Installer Client", 
            fonte=('Segoe UI', 16, 'bold'), 
            couleur=self.colors.primary
        )
        titre.pack(pady=(0, 20))
        
        sous_titre = self.Creer_Label_Stylise(
            cadre_principal, 
            "Dossier verifie avec succes. Voulez-vous continuer\nl'installation du Client R1 Voip?"
        )
        sous_titre.pack(pady=20)
        
        frame_boutons = ttk.Frame(cadre_principal)
        frame_boutons.pack(pady=20)
        
        bouton_continuer = self.Creer_Bouton_Stylise(
            frame_boutons, 
            "Continuer", 
            self.Commencer_Installation_Client, 
            'Accent.TButton'
        )
        bouton_continuer.pack(side=tk.LEFT, padx=10)
        
        bouton_annuler = self.Creer_Bouton_Stylise(
            frame_boutons, 
            "Annuler", 
            self.Annuler_Installation
        )
        bouton_annuler.pack(side=tk.LEFT, padx=10)

    def Commencer_Installation_Client(self):
        self.Nettoyer_Fenetre()
        
        cadre_principal = ttk.Frame(self.root, padding="30 30 30 30")
        cadre_principal.pack(fill=tk.BOTH, expand=True)
        
        titre = self.Creer_Label_Stylise(
            cadre_principal, 
            "Installation Client R1 Voip", 
            fonte=('Segoe UI', 16, 'bold'), 
            couleur=self.colors.primary
        )
        titre.pack(pady=(0, 20))
        
        label_statut = self.Creer_Label_Stylise(
            cadre_principal, 
            "Installation du Client, veuillez patienter..."
        )
        label_statut.pack(pady=20)
        
        barre_progression = ttk.Progressbar(
            cadre_principal, 
            length=600, 
            mode='determinate', 
            maximum=100
        )
        barre_progression.pack(pady=20)
        
        label_fichier = ttk.Label(
            cadre_principal, 
            text="", 
            font=('Consolas', 10),
            foreground=self.colors.text_primary
        )
        label_fichier.pack(pady=10)

        def Installation_Client():
            chemin_zip = getattr(sys, "_MEIPASS", os.path.abspath("."))
            fichier_zip = os.path.join(chemin_zip, "archives", "samp-client-r1-voip.zip")
            
            dossier_destination = self.dossier_selectionne.get()

            with zipfile.ZipFile(fichier_zip, 'r') as zip_ref:
                fichiers = zip_ref.namelist()
                total_fichiers = len(fichiers)
                
                for i, fichier in enumerate(fichiers, start=1):
                    label_fichier.config(text=f"Extraction: {os.path.basename(fichier)}")
                    barre_progression['value'] = (i / total_fichiers) * 100
                    self.root.update_idletasks()
                    
                    zip_ref.extract(fichier, dossier_destination)
                    self.fichiers_extraits.append(fichier)
                    time.sleep(0.1)
            
            label_fichier.config(text="Installation terminee!")
            barre_progression['value'] = 100
            self.root.update_idletasks()
            time.sleep(1)
            
            self.root.after(0, self.Afficher_Resume_Installation)
        
        threading.Thread(target=Installation_Client, daemon=True).start()

    def Afficher_Resume_Installation(self):
        self.Nettoyer_Fenetre()
        
        cadre_principal = ttk.Frame(self.root, padding="30 30 30 30")
        cadre_principal.pack(fill=tk.BOTH, expand=True)
        
        titre = self.Creer_Label_Stylise(
            cadre_principal, 
            "Fichiers Extraits", 
            fonte=('Segoe UI', 16, 'bold'), 
            couleur=self.colors.primary
        )
        titre.pack(pady=(0, 20))
        
        frame_defilement = ttk.Frame(cadre_principal)
        frame_defilement.pack(fill=tk.BOTH, expand=True, pady=20)
        
        canvas = tk.Canvas(frame_defilement)
        scrollbar = ttk.Scrollbar(frame_defilement, orient="vertical", command=canvas.yview)
        frame_defilable = ttk.Frame(canvas)

        frame_defilable.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=frame_defilable, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        for fichier in self.fichiers_extraits:
            label_fichier = ttk.Label(
                frame_defilable, 
                text=fichier, 
                font=('Consolas', 10)
            )
            label_fichier.pack(anchor='w', padx=10, pady=2)
        
        bouton_termine = self.Creer_Bouton_Stylise(
            cadre_principal, 
            "Termine", 
            self.Creer_Interface_Sociales, 
            'Accent.TButton'
        )
        bouton_termine.pack(pady=20)

    def Creer_Interface_Sociales(self):
        self.Nettoyer_Fenetre()
        
        cadre_principal = ttk.Frame(self.root, padding="30 30 30 30")
        cadre_principal.pack(fill=tk.BOTH, expand=True)
        
        titre = self.Creer_Label_Stylise(
            cadre_principal, 
            "Reseaux Sociaux", 
            fonte=('Segoe UI', 24, 'bold'), 
            couleur=self.colors.primary
        )
        titre.pack(pady=(0, 40))
        
        liens_sociaux = [
            (" Discord SPC", "https://discord.gg/3fApZh66Tf", "discord.png"),
            (" Instagram", "https://www.instagram.com/spc.samp/", "instagram.png"),
            (" YouTube", "https://www.youtube.com/@spc-samp", "youtube.png"),
            (" TikTok", "https://www.tiktok.com/@spc.samp", "tiktok.png"),
            (" GitHub", "https://github.com/spc-samp", "github.png"),
        ]
        
        frame_boutons = ttk.Frame(cadre_principal)
        frame_boutons.pack(expand=True)
        
        def Ouvrir_Lien(lien):
            webbrowser.open(lien, new=2)
        
        def redimensionner_icone(chemin_icone, taille=(30, 30)):
            base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
            chemin_complet = os.path.join(base_path, chemin_icone)
            
            image = Image.open(chemin_complet)
            image_redimensionnee = image.resize(taille, Image.LANCZOS)
            return ImageTk.PhotoImage(image_redimensionnee)
        
        for i in range(0, len(liens_sociaux), 2):
            frame_ligne = ttk.Frame(frame_boutons)
            frame_ligne.pack(fill=tk.X, pady=10)
            
            for j in range(2):
                if i + j < len(liens_sociaux):
                    nom, lien, chemin_icone = liens_sociaux[i + j]
                    
                    icone = redimensionner_icone(os.path.join('icons', chemin_icone))
                    
                    bouton_social = ttk.Button(
                        frame_ligne, 
                        text=nom, 
                        image=icone, 
                        compound=tk.LEFT,
                        command=lambda l=lien: Ouvrir_Lien(l)
                    )
                    bouton_social.image = icone
                    bouton_social.pack(side=tk.LEFT, padx=10, expand=True, fill=tk.X)
        
        bouton_fermer = ttk.Button(
            frame_boutons, 
            text="Fermer", 
            command=self.root.quit,
            style='Fermer.TButton'
        )
        bouton_fermer.pack(pady=10, padx=20, fill=tk.X)

        style = ttk.Style()
        style.configure(
            'Fermer.TButton', 
            background='red', 
            foreground='white', 
            font=('Segoe UI', 12)
        )

    def Annuler_Installation(self):
        self.Nettoyer_Fenetre()
        
        cadre_principal = ttk.Frame(self.root, padding="30 30 30 30")
        cadre_principal.pack(fill=tk.BOTH, expand=True)
        
        titre = self.Creer_Label_Stylise(
            cadre_principal, 
            "Annulation de l'Installation", 
            fonte=('Segoe UI', 16, 'bold'), 
            couleur=self.colors.primary
        )
        titre.pack(pady=(0, 20))
        
        label_statut = self.Creer_Label_Stylise(
            cadre_principal, 
            "Veuillez patienter, toute l'operation est en cours d'annulation..."
        )
        label_statut.pack(pady=20)
        
        barre_progression = ttk.Progressbar(
            cadre_principal, 
            length=600, 
            mode='determinate', 
            maximum=100
        )
        barre_progression.pack(pady=20)

        def Annulation():
            for i in range(101):
                barre_progression['value'] = i
                self.root.update_idletasks()
                time.sleep(0.05)
            
            self.root.after(0, self.Creer_Interface_Sociales)

        threading.Thread(target=Annulation, daemon=True).start()

def main_client():
    root = tk.Tk()
    Samp_Client_R1_Voip(root)
    root.mainloop()

if __name__ == "__main__":
    main_client()