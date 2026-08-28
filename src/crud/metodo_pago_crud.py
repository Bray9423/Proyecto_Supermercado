from src.entities.metodo_pago import MetodoPago

metodos_pago = []

def crear_metodopago(metodo_pago: MetodoPago):
    metodos_pago.append(metodo_pago)

def editar_metodopago(id_metodo_pago, nuevo_nombre, nuevo_tipo):
    for metodo_pago in metodos_pago:
        if metodo_pago.id_metodo_pago == id_metodo_pago:
            metodo_pago.nombre_metodo_pago = nuevo_nombre
            metodo_pago.tipo_metodo_pago = nuevo_tipo
            return metodo_pago

    return None

def eliminar_metodopago(id_metodo_pago):
    for metodo_pago in metodos_pago:
        if metodo_pago.id_metodo_pago == id_metodo_pago:
            metodos_pago.remove(metodo_pago)
            return metodo_pago

    return None

def get_ID(id_metodo_pago):
    for metodo_pago in metodos_pago:
        if metodo_pago.id_metodo_pago == id_metodo_pago:
            return metodo_pago
        
    return None

def get_lista(ids):
    resultado = []

    for metodo_pago in metodos_pago:
        if metodo_pago.id_metodo_pago in ids:
            resultado.append(metodo_pago)

    return resultado