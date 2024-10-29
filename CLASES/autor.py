from datetime import datetime
import paises

# Con herencia de la clase paises, importamos localidad para la clase de autor.

class Autor(paises):
    def __init__(self, id_autor, nombre_autor, seudonimo_autor, codigo_pais, fecha_nacimiento, fecha_defuncion, biografia_autor, foto_autor):
        super().__init__(codigo_pais)
        self.id_autor = id_autor
        self.nombre_autor = nombre_autor
        self.seudonimo_autor = seudonimo_autor
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_defuncion = fecha_defuncion
        self.biografia_autor = biografia_autor
        self.foto_autor = foto_autor
    
    def manejo_fechas(fecha):
        fecha_dt = datetime.strptime(fecha, '%d/%m/%Y')
        fecha_str = fecha_dt.strftime('%Y-%m-%d')
        return fecha_str
        