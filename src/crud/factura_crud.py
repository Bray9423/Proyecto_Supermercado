from src.entities.factura import Factura

facturas = []


# Crear
def crear_factura(factura):
    facturas.append(factura)


# Editar
def editar_factura(id_factura, id_venta, numero, fecha, total):
    factura = get_factura(id_factura)

    if factura:
        factura.id_venta = id_venta
        factura.numero = numero
        factura.fecha = fecha
        factura.total = total
        return True

    return False


# Eliminar
def eliminar_factura(id_factura):
    factura = get_factura(id_factura)

    if factura:
        facturas.remove(factura)
        return True

    return False


# Get(Id)
def get_factura(id_factura):
    for factura in facturas:
        if factura.id_factura == id_factura:
            return factura

    return None


# Get(Lista)
def get_facturas():
    return facturas