import re
import os
import requests
import datetime as dt

class Usuario:
    def __init__(self, nombre, correo, numero):
        self.nombre = nombre
        self.correo = correo
        self.numero = numero

    
    def getNombre(self):
        return self.nombre
    
    
    def getCorreo(self):
        return self.correo
    
    
    def getNumero(self):
        return self.numero
    
    
    def __del__(self):
        print(f"Usuario {self.nombre} destruido, liberando recursos.\n")
        
class Libro:
    def __init__(self, url = None, path = None):
        if path == None:
            self.crearURL(url)
        else:
            self.crearPath(path)

    
    def crearPath(self, path):
        try:
            if "Libros/" not in path:
                raise Exception("ERROR: Dirección invalida :(")
            else:
                try:
                    with open(path,"r",encoding="utf-8") as a:
                        text = a.read()
                    
                    author = re.search(r'(Author:)\s+\w+.+\n', text, flags=re.IGNORECASE).group(0).split(":")[1]
                    title = re.search(r'(Title:)\s+\w+.+\n', text, flags=re.IGNORECASE).group(0).split(":")[1].strip()
                    release_date = re.search(r'(Release date:)\s+\w+.+\[', text, flags=re.IGNORECASE).group(0).split(":")[1][:-1]
                    language = re.search(r'(Language:)\s+\w+.+\n', text, flags=re.IGNORECASE).group(0).split(":")[1]
                    url = re.search(r'(URL=)\s+\w+.+\n', text, flags=re.IGNORECASE).group(0).split("=")[1]

                    self.autor = author
                    self.titulo = title
                    self.fecha_lanzamiento = release_date
                    self.idioma = language
                    self.url = url

                    if not os.path.exists("Libros/"):
                        os.makedirs("Libros/")

                    doc_name= "Libros/"+title.replace(" ","_")+".txt"

                    with open(doc_name, "w", encoding="utf-8") as f:
                        f.write(text)

                    self.path = doc_name
                    self.usuario = None
                    self.disponible = True
                    self.fecha_prestamo = None
                    self.fecha_devolucion = None

                    print(f"Se creo correctamente el Libro:\n\tTitulo: {title}\n\tRuta: {doc_name}\n")
                except Exception as e:
                    raise Exception(e)    
        except Exception as e:
            raise SystemExit(f"ERROR: No se pudo crear libro usando path \n\t -- {e} --")
                

    def crearURL(self, url):
        try:
            if "https://www.gutenberg.org/cache/epub" not in url:
                raise Exception("ERROR: URL invalida :(")
            else:
                r = requests.get(url)
                if r.status_code in range(400,499):
                    raise Exception("ERROR: no se pudo consultar la URL")
                elif r.status_code == 200:
                    text = r.text 
                    author = re.search(r'(Author:)\s+\w+.+\n', text, flags=re.IGNORECASE).group(0).split(":")[1]
                    title = re.search(r'(Title:)\s+\w+.+\n', text, flags=re.IGNORECASE).group(0).split(":")[1].strip()
                    release_date = re.search(r'(Release date:)\s+\w+.+\[', text, flags=re.IGNORECASE).group(0).split(":")[1][:-1]
                    language = re.search(r'(Language:)\s+\w+.+\n', text, flags=re.IGNORECASE).group(0).split(":")[1]
                    self.autor = author
                    self.titulo = title
                    self.fecha_lanzamiento = release_date
                    self.idioma = language
                    self.url = url

                    if not os.path.exists("Libros/"):
                        os.makedirs("Libros/")

                    doc_name= "Libros/"+title.replace(" ","_")+".txt"

                    with open(doc_name, "w", encoding="utf-8") as f:
                        text = f"URL= {url}\n" + text
                        f.write(text)
                    self.path = doc_name
                    self.usuario = None
                    self.disponible = True
                    self.fecha_prestamo = None
                    self.fecha_devolucion = None

                    print(f"Se creo correctamente el Libro:\n\tTitulo: {title}\n\tRuta: {doc_name}\n")
                else:
                    raise Exception("ERROR: algo salio mal :(")
        except Exception as e:
            raise SystemExit(f"ERROR: No se pudo crear libro usando la URL\n\t -- {e} --")
        
    
    def getTitulo(self):
        return self.titulo
    
    
    def getAutor(self):
        return self.autor
    
    
    def getFechaLanzamiento(self):
        return self.fecha_lanzamiento
    
    
    def getIdioma(self):
        return self.idioma
    
    
    def getUrl(self):
        return self.url
    
    
    def getPath(self):
        return self.path
    
    
    def getDisponible(self):
        return self.disponible
    
    
    def getFechaPrestamo(self):
        return self.fecha_prestamo
    
    
    def getFechaDevolucion(self):
        return self.fecha_devolucion
    
    
    def cambiarDisponibilidad(self):
        if self.disponible: 
            self.disponible = False
        else:
            self.disponible = True

    
    def setFechaPestramo(self, fecha):
        try:
            if self.disponible:
                self.fecha_prestamo = fecha
            else:
                raise Exception("ERROR: Libro no disponible! :(")
        except Exception as e:
            raise SystemError(f"\n{e}\n")
        
    
    def setFechaDevolucion(self, fecha):
        try:
            if self.disponible:
                self.fecha_devolucion = fecha
            else:
                raise Exception("ERROR: Libro no disponible! :(")
        except Exception as e:
            raise SystemError(f"\n{e}\n")


    def setUsuario(self, usuario):
        try:
            if self.disponible:
                self.usuario = usuario
            else:
                raise Exception("ERROR: Libro no disponible! :(")
        except Exception as e:
            raise SystemError(f"\n{e}\n")
    

    def __str__(self):
        return f"Titulo: {self.titulo}\nAutor: {self.autor}\nFecha de Lanzamiento: {self.fecha_lanzamiento}\nIdioma: {self.idioma}\nURL: {self.url}\nPath: {self.path}\nDisponible: {self.disponible}\nFecha de Prestamo: {self.fecha_prestamo}\nFecha de Devolucion: {self.fecha_devolucion}\n"
    
    
    def __del__(self):
        print(f"Estas quemando el conocimiento :(")
        print(f"El libro '{self.titulo}' ha sido destruido, liberando recursos...\n")
    
