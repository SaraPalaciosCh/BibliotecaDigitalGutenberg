import re
import requests


class Libro():
    def __init__(self, url):
        try:
            if "https://www.gutenberg.org/cache/epub" not in url:
                raise("ERROR: URL invalida :(")
            else:
                r = requests.get(url)
                if r.status_code in range(400,499):
                    raise("ERROR: no se pudo consultar la URL")
                elif r.status_code == 200:
                    text = r.text 
                    self.autor = 
                    self.titulo
                    self.fecha_lanzamiento
                    self.url
                    self.estado
                    self.fecha_prestamo
                    self.fecha_devolucion

    def solicitar_prestamo(self, Usuario):
        # Se registra automaticamente la fecha de prestamo
        self.fecha_prestamo = date.now()

        # Se fina la devolucion a 15 dias
        self.fecha_devolucion = self.fecha_prestamo.day() + 15
        self.estado = "Prestado"

    

class Usuario():
    def __init__(self):
        self.nombre
        self.correo
        self.telefono
        self.es_admin
        self.libros = []

