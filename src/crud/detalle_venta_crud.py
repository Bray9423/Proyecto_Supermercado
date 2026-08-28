from src.entities.detalle_venta import DetalleVenta

detalles_venta = []


# Crear
def crear_detalle_venta(detalle):
    detalles_venta.append(detalle)


# Editar
def editar_detalle_venta(id_detalle, id_venta, id_producto, cantidad, precio):
    detalle = get_detalle_venta(id_detalle)

    if detalle:
        detalle.id_venta = id_venta
        detalle.id_producto = id_producto
        detalle.cantidad = cantidad
        detalle.precio = precio
        return True

    return False


# Eliminar
def eliminar_detalle_venta(id_detalle):
    detalle = get_detalle_venta(id_detalle)

    if detalle:
        detalles_venta.remove(detalle)
        return True

    return False


# Get(Id)
def get_detalle_venta(id_detalle):
    for detalle in detalles_venta:
        if detalle.id_detalle == id_detalle:
            return detalle

    return None


# Get(Lista)
def get_detalles_venta():
    return detalles_venta