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
class Client_Colores:
    background: str = '#1E1E1E'
    primary: str = '#3B8AFF'
    secondary: str = '#2C2C2C'
    text_primary: str = '#FFFFFF'
    text_secondary: str = '#A0A0A0'

class Samp_Client_R2:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.Configurar_Raiz()
        self.colors = Client_Colores()
        self.carpeta_seleccionada = tk.StringVar(value="Ninguna carpeta ha sido seleccionada aun")
        self.archivos_extraidos = []
        self.Configurar_Tema()
        self.Crear_Interfaz_Inicial()
        self.Configurar_IconVentana()

    def Configurar_IconVentana(self):
        base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
        icon_path = os.path.join(base_path, "icons", "spc.png")

        img = Image.open(icon_path)
        icon = ImageTk.PhotoImage(img)
        self.root.iconphoto(True, icon)

    def Configurar_Raiz(self):
        self.root.title("Client R2 - SPC")
        self.root.geometry("700x500")
        self.root.resizable(True, True)

    def Configurar_Tema(self):
        sv_ttk.set_theme("dark")
        self.root.configure(bg=self.colors.background)

    def Limpiar_Ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def Crear_Etiqueta_Estilizada(
        self, 
        parent, 
        texto: str, 
        fuente: tuple = ('Segoe UI', 12), 
        color: Optional[str] = None
    ) -> ttk.Label:
        return ttk.Label(
            parent, 
            text=texto, 
            font=fuente,
            foreground=color or self.colors.text_secondary
        )

    def Crear_Boton_Estilizado(
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

    def Crear_Interfaz_Inicial(self):
        self.Limpiar_Ventana()
        
        cuadro_principal = ttk.Frame(self.root, padding="30 30 30 30")
        cuadro_principal.pack(fill=tk.BOTH, expand=True)
        
        titulo = self.Crear_Etiqueta_Estilizada(
            cuadro_principal, 
            "Instalador Client R2 SA:MP", 
            fuente=('Segoe UI', 20, 'bold'), 
            color=self.colors.primary
        )
        titulo.pack(pady=(0, 30))
        
        subtitulo = self.Crear_Etiqueta_Estilizada(
            cuadro_principal, 
            "Instalador del mod SA:MP (San Andreas Multiplayer), versión 0.3.7 R2"
        )
        subtitulo.pack(pady=(0, 20))
        
        frame_carpeta = ttk.Frame(cuadro_principal)
        frame_carpeta.pack(fill=tk.X, pady=10)
        
        carpeta_label = ttk.Label(
            frame_carpeta, 
            textvariable=self.carpeta_seleccionada, 
            font=('Consolas', 10), 
            wraplength=500,
            foreground=self.colors.text_primary
        )
        carpeta_label.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 10))
        
        boton_seleccionar = self.Crear_Boton_Estilizado(
            frame_carpeta, 
            "Seleccionar Carpeta", 
            self.Elegir_Carpeta
        )
        boton_seleccionar.pack(side=tk.RIGHT)

    def Elegir_Carpeta(self):
        carpeta = filedialog.askdirectory(
            title="Seleccione la carpeta de Grand Theft Auto San Andreas",
            initialdir=os.path.expanduser("~")
        )
        
        if carpeta:
            self.carpeta_seleccionada.set(carpeta)
            self.Crear_Interfaz_Verificacion_Carpeta()

    def Crear_Interfaz_Verificacion_Carpeta(self):
        self.Limpiar_Ventana()
        
        cuadro_principal = ttk.Frame(self.root, padding="30 30 30 30")
        cuadro_principal.pack(fill=tk.BOTH, expand=True)
        
        titulo = self.Crear_Etiqueta_Estilizada(
            cuadro_principal, 
            "Verificando Carpeta", 
            fuente=('Segoe UI', 16, 'bold'), 
            color=self.colors.primary
        )
        titulo.pack(pady=(0, 20))
        
        status_label = self.Crear_Etiqueta_Estilizada(
            cuadro_principal, 
            "Verificando si esta es la carpeta correcta de su GTA..."
        )
        status_label.pack(pady=20)
        
        error_label = ttk.Label(
            cuadro_principal, 
            text="", 
            foreground="red", 
            font=('Segoe UI', 10)
        )
        error_label.pack(pady=10)
        
        barra_progreso = ttk.Progressbar(
            cuadro_principal, 
            length=600, 
            mode='determinate', 
            maximum=100
        )
        barra_progreso.pack(pady=20)

        def Verificacion_Completa():
            carpeta = self.carpeta_seleccionada.get()
            
            for i in range(101):
                barra_progreso['value'] = i
                self.root.update_idletasks()
                time.sleep(0.05)
            
            def Mostrar_Error(mensaje):
                error_label.config(text=mensaje)
                boton_intentar_nuevamente.pack()
            
            if not os.path.exists(carpeta):
                Mostrar_Error("Error: La carpeta seleccionada no existe.")
                return

            if os.path.basename(carpeta) != "Grand Theft Auto San Andreas":
                Mostrar_Error("Error: Carpeta inválida. Seleccione la carpeta correcta de GTA San Andreas (Grand Theft Auto San Andreas).")
                return

            ruta_exe = os.path.join(carpeta, "gta_sa.exe")
            if not os.path.isfile(ruta_exe):
                Mostrar_Error("Error: El archivo 'gta_sa.exe' no se encontró en la carpeta.")
                return
            
            self.root.after(0, self.Crear_Interfaz_Confirmacion_Client)

        def Intentar_Nuevamente():
            boton_intentar_nuevamente.pack_forget()
            error_label.config(text="")
            self.Crear_Interfaz_Inicial()

        boton_intentar_nuevamente = self.Crear_Boton_Estilizado(
            cuadro_principal, 
            "Intentar de Nuevo", 
            Intentar_Nuevamente
        )

        threading.Thread(target=Verificacion_Completa, daemon=True).start()

    def Crear_Interfaz_Confirmacion_Client(self):
        self.Limpiar_Ventana()
        
        cuadro_principal = ttk.Frame(self.root, padding="30 30 30 30")
        cuadro_principal.pack(fill=tk.BOTH, expand=True)
        
        titulo = self.Crear_Etiqueta_Estilizada(
            cuadro_principal, 
            "Instalar Client", 
            fuente=('Segoe UI', 16, 'bold'), 
            color=self.colors.primary
        )
        titulo.pack(pady=(0, 20))
        
        subtitulo = self.Crear_Etiqueta_Estilizada(
            cuadro_principal, 
            "Carpeta verificada con éxito. ¿Desea continuar con la instalación\ndel Client R2?"
        )
        subtitulo.pack(pady=20)
        
        frame_botones = ttk.Frame(cuadro_principal)
        frame_botones.pack(pady=20)
        
        boton_continuar = self.Crear_Boton_Estilizado(
            frame_botones, 
            "Continuar", 
            self.Iniciar_Instalacion_Client, 
            'Accent.TButton'
        )
        boton_continuar.pack(side=tk.LEFT, padx=10)
        
        boton_cancelar = self.Crear_Boton_Estilizado(
            frame_botones, 
            "Cancelar", 
            self.Cancelar_Instalacion
        )
        boton_cancelar.pack(side=tk.LEFT, padx=10)

    def Iniciar_Instalacion_Client(self):
        self.Limpiar_Ventana()
        
        cuadro_principal = ttk.Frame(self.root, padding="30 30 30 30")
        cuadro_principal.pack(fill=tk.BOTH, expand=True)
        
        titulo = self.Crear_Etiqueta_Estilizada(
            cuadro_principal, 
            "Instalando Client R2", 
            fuente=('Segoe UI', 16, 'bold'), 
            color=self.colors.primary
        )
        titulo.pack(pady=(0, 20))
        
        status_label = self.Crear_Etiqueta_Estilizada(
            cuadro_principal, 
            "Instalando Client, por favor espere..."
        )
        status_label.pack(pady=20)
        
        barra_progreso = ttk.Progressbar(
            cuadro_principal, 
            length=600, 
            mode='determinate', 
            maximum=100
        )
        barra_progreso.pack(pady=20)
        
        archivo_label = ttk.Label(
            cuadro_principal, 
            text="", 
            font=('Consolas', 10),
            foreground=self.colors.text_primary
        )
        archivo_label.pack(pady=10)

        def Instalacion_Client():
            ruta_zip = getattr(sys, "_MEIPASS", os.path.abspath("."))
            archivo_zip = os.path.join(ruta_zip, "archives", "samp-client-r2.zip")
            
            carpeta_destino = self.carpeta_seleccionada.get()

            with zipfile.ZipFile(archivo_zip, 'r') as zip_ref:
                archivos = zip_ref.namelist()
                total_archivos = len(archivos)
                
                for i, archivo in enumerate(archivos, start=1):
                    archivo_label.config(text=f"Extrayendo: {os.path.basename(archivo)}")
                    barra_progreso['value'] = (i / total_archivos) * 100
                    self.root.update_idletasks()
                    
                    zip_ref.extract(archivo, carpeta_destino)
                    self.archivos_extraidos.append(archivo)
                    time.sleep(0.1)
            
            archivo_label.config(text="¡Instalación completada!")
            barra_progreso['value'] = 100
            self.root.update_idletasks()
            time.sleep(1)
            
            self.root.after(0, self.Mostrar_Resumen_Instalacion)
        
        threading.Thread(target=Instalacion_Client, daemon=True).start()

    def Mostrar_Resumen_Instalacion(self):
        self.Limpiar_Ventana()
        
        cuadro_principal = ttk.Frame(self.root, padding="30 30 30 30")
        cuadro_principal.pack(fill=tk.BOTH, expand=True)
        
        titulo = self.Crear_Etiqueta_Estilizada(
            cuadro_principal, 
            "Archivos Extraidos", 
            fuente=('Segoe UI', 16, 'bold'), 
            color=self.colors.primary
        )
        titulo.pack(pady=(0, 20))
        
        frame_desplazamiento = ttk.Frame(cuadro_principal)
        frame_desplazamiento.pack(fill=tk.BOTH, expand=True, pady=20)
        
        canvas = tk.Canvas(frame_desplazamiento)
        scrollbar = ttk.Scrollbar(frame_desplazamiento, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        for archivo in self.archivos_extraidos:
            label_archivo = ttk.Label(
                scrollable_frame, 
                text=archivo, 
                font=('Consolas', 10)
            )
            label_archivo.pack(anchor='w', padx=10, pady=2)
        
        boton_completado = self.Crear_Boton_Estilizado(
            cuadro_principal, 
            "Completado", 
            self.Crear_Interfaz_Sociales, 
            'Accent.TButton'
        )
        boton_completado.pack(pady=20)

    def Crear_Interfaz_Sociales(self):
        self.Limpiar_Ventana()
        
        cuadro_principal = ttk.Frame(self.root, padding="30 30 30 30")
        cuadro_principal.pack(fill=tk.BOTH, expand=True)
        
        titulo = self.Crear_Etiqueta_Estilizada(
            cuadro_principal, 
            "Sociales", 
            fuente=('Segoe UI', 24, 'bold'), 
            color=self.colors.primary
        )
        titulo.pack(pady=(0, 40))
        
        enlaces_sociales = [
            (" Discord SPC", "https://discord.gg/3fApZh66Tf", "discord.png"),
            (" Instagram", "https://www.instagram.com/spc.samp/", "instagram.png"),
            (" YouTube", "https://www.youtube.com/@spc-samp", "youtube.png"),
            (" TikTok", "https://www.tiktok.com/@spc.samp", "tiktok.png"),
            (" GitHub", "https://github.com/spc-samp", "github.png"),
        ]
        
        frame_botones = ttk.Frame(cuadro_principal)
        frame_botones.pack(expand=True)
        
        def Abrir_Enlace(enlace):
            webbrowser.open(enlace, new=2)
        
        def redimensionar_icono(ruta_icono, tamano=(30, 30)):
            base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
            ruta_completa = os.path.join(base_path, ruta_icono)
            
            imagen = Image.open(ruta_completa)
            imagen_redimensionada = imagen.resize(tamano, Image.LANCZOS)
            return ImageTk.PhotoImage(imagen_redimensionada)
        
        for i in range(0, len(enlaces_sociales), 2):
            frame_linea = ttk.Frame(frame_botones)
            frame_linea.pack(fill=tk.X, pady=10)
            
            for j in range(2):
                if i + j < len(enlaces_sociales):
                    nombre, enlace, ruta_icono = enlaces_sociales[i + j]
                    
                    icono = redimensionar_icono(os.path.join('icons', ruta_icono))
                    
                    boton_social = ttk.Button(
                        frame_linea, 
                        text=nombre, 
                        image=icono, 
                        compound=tk.LEFT,
                        command=lambda l=enlace: Abrir_Enlace(l)
                    )
                    boton_social.image = icono
                    boton_social.pack(side=tk.LEFT, padx=10, expand=True, fill=tk.X)
        
        boton_cerrar = ttk.Button(
            frame_botones, 
            text="Cerrar", 
            command=self.root.quit,
            style='Cerrar.TButton'
        )
        boton_cerrar.pack(pady=10, padx=20, fill=tk.X)

        style = ttk.Style()
        style.configure(
            'Cerrar.TButton', 
            background='red', 
            foreground='white', 
            font=('Segoe UI', 12)
        )

    def Cancelar_Instalacion(self):
        self.Limpiar_Ventana()
        
        cuadro_principal = ttk.Frame(self.root, padding="30 30 30 30")
        cuadro_principal.pack(fill=tk.BOTH, expand=True)
        
        titulo = self.Crear_Etiqueta_Estilizada(
            cuadro_principal, 
            "Cancelando Instalación", 
            fuente=('Segoe UI', 16, 'bold'), 
            color=self.colors.primary
        )
        titulo.pack(pady=(0, 20))
        
        status_label = self.Crear_Etiqueta_Estilizada(
            cuadro_principal, 
            "Espere, toda la operación se está cancelando..."
        )
        status_label.pack(pady=20)
        
        barra_progreso = ttk.Progressbar(
            cuadro_principal, 
            length=600, 
            mode='determinate', 
            maximum=100
        )
        barra_progreso.pack(pady=20)

        def Cancelamiento():
            for i in range(101):
                barra_progreso['value'] = i
                self.root.update_idletasks()
                time.sleep(0.05)
            
            self.root.after(0, self.Crear_Interfaz_Sociales)

        threading.Thread(target=Cancelamiento, daemon=True).start()

def main_client():
    root = tk.Tk()
    Samp_Client_R2(root)
    root.mainloop()

if __name__ == "__main__":
    main_client()