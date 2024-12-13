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
class Client_Colors:
    background: str = '#1E1E1E'
    primary: str = '#3B8AFF'
    secondary: str = '#2C2C2C'
    text_primary: str = '#FFFFFF'
    text_secondary: str = '#A0A0A0'

class Samp_Client_DL_R1:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.Configure_Root()
        self.colors = Client_Colors()
        self.selected_folder = tk.StringVar(value="No folder has been selected yet")
        self.extracted_files = []
        self.Configure_Theme()
        self.Create_Initial_Interface()
        self.Configure_Window_Icon()

    def Configure_Window_Icon(self):
        base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
        icon_path = os.path.join(base_path, "icons", "spc.png")

        img = Image.open(icon_path)
        icon = ImageTk.PhotoImage(img)
        self.root.iconphoto(True, icon)

    def Configure_Root(self):
        self.root.title("Client DL R1 - SPC")
        self.root.geometry("700x500")
        self.root.resizable(True, True)

    def Configure_Theme(self):
        sv_ttk.set_theme("dark")
        self.root.configure(bg=self.colors.background)

    def Clear_Window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def Create_Styled_Label(
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

    def Create_Styled_Button(
        self, 
        parent, 
        text: str, 
        command: Callable, 
        style: str = 'Accent.TButton'
    ) -> ttk.Button:
        return ttk.Button(
            parent, 
            text=text, 
            command=command,
            style=style
        )

    def Create_Initial_Interface(self):
        self.Clear_Window()
        
        main_frame = ttk.Frame(self.root, padding="30 30 30 30")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        title = self.Create_Styled_Label(
            main_frame, 
            "Client DL R1 Installer SA:MP", 
            font=('Segoe UI', 20, 'bold'), 
            color=self.colors.primary
        )
        title.pack(pady=(0, 30))
        
        subtitle = self.Create_Styled_Label(
            main_frame, 
            "Installer for SA:MP (San Andreas Multiplayer) mod, version 0.3.7 DL R1"
        )
        subtitle.pack(pady=(0, 20))
        
        folder_frame = ttk.Frame(main_frame)
        folder_frame.pack(fill=tk.X, pady=10)
        
        folder_label = ttk.Label(
            folder_frame, 
            textvariable=self.selected_folder, 
            font=('Consolas', 10), 
            wraplength=500,
            foreground=self.colors.text_primary
        )
        folder_label.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 10))
        
        select_button = self.Create_Styled_Button(
            folder_frame, 
            "Select Folder", 
            self.Choose_Folder
        )
        select_button.pack(side=tk.RIGHT)

    def Choose_Folder(self):
        folder = filedialog.askdirectory(
            title="Select Grand Theft Auto San Andreas folder",
            initialdir=os.path.expanduser("~")
        )
        
        if folder:
            self.selected_folder.set(folder)
            self.Create_Interface_Folder_Verification()

    def Create_Interface_Folder_Verification(self):
        self.Clear_Window()
        
        main_frame = ttk.Frame(self.root, padding="30 30 30 30")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        title = self.Create_Styled_Label(
            main_frame, 
            "Verifying Folder", 
            font=('Segoe UI', 16, 'bold'), 
            color=self.colors.primary
        )
        title.pack(pady=(0, 20))
        
        status_label = self.Create_Styled_Label(
            main_frame, 
            "Checking if this is the correct GTA folder..."
        )
        status_label.pack(pady=20)
        
        error_label = ttk.Label(
            main_frame, 
            text="", 
            foreground="red", 
            font=('Segoe UI', 10)
        )
        error_label.pack(pady=10)
        
        progress_bar = ttk.Progressbar(
            main_frame, 
            length=600, 
            mode='determinate', 
            maximum=100
        )
        progress_bar.pack(pady=20)

        def Verification_Complete():
            folder = self.selected_folder.get()
            
            for i in range(101):
                progress_bar['value'] = i
                self.root.update_idletasks()
                time.sleep(0.05)
            
            def Show_Error(message):
                error_label.config(text=message)
                retry_button.pack()
            
            if not os.path.exists(folder):
                Show_Error("Error: The selected folder does not exist.")
                return

            if os.path.basename(folder) != "Grand Theft Auto San Andreas":
                Show_Error("Error: Invalid folder. Please select the correct GTA San Andreas folder.")
                return

            exe_path = os.path.join(folder, "gta_sa.exe")
            if not os.path.isfile(exe_path):
                Show_Error("Error: 'gta_sa.exe' file not found in the folder.")
                return
            
            self.root.after(0, self.Create_Interface_Client_Confirmation)

        def Try_Again():
            retry_button.pack_forget()
            error_label.config(text="")
            self.Create_Initial_Interface()

        retry_button = self.Create_Styled_Button(
            main_frame, 
            "Try Again", 
            Try_Again
        )

        threading.Thread(target=Verification_Complete, daemon=True).start()

    def Create_Interface_Client_Confirmation(self):
        self.Clear_Window()
        
        main_frame = ttk.Frame(self.root, padding="30 30 30 30")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        title = self.Create_Styled_Label(
            main_frame, 
            "Install Client", 
            font=('Segoe UI', 16, 'bold'), 
            color=self.colors.primary
        )
        title.pack(pady=(0, 20))
        
        subtitle = self.Create_Styled_Label(
            main_frame, 
            "Folder verified successfully. Do you want to proceed\nwith the DL R1 Client installation?"
        )
        subtitle.pack(pady=20)
        
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=20)
        
        proceed_button = self.Create_Styled_Button(
            button_frame, 
            "Proceed", 
            self.Start_Client_Installation, 
            'Accent.TButton'
        )
        proceed_button.pack(side=tk.LEFT, padx=10)
        
        cancel_button = self.Create_Styled_Button(
            button_frame, 
            "Cancel", 
            self.Cancel_Installation
        )
        cancel_button.pack(side=tk.LEFT, padx=10)

    def Start_Client_Installation(self):
        self.Clear_Window()
        
        main_frame = ttk.Frame(self.root, padding="30 30 30 30")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        title = self.Create_Styled_Label(
            main_frame, 
            "Installing Client DL R1", 
            font=('Segoe UI', 16, 'bold'), 
            color=self.colors.primary
        )
        title.pack(pady=(0, 20))
        
        status_label = self.Create_Styled_Label(
            main_frame, 
            "Installing Client, please wait..."
        )
        status_label.pack(pady=20)
        
        progress_bar = ttk.Progressbar(
            main_frame, 
            length=600, 
            mode='determinate', 
            maximum=100
        )
        progress_bar.pack(pady=20)
        
        file_label = ttk.Label(
            main_frame, 
            text="", 
            font=('Consolas', 10),
            foreground=self.colors.text_primary
        )
        file_label.pack(pady=10)

        def Client_Installation():
            zip_path = getattr(sys, "_MEIPASS", os.path.abspath("."))
            zip_file = os.path.join(zip_path, "archives", "samp-client-dl-r1.zip")
            
            destination_folder = self.selected_folder.get()

            with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                files = zip_ref.namelist()
                total_files = len(files)
                
                for i, file in enumerate(files, start=1):
                    file_label.config(text=f"Extracting: {os.path.basename(file)}")
                    progress_bar['value'] = (i / total_files) * 100
                    self.root.update_idletasks()
                    
                    zip_ref.extract(file, destination_folder)
                    self.extracted_files.append(file)
                    time.sleep(0.1)
            
            file_label.config(text="Installation completed!")
            progress_bar['value'] = 100
            self.root.update_idletasks()
            time.sleep(1)
            
            self.root.after(0, self.Show_Installation_Summary)
        
        threading.Thread(target=Client_Installation, daemon=True).start()

    def Show_Installation_Summary(self):
        self.Clear_Window()
        
        main_frame = ttk.Frame(self.root, padding="30 30 30 30")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        title = self.Create_Styled_Label(
            main_frame, 
            "Extracted Files", 
            font=('Segoe UI', 16, 'bold'), 
            color=self.colors.primary
        )
        title.pack(pady=(0, 20))
        
        scroll_frame = ttk.Frame(main_frame)
        scroll_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        
        canvas = tk.Canvas(scroll_frame)
        scrollbar = ttk.Scrollbar(scroll_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        for file in self.extracted_files:
            file_label = ttk.Label(
                scrollable_frame, 
                text=file, 
                font=('Consolas', 10)
            )
            file_label.pack(anchor='w', padx=10, pady=2)
        
        completed_button = self.Create_Styled_Button(
            main_frame, 
            "Completed", 
            self.Create_Interface_Socials, 
            'Accent.TButton'
        )
        completed_button.pack(pady=20)

    def Create_Interface_Socials(self):
        self.Clear_Window()
        
        main_frame = ttk.Frame(self.root, padding="30 30 30 30")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        title = self.Create_Styled_Label(
            main_frame, 
            "Socials", 
            font=('Segoe UI', 24, 'bold'), 
            color=self.colors.primary
        )
        title.pack(pady=(0, 40))
        
        social_links = [
            (" Discord SPC", "https://discord.gg/3fApZh66Tf", "discord.png"),
            (" Instagram", "https://www.instagram.com/spc.samp/", "instagram.png"),
            (" YouTube", "https://www.youtube.com/@spc-samp", "youtube.png"),
            (" TikTok", "https://www.tiktok.com/@spc.samp", "tiktok.png"),
            (" GitHub", "https://github.com/spc-samp", "github.png"),
        ]
        
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(expand=True)
        
        def Open_Link(link):
            webbrowser.open(link, new=2)
        
        def resize_icon(icon_path, size=(30, 30)):
            base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
            full_path = os.path.join(base_path, icon_path)
            
            image = Image.open(full_path)
            resized_image = image.resize(size, Image.LANCZOS)
            return ImageTk.PhotoImage(resized_image)
        
        for i in range(0, len(social_links), 2):
            line_frame = ttk.Frame(button_frame)
            line_frame.pack(fill=tk.X, pady=10)
            
            for j in range(2):
                if i + j < len(social_links):
                    name, link, icon_path = social_links[i + j]
                    
                    icon = resize_icon(os.path.join('icons', icon_path))
                    
                    social_button = ttk.Button(
                        line_frame, 
                        text=name, 
                        image=icon, 
                        compound=tk.LEFT,
                        command=lambda l=link: Open_Link(l)
                    )
                    social_button.image = icon
                    social_button.pack(side=tk.LEFT, padx=10, expand=True, fill=tk.X)
        
        close_button = ttk.Button(
            button_frame, 
            text="Close", 
            command=self.root.quit,
            style='Close.TButton'
        )
        close_button.pack(pady=10, padx=20, fill=tk.X)

        style = ttk.Style()
        style.configure(
            'Close.TButton', 
            background='red', 
            foreground='white', 
            font=('Segoe UI', 12)
        )

    def Cancel_Installation(self):
        self.Clear_Window()
        
        main_frame = ttk.Frame(self.root, padding="30 30 30 30")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        title = self.Create_Styled_Label(
            main_frame, 
            "Canceling Installation", 
            font=('Segoe UI', 16, 'bold'), 
            color=self.colors.primary
        )
        title.pack(pady=(0, 20))
        
        status_label = self.Create_Styled_Label(
            main_frame, 
            "Please wait, the entire operation is being canceled..."
        )
        status_label.pack(pady=20)
        
        progress_bar = ttk.Progressbar(
            main_frame, 
            length=600, 
            mode='determinate', 
            maximum=100
        )
        progress_bar.pack(pady=20)

        def Cancellation():
            for i in range(101):
                progress_bar['value'] = i
                self.root.update_idletasks()
                time.sleep(0.05)
            
            self.root.after(0, self.Create_Interface_Socials)

        threading.Thread(target=Cancellation, daemon=True).start()

def main_client():
    root = tk.Tk()
    Samp_Client_DL_R1(root)
    root.mainloop()

if __name__ == "__main__":
    main_client()