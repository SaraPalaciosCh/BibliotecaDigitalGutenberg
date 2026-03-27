from customtkinter import *
from agregar import ToplevelWindow

class App(CTk):
    def __init__(self):
        super().__init__()
        self.title("Biblioteca Gutenberg")
        self.configure(fg_color="white")

        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        self.geometry(f"{self.screen_width}x{self.screen_height}+0+0")

        # Armamos una grid 3x3
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=8)
        self.grid_columnconfigure(2, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=20)
        self.grid_rowconfigure(2, weight=1)

        self.pag_principal()

        self.toplevel_window = None


    def pag_principal(self):

        self.main_frame = CTkFrame(self, fg_color="white", corner_radius=0)
        self.main_frame.grid(row=1, column=1, sticky="nsew")

        self.main_frame.grid_columnconfigure(0, weight=6)
        self.main_frame.grid_columnconfigure(1, weight=2)

        for i in range(4):
            self.main_frame.grid_rowconfigure(i, weight=0)
        self.main_frame.grid_rowconfigure(4, weight=1)

        title ="CATÁLOGO GENERAL"
        self.titulo = CTkLabel(self.main_frame, 
                                text=title, 
                                fg_color="transparent", 
                                font=("Roboto",30,"bold"),
                                anchor="w"
                                )
        self.titulo.grid(row=0, column=0, padx=30, pady=(20,5),sticky="w")

        subtxt = "Explora y gestione el inventario de la biblioteca académica"
        self.subtitulo = CTkLabel(self.main_frame, 
                                    text=subtxt, 
                                    fg_color="transparent", 
                                    font=("Open Sans",14),
                                    anchor="w"
                                    )
        self.subtitulo.grid(row=1, 
                            column=0, 
                            columnspan=2, 
                            padx=30, 
                            pady=(0, 10), 
                            sticky="w")

        self.btt = CTkButton(self.main_frame, 
                             text="+ Agregar libro", 
                             command=self.open_win,
                             fg_color="black",
                             height=40,
                             corner_radius=0,
                             font=("Open Sans",14),
                             )

        self.btt.grid(row=0, column=1, padx=30, pady=(20,5),sticky="e")

        self.linea = CTkFrame(self.main_frame,
                              height=2,
                              fg_color="#DEE1E6",
                              )
        self.linea.grid(row=2, 
                        column=0, 
                        columnspan=2, 
                        sticky="ew", 
                        padx=30, 
                        pady=(0, 20))

        src_txt="Texto de prueba..."

        self.buscador = CTkEntry(self.main_frame,
                                 height=40,
                                 placeholder_text=src_txt,
                                 corner_radius=0,
                                 border_color="#DEE1E6",
                                 fg_color="white",

                                 )
        self.buscador.grid(row=3, column=0, padx=(30, 10), pady=5, sticky="ew")


        self.btt_buscar = CTkButton(self.main_frame,
                                    text="Buscar",
                                    command=self.entry_handler,
                                    fg_color="black",
                                    width=120,
                                    height=40,
                                    corner_radius=0,
                                    font=("Open Sans",14),
                                    )
        self.btt_buscar.grid(row=3, column=1, padx=(0, 30), pady=5, sticky="w")
        self.tabla()
        

    def tabla(self):
        self.table_frame = CTkFrame(self.main_frame, 
                                    fg_color="white", 
                                    border_color="#DEE1E6",
                                    border_width=1,
                                    corner_radius=0)
        self.table_frame.grid(row=4, column=0,columnspan=2, sticky="nsew", padx=30, pady=20)

        # Me divide el frame en 4 columnas (las mismas de la tabla)
        self.table_frame.grid_columnconfigure(0, weight=4)  # título
        self.table_frame.grid_columnconfigure(1, weight=3)  # autor
        self.table_frame.grid_columnconfigure(2, weight=2)  # estado
        self.table_frame.grid_columnconfigure(3, weight=2)  # acciones

        headers = ["TÍTULO DEL LIBRO","AUTOR","ESTADO","ACCIONES"]

        for i in range(4):
            CTkLabel(self.table_frame, 
                     text=headers[i], 
                     font=("Roboto", 14, "bold")).grid(row=0, 
                                                       column=i, 
                                                       sticky="w", 
                                                       padx=10, 
                                                       pady=10)


    def open_win(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  
        else:
            self.toplevel_window.focus()  


    def button_click(self):
        print("button click")

    
    def entry_handler(self):
        print(f"EL contenido es: {self.buscador.get()}")


app = App()
set_appearance_mode("light")

app.mainloop()