
"""
l1 = Libro(url="https://www.gutenberg.org/cache/epub/11/pg11.txt")
#l2 = Libro(url="https://docs.python.org/es/3/library/re.html") # ERROR: Url no valida
l3 = Libro(path="Libros/Frankenstein;_or,_the_modern_prometheus.txt") # 

bbl = Biblioteca()

bbl.agregarLibro(l1)

bbl.agregarLibro(l1)

bbl.agregarLibro(l3)

bbl.buscarCodigo("Matilda")

bbl.mostrarBiblioteca()

del bbl
"""
"""
l1 = Libro(url="https://www.gutenberg.org/cache/epub/11/pg11.txt")
#l2 = Libro(url="https://docs.python.org/es/3/library/re.html") # ERROR: Url no valida
l3 = Libro(path="Libros/Frankenstein;_or,_the_modern_prometheus.txt")

bbl = Biblioteca()

bbl.agregarLibro(l1)

#bbl.agregarLibro(l1)

bbl.agregarLibro(l3)

#bbl.buscarCodigo("Matilda")

bbl.mostrarBiblioteca()

usr1= Usuario("Julian","julian@gmail.com",3058128646)
p1 = Prestamo(bbl,l1.getTitulo(),usr1)
p1.prestarLibro()
#p1.prestarLibro()
p1.devolverLibro()
#p1.devolverLibro()
"""