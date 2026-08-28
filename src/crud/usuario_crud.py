from src.entities.usuario import Usuario

usuarios = []


def crear_usuario(usuario: Usuario):
    usuarios.append(usuario)


def editar_usuario(id_usuario, nuevo_nombre, nuevo_apellido, nuevo_documento, nuevo_telefono, nuevo_correo):
    for usuario in usuarios:
        if usuario.id == id_usuario:
            usuario.nombre = nuevo_nombre
            usuario.apellido = nuevo_apellido
            usuario.documento = nuevo_documento
            usuario.telefono = nuevo_telefono
            usuario.correo = nuevo_correo
            return usuario

    return None


def eliminar_usuario(id_usuario):
    for usuario in usuarios:
        if usuario.id == id_usuario:
            usuarios.remove(usuario)
            return usuario

    return None


def get_ID(id_usuario):
    for usuario in usuarios:
        if usuario.id == id_usuario:
            return usuario

    return None


def get_lista(ids):
    resultado = []

    for usuario in usuarios:
        if usuario.id in ids:
            resultado.append(usuario)

    return resultado