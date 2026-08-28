from src.entities.producto import Producto

productos = []


def crear_producto(producto: Producto):
    productos.append(producto)


def editar_producto(id_producto, nuevo_nombre, nuevo_precio):
    for producto in productos:
        if producto.id_producto == id_producto:
            producto.nombre = nuevo_nombre
            producto.precio = nuevo_precio
            return producto
        
    return None


def eliminar_producto(id_producto):
    for producto in productos:
        if producto.id_producto == id_producto:
            productos.remove(producto)
            return producto

    return None

def get_ID(id_producto):
    for producto in productos:
        if producto.id_producto == id_producto:
            return producto
        
    return None

def get_lista(ids):
    resultado = []

    for producto in productos:
        if producto.id_producto in ids:
            resultado.append(producto)

    return resultado