class Biblioteca:
    def __init__(self, nombre = "Biblioteca de Alejandria"):
        self.nombreB = nombre
        self.libros = {}
        self.inventario = {}


    def agregarLibro(self, libro):
        try:
            url = libro.getUrl()
            codigo = url.split("/")[5]
            titulo = libro.getTitulo()
            if codigo in list(self.libros.keys()):
                raise Exception(f"El libro '{titulo}' con el codigo #{codigo} ya existe")
            else:
                self.libros[codigo] = libro
                self.inventario[titulo] = codigo
                print(f"Se añadio correctamente el Libro:\n\tTitulo: {titulo}\n\tCodigo: {codigo}\n\tBiblioteca: {self.nombreB}\n")
                
        except Exception as e:
            raise SystemError(f"\n{e}\n")

    
    def eliminarLibro(self, codigo):
        try:
            libro = self.libros[codigo]
            archivo = libro.getPath()
            if os.path.exists(archivo):
                os.remove(archivo)
                del self.libros[codigo]
                print(f"El libro #{codigo} ha sido eliminado.\n")
            else:
                raise Exception("ERROR: El libro #{codigo} no existe")
        except Exception as e:
            raise SystemError(f"\n{e}\n")

    
    def buscarLibro(self, codigo):
        try:
            return self.libros[codigo]
        except KeyError:
            raise Exception(f"ERROR: No existe el libro #{codigo}")
        except Exception as e:
            raise SystemError(f"\n{e}\n")
        
    
    def buscarCodigo(self, titulo):
        try:
            codigo = self.inventario[titulo]
            return codigo
        except KeyError:
            raise Exception(f"ERROR: No existe el libro '{titulo}'")
        except Exception as e:
            raise SystemError(f"\n{e}\n")
        
    
    def mostrarBiblioteca(self):
        print(f"Bienvenido a la {self.nombreB}")
        print("Tenemos los siguientes libros disponibles:\n")

        for codigo, libro in self.libros.items():
            print("="*30)
            print(f"Libro #{codigo}: \n")
            print(libro)
            print("="*30)
            print("\n")

    
    def __del__(self):
        print(f"ALEJANDRIA 2.0!! SE INCENDIA LA BIBLIOTECA!!")
        print(f"HAS DESTRUIDO EL CONOCIMIENTO :( !!, liberando recursos...\n")

class Prestamo:
    def __init__(self, biblioteca, titulo, usuario):
        self.titulo = titulo
        self.usuario = usuario
        self.biblioteca = biblioteca

    def prestarLibro(self):
        libro, disp = self.revisarDisponibilidad()
        if disp:
            hoy = dt.date.today()
            entrega = dt.timedelta(days=15)

            libro.setFechaPestramo(hoy)
            libro.setFechaDevolucion(entrega)
            libro.setUsuario(self.usuario)
            libro.cambiarDisponibilidad()

            print("Se ha realizado el prestamo exitosamente.\n")
        else:
            raise Exception(f"El libro {self.titulo} NO esta disponble.\n")
        
        
    def devolverLibro(self):
        libro, disp = self.revisarDisponibilidad()
        if not disp:
            libro.cambiarDisponibilidad()
            libro.setFechaPestramo(None)
            libro.setFechaDevolucion(None)
            libro.setUsuario(None)
            print("Se ha devuelto el libro exitosamente.\n")
        else:
            raise Exception(f"El libro {self.titulo} NO esta en prestamo.\n")
        

    def revisarDisponibilidad(self):
        try:
            codigo = self.biblioteca.buscarCodigo(self.titulo)
            libro = self.biblioteca.buscarLibro(codigo)
            if libro.disponible:
                return libro, True
            else:
                return libro, False
        except Exception as e:
            raise SystemError(f"\n{e}\n")
