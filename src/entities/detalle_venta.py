class DetalleVenta:
    def __init__(self, id_detalle=None, id_venta=None, id_producto=None, cantidad=None, precio=None):
        self.id_detalle = id_detalle
        self.id_venta = id_venta
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.precio = precio