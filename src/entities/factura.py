class Factura:
    def __init__(self, id_factura=None, id_venta=None, numero=None, fecha=None, total=None):
        self.id_factura = id_factura
        self.id_venta = id_venta
        self.numero = numero
        self.fecha = fecha
        self.total = total