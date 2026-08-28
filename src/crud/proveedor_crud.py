from src.entities.proveedor import Proveedor

proveedores = []


def crear_proveedor(proveedor: Proveedor):
    proveedores.append(proveedor)


def editar_proveedor(id_proveedor, nuevo_nombre, nuevo_telefono, nuevo_correo):
    for proveedor in proveedores:
        if proveedor.id_proveedor == id_proveedor:
            proveedor.nombre = nuevo_nombre
            proveedor.telefono = nuevo_telefono
            proveedor.correo = nuevo_correo
            return proveedor

    return None


def eliminar_proveedor(id_proveedor, nombre_proveedor):
    for proveedor in proveedores:
        if proveedor.id_proveedor == id_proveedor or proveedor.nombre == nombre_proveedor:
            proveedores.remove(proveedor)
            return proveedor

    return None


def get_ID(id_proveedor):
    for proveedor in proveedores:
        if proveedor.id_proveedor == id_proveedor:
            return proveedor

    return None


def get_lista(ids):
    resultado = []

    for proveedor in proveedores:
        if proveedor.id_proveedor in ids:
            resultado.append(proveedor)

    return resultado