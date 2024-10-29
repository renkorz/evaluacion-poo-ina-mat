import autor

# Al importar la clase libro como herencia, podemos ingresarles el dato del autor
# que escribio el libro y asi agregarlo al motor de busqueda de un libro por su autor.

class Libro(autor):
    def __init__(self, isbn, titulo, id_autor):
        super().__init__(id_autor)
        self.isbn = isbn
        self.titulo = titulo
        
    def validar_isbn(self):
        if(10 <= len(self.isbn) <= 13 and self.isbn.isdigit()):
            return True
        else:
            return False