from customtkinter import *

class ToplevelWindow(CTkToplevel):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Agregar Libro")
        self.configure(fg_color="white")

        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        self.geometry(f"{self.screen_width}x{self.screen_height}+0+0")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=8)
        self.grid_columnconfigure(2, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=30)
        self.grid_rowconfigure(2, weight=1)

        self.div_agregar()
        self.top_bar()
        

    def top_bar(self):

        self.back = CTkButton(self, 
                             text=" < Atrás", 
                             command=self.go_back,
                             fg_color="transparent",
                             text_color="black",
                             height=36,
                             corner_radius=0,
                             font=("Open Sans",14),
                             )

        self.back.grid(row=0, column=0, padx=20, pady=(15,0),sticky="n")

        CTkFrame(self,
                 height=2,
                 fg_color="#DEE1E6").grid(row=0,
                                          column=0,
                                          columnspan=3,
                                          sticky="ew", 
                                          padx=0, 
                                          pady=(40, 0))

    def div_agregar(self):

        self.agregar_frame = CTkFrame(self, 
                                   fg_color="white", 
                                   corner_radius=0,
                                   border_color="#DEE1E6",
                                   border_width=1,
                                   )
        self.agregar_frame.grid(row=1, 
                                column=0, 
                                columnspan=3,
                                padx=150, 
                                pady=(10,400),  
                                sticky="nesw")

        self.agregar_frame.grid_columnconfigure(0, weight=6)
        self.agregar_frame.grid_columnconfigure(1, weight=2)

        for i in range(3):
            self.agregar_frame.grid_rowconfigure(i, weight=0)
        self.agregar_frame.grid_rowconfigure(3, weight=1)

        title = "AGREGAR LIBRO DESDE PROJECT GUTENBERG"

        CTkLabel(self.agregar_frame,
                 text=title,
                 fg_color="transparent",
                 font=("Roboto",30,"bold"),
                 anchor="w").grid(row=0,
                                  column=0, 
                                  padx=30, 
                                  pady=(20,5),
                                  sticky="w")

        CTkFrame(self.agregar_frame,
                 height=2,
                 fg_color="#DEE1E6",
                 ).grid(row=0, 
                        column=0,  
                        columnspan=2,
                        sticky="ew", 
                        padx=30, 
                        pady=(60, 0))
        
        self.div_info()
        self.div_input()
        self.div_bot()
        
    def div_info(self):
        self.info_frame = CTkFrame(self.agregar_frame, 
                                   fg_color="transparent", 
                                   corner_radius=0,
                                   border_width=1,
                                   border_color="#DEE1E6"
                                   )
        self.info_frame.grid(row=1, column=0, columnspan=3,padx=30, pady=(20,0),  sticky="nsew")

        self.info_frame.grid_columnconfigure(0, weight=6)
        self.info_frame.grid_columnconfigure(1, weight=2)

        texto = (
            "Ingrese la dirección URL completa del libro electrónico de Project Gutenberg.\n"
            "El sistema extraerá automáticamente el título, autor, idioma y contenido preliminar."
        )
        
        CTkLabel(self.info_frame,
                 text=texto, 
                 fg_color="transparent",
                 font=("Open Sans",14,"italic"),
                 text_color="#565D6D",
                 justify="left",
                 anchor="center"
                 ).grid(row=0, 
                        column=0,
                        columnspan=2, 
                        padx=30, 
                        pady=20,
                        sticky="nsew")

    def div_input(self):
        self.input_frame = CTkFrame(self.agregar_frame, 
                                   fg_color="white", 
                                   corner_radius=0,
                                   )
        self.input_frame.grid(row=2, column=0, columnspan=3,padx=30, pady=(5,0),  sticky="nsew")

        self.input_frame.grid_columnconfigure(0, weight=6)
        self.input_frame.grid_columnconfigure(1, weight=2)

        labeltxt = "URL de Project Gutenberg"
        
        CTkLabel(self.input_frame,
                 text=labeltxt,
                 fg_color="transparent",
                 font=("Open Sans",14,"bold"),
                 anchor="w"
                 ).grid(row=1,
                        column=0,
                        columnspan=2,
                        padx=2,
                        pady=(10, 0),
                        sticky="w")

        src_txt="https://www.gutenberg.org/ebooks/12345"

        self.url = CTkEntry(self.input_frame,
                                 height=40,
                                 placeholder_text=src_txt,
                                 corner_radius=0,
                                 border_color="#9CA3AF",
                                 fg_color="white",

                                 )
        self.url.grid(row=3, column=0, columnspan=2,pady=5, sticky="ew")

    def div_bot(self):
        self.bot_frame = CTkFrame(self.agregar_frame, 
                                   fg_color="transparent", 
                                   corner_radius=0,
                                   )
        self.bot_frame.grid(row=3, column=0, columnspan=3,padx=30, pady=(0,5),  sticky="nsew")

        self.bot_frame.grid_columnconfigure(0, weight=0)
        self.bot_frame.grid_columnconfigure(1, weight=1)

        self.bot_frame.grid_rowconfigure(0, weight=0)
        self.bot_frame.grid_rowconfigure(1, weight=0)

        self.line = CTkFrame(self.bot_frame,
                              height=2,
                              fg_color="#DEE1E6",
                              )
        self.line.grid(row=0, 
                        column=0,  
                        columnspan=3,
                        sticky="ew", 
                        pady=(5, 0))
        
        CTkButton(self.bot_frame,
                  text="Obtener Información",
                  command=self.obtener_info,
                  fg_color="black",
                  height=40,
                  corner_radius=0,
                  width=200,
                  font=("Open Sans",14),
                  ).grid(row=1, column=0, pady=(10,0),sticky="w")

        CTkButton(self.bot_frame, 
                  text="Cancelar", 
                  command=self.cancelar,
                  fg_color="white",
                  border_color="#DEE1E6",
                  text_color="black",
                  height=40,
                  border_width=1,
                  corner_radius=0,
                  width=200,
                  font=("Open Sans",14),
                  ).grid(row=1, column=1,padx=10, pady=(10,0),sticky="w")

    def go_back(self):
        print("atrás")

    def obtener_info(self):
        print(f"Url ingresada {self.url.get()}")

    def cancelar(self):
        print("Cancelar")