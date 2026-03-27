from customtkinter import *

class App(CTk):
    def __init__(self):
        super().__init__()
        self.height=1000
        self.width=1200
        self.geometry("1200x1000")
        self.title("Biblioteca Gutenberg")
        self.configure(fg_color="white")
        self.pag_principal()

    def pag_principal(self):
        tit ="CATÁLOGO GENERAL"
        self.titulo = CTkLabel(self, 
                                text=tit, 
                                fg_color="transparent", 
                                font=("Roboto",30,"bold"),
                                justify= "right",
                                compound="right"
                                )
        self.titulo.grid(row=1, column=1, padx=30, pady=5)

        subtxt = "Explora y gestione el inventario de la biblioteca académica"
        self.subtitulo = CTkLabel(self, 
                                    text=subtxt, 
                                    fg_color="transparent", 
                                    font=("Open Sans",14),
                                    justify= "left",
                                    compound="left"
                                    )
        self.subtitulo.grid(row=2, column=1, padx=30, pady=5)

        self.btt = CTkButton(self, 
                       text="+ Agregar libro", 
                       command=self.button_click,
                       fg_color="black"
                       )

        self.btt.grid(row=1, column=2, padx=30, pady=5)
        src_txt="Texto de prueba..."
        self.buscador = CTkEntry(self,
                                 width=self.width*0.8,
                                 height=30,
                                 placeholder_text=src_txt
                                 )
        self.buscador.grid(row=3,column=1, padx=30, pady=5)

        self.btt_buscar = CTkButton(self, 
                       text="Buscar", 
                       command=self.entry_handler,
                       fg_color="black"
                       )

        self.btt_buscar.grid(row=3, column=2, padx=30, pady=5)
        

        
    def button_click(self):
        print("button click")

    
    def entry_handler(self):
        print(f"EL contenido es: {self.buscador.get()}")


app = App()
set_appearance_mode("light")

app.mainloop()