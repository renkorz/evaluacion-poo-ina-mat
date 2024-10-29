# "Tipo_usuario" al igual que tipo de categoria, es una sub clase para la base de datos,
# para que de esta forma podamos identificar de manera clara al usuario.
class Tipo_Usuario():
    def __init__(self, id_tipo_usuario, tipo_usuario, descripcion_tipo_usuario):
        self.id_tipo_usuario = id_tipo_usuario
        self.tipo_usuario = tipo_usuario
        self.descripcion_tipo_usuario = descripcion_tipo_usuario
        