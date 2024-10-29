# La clase "Paises" es la base para agregarlo como una clase hija a otras clases y asi ingresarle
# mas datos descriptivos a otro.

class Paises():
    def __init__(self, codigo_pais, codigo_iso3_pais, nombre_pais, gentilicio_pais):
        self.codigo_pais = codigo_pais
        self.codigo_iso3_pais = codigo_iso3_pais
        self.nombre_pais = nombre_pais
        self.gentilicio_pais = gentilicio_pais