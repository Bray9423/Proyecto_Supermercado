<<<<<<< HEAD
<<<<<<< Updated upstream
=======
=======
>>>>>>> origin/main
from src.entities.sucursal import Sucursal

sucursales = []


def crear_sucursal(sucursal: Sucursal):
    sucursales.append(sucursal)


def editar_sucursal(id_sucursal, nuevo_nombre, nueva_direccion, nuevo_telefono):
    for sucursal in sucursales:
        if sucursal.id_sucursal == id_sucursal:
            sucursal.nombre = nuevo_nombre
            sucursal.direccion = nueva_direccion
            sucursal.telefono = nuevo_telefono
            return sucursal

    return None


<<<<<<< HEAD
def eliminar_sucursal(id_sucursal):
    for sucursal in sucursales:
        if sucursal.id_sucursal == id_sucursal:
=======
def eliminar_sucursal(id_sucursal, nombre_sucursal):
    for sucursal in sucursales:
        if sucursal.id_sucursal == id_sucursal or sucursal.nombre == nombre_sucursal:
>>>>>>> origin/main
            sucursales.remove(sucursal)
            return sucursal

    return None


<<<<<<< HEAD
def get_sucursal(id_sucursal):
=======
def get_ID(id_sucursal):
>>>>>>> origin/main
    for sucursal in sucursales:
        if sucursal.id_sucursal == id_sucursal:
            return sucursal

    return None
<<<<<<< HEAD
>>>>>>> Stashed changes
=======


def get_lista(ids):
    resultado = []

    for sucursal in sucursales:
        if sucursal.id_sucursal in ids:
            resultado.append(sucursal)

    return resultado
>>>>>>> origin/main
