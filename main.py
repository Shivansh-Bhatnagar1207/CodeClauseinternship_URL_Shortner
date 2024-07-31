import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import pyshorteners

ctk.set_appearance_mode('System')
ctk.set_default_color_theme('green')

class App(ctk.CTk):
    def __init__(self):
        super().__init__()


        self.getURl = tk.StringVar()
        self.shortenURL = tk.StringVar()


        self.title("URL_SHORTNER")
        self.geometry(f'{500}x{650}')


        self.grid_columnconfigure(1,weight=1)

        self.main = ctk.CTkLabel(self,text='URL Shortner',font=ctk.CTkFont(size=25,weight='bold'))
        self.main.grid(row=0 ,column=1,pady=(20,10))
        self.heading = ctk.CTkLabel(self,text="Enter The full URL:",font = ctk.CTkFont(size=20,weight='bold'))
        self.heading.grid(row=1,column=1,pady=20)
        self.url = ctk.CTkEntry(self,placeholder_text="Enter URL")
        self.url.insert(0,'')
        self.url.grid(row=2,column=1,pady=20)
        self.btn = ctk.CTkButton(self,text='Generate Shorter URL',command=self.generate)
        self.btn.grid(row=3,column=1,pady=(20,80))
        

        self.appearance_mode_label = ctk.CTkLabel(self, text ='Appearance Mode:',font=ctk.CTkFont(size=20,weight='bold'))
        self.appearance_mode_label.grid(row=4,column =1,pady=10)
        self.appearance_mode_option = ctk.CTkOptionMenu(self, values=["System",'Light',"Dark"],command=self.theme)
        self.appearance_mode_option.grid(row=5,column=1,pady=10)
        self.scale_label = ctk.CTkLabel(self, text ='UI Scaling:',font=ctk.CTkFont(size=20,weight='bold'))
        self.scale_label.grid(row=6,column=1,pady=10)
        self.scale_option = ctk.CTkOptionMenu(self,values=["80%","90%",'100%',"110%","120%"],command=self.scale)
        self.scale_option.grid(row=7,column=1,pady=10)
        self.short = ctk.CTkEntry(self,placeholder_text='shorten url')
        self.short.grid(row=8,column=1,pady=20)
        self.copybtn = ctk.CTkButton(self,text='Copy to clipboard',command=self.copy)
        self.copybtn.grid(row=9,column=1,pady=10)

    def theme(self, new_theme:str):
        ctk.set_appearance_mode(new_theme)

    def scale(self,new_scale:str):
        new_scale_float = int(new_scale.replace("%",""))/100
        ctk.set_widget_scaling(new_scale_float)

    def generate(self):
        url = self.url.get()
        self.getURl.set(url)
        shortner = pyshorteners.Shortener()
        shortURL = shortner.tinyurl.short(url)
        self.shortenURL.set(shortURL)
        self.short.insert(0,shortURL)
    def copy(self):
        store = self.shortenURL.get()
        if len(store)==0:
            tk.messagebox.showerror('Error','Link cannot be copied')
        else:
            self.clipboard_clear()
            self.clipboard_append(store)
            tk.messagebox.showinfo('Copied',"Link Copied")
if __name__ == '__main__':
    app=App()
    app.mainloop()