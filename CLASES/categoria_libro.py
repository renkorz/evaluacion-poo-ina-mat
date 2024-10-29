import tipo_categoria

# Agregamos e importamos la sub herencia de "tipo_categoria", para implementar mas informacion
# a la clase de "Categoria_Libro"

class Categoria_Libro(tipo_categoria):
    def __init__(self, id_categoria_libro, id_tipo_categoria, categoria_libro):
        super().__init__(id_tipo_categoria)
        self.id_categoria_libro = id_categoria_libro
        self.categoria_libro = categoria_libro