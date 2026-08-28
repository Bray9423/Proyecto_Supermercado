from src.entities.venta import Venta

ventas = []


def crear_venta(venta: Venta):
    ventas.append(venta)


def editar_venta(id_venta, nueva_fecha, nuevo_total, nuevo_usuario_id, nueva_sucursal_id):
    for venta in ventas:
        if venta.id == id_venta:
            venta.fecha = nueva_fecha
            venta.total = nuevo_total
            venta.usuario_id = nuevo_usuario_id
            venta.sucursal_id = nueva_sucursal_id
            return venta

    return None


def eliminar_venta(id_venta):
    for venta in ventas:
        if venta.id == id_venta:
            ventas.remove(venta)
            return venta

    return None


def get_ID(id_venta):
    for venta in ventas:
        if venta.id == id_venta:
            return venta

    return None


def get_lista(ids):
    resultado = []

    for venta in ventas:
        if venta.id in ids:
            resultado.append(venta)

    return resultado