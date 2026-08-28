from src.entities.inventario import Inventario

inventarios = []

def crear_inventario(inventario: Inventario):
    inventarios.append(inventario)

def editar_inventario(id_producto, nuevo_nombre, nuevo_precio, nuevo_cantidad):
    for inventario in inventarios:
        if inventario.id_producto == id_producto:
            inventario.nombre = nuevo_nombre
            inventario.precio = nuevo_precio
            inventario.cantidad = nuevo_cantidad
            return inventario

    return None

def eliminar_inventario(id_producto):
    for inventario in inventarios:
        if inventario.id_producto == id_producto:
            inventarios.remove(inventario)
        
            return inventario

    return None

def get_ID(id_producto):
    for inventario in inventarios:
        if inventario.id_producto == id_producto:
            return inventario

    return None

def get_lista(ids):
    resultado = []

    for inventario in inventarios:
        if inventario.id_producto in ids:
            resultado.append(inventario)

    return resultado

        