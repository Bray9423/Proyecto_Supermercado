
# ============================================================
# IMPORTAR ENTIDADES
# ============================================================

from src.entities.categoria import Categoria
from src.entities.detalle_venta import DetalleVenta
from src.entities.factura import Factura
from src.entities.inventario import Inventario
from src.entities.metodo_pago import MetodoPago
from src.entities.producto import Producto
from src.entities.proveedor import Proveedor
from src.entities.sucursal import Sucursal
from src.entities.usuario import Usuario
from src.entities.venta import Venta

# ============================================================
# IMPORTAR CRUD
# ============================================================

from src.crud.categoria_crud import (
    crear_categoria,
    editar_categoria,
    eliminar_categoria,
    get_categoria,
    get_categorias,
    categorias
)

from src.crud.detalle_venta_crud import (
    crear_detalle_venta,
    editar_detalle_venta,
    eliminar_detalle_venta,
    get_detalle_venta,
    get_detalles_venta,
    detalles_venta
)

from src.crud.factura_crud import (
    crear_factura,
    editar_factura,
    eliminar_factura,
    get_factura,
    get_facturas,
    facturas
)

from src.crud.inventario_crud import (
    crear_inventario,
    editar_inventario,
    eliminar_inventario,
    get_ID as get_inventario,
    get_lista as get_inventarios,
    inventarios
)

from src.crud.metodo_pago_crud import (
    crear_metodopago,
    editar_metodopago,
    eliminar_metodopago,
    get_ID as get_metodo_pago,
    get_lista as get_metodos_pago,
    metodos_pago
)

from src.crud.producto_crud import (
    crear_producto,
    editar_producto,
    eliminar_producto,
    get_ID as get_producto,
    get_lista as get_productos,
    productos
)

from src.crud.proveedor_crud import (
    crear_proveedor,
    editar_proveedor,
    eliminar_proveedor,
    get_ID as get_proveedor,
    get_lista as get_proveedores,
    proveedores
)

from src.crud.sucursal_crud import (
    crear_sucursal,
    editar_sucursal,
    eliminar_sucursal,
    get_ID as get_sucursal,
    get_lista as get_sucursales,
    sucursales
)

from src.crud.usuario_crud import (
    crear_usuario,
    editar_usuario,
    eliminar_usuario,
    get_ID as get_usuario,
    get_lista as get_usuarios,
    usuarios
)

from src.crud.venta_crud import (
    crear_venta,
    editar_venta,
    eliminar_venta,
    get_ID as get_venta,
    get_lista as get_ventas,
    ventas
)


# ============================================================
# FUNCIONES AUXILIARES
# ============================================================

def pausa():
    input("\nPresione ENTER para continuar...")


def titulo(texto):
    print("\n" + "=" * 60)
    print(texto)
    print("=" * 60)


def buscar_por_id(lista, atributo, valor):

    for elemento in lista:

        if getattr(elemento, atributo, None) == valor:
            return elemento

    return None


# ============================================================
# CATEGORIA
# ============================================================

def menu_categoria():

    while True:

        titulo("CRUD CATEGORIA")

        print("1. Crear")
        print("2. Editar")
        print("3. Eliminar")
        print("4. Get(Id)")
        print("5. Get(Lista)")
        print("0. Volver")

        opcion = input("\nSeleccione una opcion: ")

        # ----------------------------------------------------
        # CREAR
        # ----------------------------------------------------

        if opcion == "1":

            id_categoria = int(input("ID categoria: "))
            nombre = input("Nombre: ")

            categoria = Categoria(
                id_categoria,
                nombre
            )

            crear_categoria(categoria)

            print("\nCategoria creada correctamente.")

            pausa()

        # ----------------------------------------------------
        # EDITAR
        # ----------------------------------------------------

        elif opcion == "2":

            id_categoria = int(input("ID categoria: "))
            nombre = input("Nuevo nombre: ")

            if editar_categoria(
                id_categoria,
                nombre
            ):
                print("\nCategoria actualizada correctamente.")
            else:
                print("\nCategoria no encontrada.")

            pausa()

        # ----------------------------------------------------
        # ELIMINAR
        # ----------------------------------------------------

        elif opcion == "3":

            id_categoria = int(input("ID categoria: "))

            if eliminar_categoria(id_categoria):
                print("\nCategoria eliminada correctamente.")
            else:
                print("\nCategoria no encontrada.")

            pausa()

        # ----------------------------------------------------
        # GET ID
        # ----------------------------------------------------

        elif opcion == "4":

            id_categoria = int(input("ID categoria: "))

            categoria = get_categoria(id_categoria)

            if categoria:

                print("\nID:", categoria.id_categoria)
                print("Nombre:", categoria.nombre)

            else:

                print("\nCategoria no encontrada.")

            pausa()

        # ----------------------------------------------------
        # GET LISTA
        # ----------------------------------------------------

        elif opcion == "5":

            titulo("LISTA DE CATEGORIAS")

            lista = get_categorias()

            if not lista:

                print("No existen categorias.")

            else:

                for categoria in lista:

                    print(
                        f"ID: {categoria.id_categoria} | "
                        f"Nombre: {categoria.nombre}"
                    )

            pausa()

        elif opcion == "0":

            break

        else:

            print("\nOpcion invalida.")


# ============================================================
# PRODUCTO
# ============================================================

def menu_producto():

    while True:

        titulo("CRUD PRODUCTO")

        print("1. Crear")
        print("2. Editar")
        print("3. Eliminar")
        print("4. Get(Id)")
        print("5. Get(Lista)")
        print("0. Volver")

        opcion = input("\nSeleccione una opcion: ")

        # ----------------------------------------------------
        # CREAR
        # ----------------------------------------------------

        if opcion == "1":

            id_producto = int(input("ID producto: "))
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))

            producto = Producto(
                id_producto,
                nombre,
                precio
            )

            crear_producto(producto)

            print("\nProducto creado correctamente.")

            pausa()

        # ----------------------------------------------------
        # EDITAR
        # ----------------------------------------------------

        elif opcion == "2":

            id_producto = int(input("ID producto: "))
            nombre = input("Nuevo nombre: ")
            precio = float(input("Nuevo precio: "))

            resultado = editar_producto(
                id_producto,
                nombre,
                precio
            )

            if resultado:

                print("\nProducto actualizado correctamente.")

            else:

                print("\nProducto no encontrado.")

            pausa()

        # ----------------------------------------------------
        # ELIMINAR
        # ----------------------------------------------------

        elif opcion == "3":

            id_producto = int(input("ID producto: "))

            # =================================================
            # CAMBIO RELACION:
            # No permitimos eliminar un producto que tenga
            # detalles de venta asociados.
            #
            # Esto evita dejar referencias a un producto
            # inexistente.
            # =================================================

            detalle = buscar_por_id(
                detalles_venta,
                "id_producto",
                id_producto
            )

            if detalle:

                print(
                    "\nNo se puede eliminar el producto."
                )

                print(
                    "El producto tiene detalles de venta asociados."
                )

            else:

                resultado = eliminar_producto(id_producto)

                if resultado:

                    print("\nProducto eliminado correctamente.")

                else:

                    print("\nProducto no encontrado.")

            pausa()

        # ----------------------------------------------------
        # GET ID
        # ----------------------------------------------------

        elif opcion == "4":

            id_producto = int(input("ID producto: "))

            producto = get_producto(id_producto)

            if producto:

                print("\nID:", producto.id_producto)
                print("Nombre:", producto.nombre)
                print("Precio:", producto.precio)

            else:

                print("\nProducto no encontrado.")

            pausa()

        # ----------------------------------------------------
        # GET LISTA
        # ----------------------------------------------------

        elif opcion == "5":

            ids = input(
                "Ingrese los IDs separados por coma: "
            )

            ids = [
                int(id_producto.strip())
                for id_producto in ids.split(",")
            ]

            lista = get_productos(ids)

            titulo("PRODUCTOS ENCONTRADOS")

            if not lista:

                print(
                    "No existe el producto o no hay productos "
                    "que coincidan con los IDs."
                )

            else:

                for producto in lista:

                    print(
                        f"ID: {producto.id_producto} | "
                        f"Nombre: {producto.nombre} | "
                        f"Precio: {producto.precio}"
                    )

            pausa()

        elif opcion == "0":

            break

        else:

            print("\nOpcion invalida.")


# ============================================================
# USUARIO
# ============================================================

def menu_usuario():

    while True:

        titulo("CRUD USUARIO")

        print("1. Crear")
        print("2. Editar")
        print("3. Eliminar")
        print("4. Get(Id)")
        print("5. Get(Lista)")
        print("0. Volver")

        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":

            id_usuario = int(input("ID usuario: "))
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            documento = input("Documento: ")
            telefono = input("Telefono: ")
            correo = input("Correo: ")

            usuario = Usuario(
                id_usuario,
                nombre,
                apellido,
                documento,
                telefono,
                correo
            )

            crear_usuario(usuario)

            print("\nUsuario creado correctamente.")

            pausa()

        elif opcion == "2":

            id_usuario = int(input("ID usuario: "))
            nombre = input("Nuevo nombre: ")
            apellido = input("Nuevo apellido: ")
            documento = input("Nuevo documento: ")
            telefono = input("Nuevo telefono: ")
            correo = input("Nuevo correo: ")

            resultado = editar_usuario(
                id_usuario,
                nombre,
                apellido,
                documento,
                telefono,
                correo
            )

            if resultado:

                print("\nUsuario actualizado correctamente.")

            else:

                print("\nUsuario no encontrado.")

            pausa()

        elif opcion == "3":

            id_usuario = int(input("ID usuario: "))

            # =================================================
            # CAMBIO RELACION:
            # Un usuario que tenga ventas asociadas no debe
            # eliminarse porque Venta mantiene usuario_id.
            # =================================================

            venta = buscar_por_id(
                ventas,
                "usuario_id",
                id_usuario
            )

            if venta:

                print(
                    "\nNo se puede eliminar el usuario."
                )

                print(
                    "El usuario tiene ventas asociadas."
                )

            else:

                resultado = eliminar_usuario(id_usuario)

                if resultado:

                    print("\nUsuario eliminado correctamente.")

                else:

                    print("\nUsuario no encontrado.")

            pausa()

        elif opcion == "4":

            id_usuario = int(input("ID usuario: "))

            usuario = get_usuario(id_usuario)

            if usuario:

                print("\nID:", usuario.id)
                print("Nombre:", usuario.nombre)
                print("Apellido:", usuario.apellido)
                print("Documento:", usuario.documento)
                print("Telefono:", usuario.telefono)
                print("Correo:", usuario.correo)

            else:

                print("\nUsuario no encontrado.")

            pausa()

        elif opcion == "5":

            ids = input(
                "Ingrese los IDs separados por coma: "
            )

            ids = [
                int(id_usuario.strip())
                for id_usuario in ids.split(",")
            ]

            lista = get_usuarios(ids)

            titulo("USUARIOS ENCONTRADOS")

            if not lista:

                print("No se encontraron usuarios.")

            else:

                for usuario in lista:

                    print(
                        f"ID: {usuario.id} | "
                        f"Nombre: {usuario.nombre} | "
                        f"Apellido: {usuario.apellido}"
                    )

            pausa()

        elif opcion == "0":

            break

        else:

            print("\nOpcion invalida.")


# ============================================================
# SUCURSAL
# ============================================================

def menu_sucursal():

    while True:

        titulo("CRUD SUCURSAL")

        print("1. Crear")
        print("2. Editar")
        print("3. Eliminar")
        print("4. Get(Id)")
        print("5. Get(Lista)")
        print("0. Volver")

        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":

            id_sucursal = int(input("ID sucursal: "))
            nombre = input("Nombre: ")
            direccion = input("Direccion: ")
            telefono = input("Telefono: ")

            sucursal = Sucursal(
                id_sucursal,
                nombre,
                direccion,
                telefono
            )

            crear_sucursal(sucursal)

            print("\nSucursal creada correctamente.")

            pausa()

        elif opcion == "2":

            id_sucursal = int(input("ID sucursal: "))
            nombre = input("Nuevo nombre: ")
            direccion = input("Nueva direccion: ")
            telefono = input("Nuevo telefono: ")

            resultado = editar_sucursal(
                id_sucursal,
                nombre,
                direccion,
                telefono
            )

            if resultado:

                print("\nSucursal actualizada correctamente.")

            else:

                print("\nSucursal no encontrada.")

            pausa()

        elif opcion == "3":

            id_sucursal = int(input("ID sucursal: "))

            # =================================================
            # CAMBIO RELACION:
            # Una sucursal que tenga ventas asociadas no debe
            # eliminarse porque Venta mantiene sucursal_id.
            # =================================================

            venta = buscar_por_id(
                ventas,
                "sucursal_id",
                id_sucursal
            )

            if venta:

                print(
                    "\nNo se puede eliminar la sucursal."
                )

                print(
                    "La sucursal tiene ventas asociadas."
                )

            else:

                resultado = eliminar_sucursal(id_sucursal)

                if resultado:

                    print("\nSucursal eliminada correctamente.")

                else:

                    print("\nSucursal no encontrada.")

            pausa()

        elif opcion == "4":

            id_sucursal = int(input("ID sucursal: "))

            sucursal = get_sucursal(id_sucursal)

            if sucursal:

                print("\nID:", sucursal.id_sucursal)
                print("Nombre:", sucursal.nombre)
                print("Direccion:", sucursal.direccion)
                print("Telefono:", sucursal.telefono)

            else:

                print("\nSucursal no encontrada.")

            pausa()

        elif opcion == "5":

            ids = input(
                "Ingrese los IDs separados por coma: "
            )

            ids = [
                int(id_sucursal.strip())
                for id_sucursal in ids.split(",")
            ]

            lista = get_sucursales(ids)

            titulo("SUCURSALES ENCONTRADAS")

            if not lista:

                print("No se encontraron sucursales.")

            else:

                for sucursal in lista:

                    print(
                        f"ID: {sucursal.id_sucursal} | "
                        f"Nombre: {sucursal.nombre} | "
                        f"Direccion: {sucursal.direccion}"
                    )

            pausa()

        elif opcion == "0":

            break

        else:

            print("\nOpcion invalida.")


# ============================================================
# PROVEEDOR
# ============================================================

def menu_proveedor():

    while True:

        titulo("CRUD PROVEEDOR")

        print("1. Crear")
        print("2. Editar")
        print("3. Eliminar")
        print("4. Get(Id)")
        print("5. Get(Lista)")
        print("0. Volver")

        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":

            id_proveedor = int(input("ID proveedor: "))
            nombre = input("Nombre: ")
            telefono = input("Telefono: ")
            correo = input("Correo: ")

            proveedor = Proveedor(
                id_proveedor,
                nombre,
                telefono,
                correo
            )

            crear_proveedor(proveedor)

            print("\nProveedor creado correctamente.")

            pausa()

        elif opcion == "2":

            id_proveedor = int(input("ID proveedor: "))
            nombre = input("Nuevo nombre: ")
            telefono = input("Nuevo telefono: ")
            correo = input("Nuevo correo: ")

            resultado = editar_proveedor(
                id_proveedor,
                nombre,
                telefono,
                correo
            )

            if resultado:

                print("\nProveedor actualizado correctamente.")

            else:

                print("\nProveedor no encontrado.")

            pausa()

        elif opcion == "3":

            id_proveedor = int(input("ID proveedor: "))

            resultado = eliminar_proveedor(id_proveedor)

            if resultado:

                print("\nProveedor eliminado correctamente.")

            else:

                print("\nProveedor no encontrado.")

            pausa()

        elif opcion == "4":

            id_proveedor = int(input("ID proveedor: "))

            proveedor = get_proveedor(id_proveedor)

            if proveedor:

                print("\nID:", proveedor.id_proveedor)
                print("Nombre:", proveedor.nombre)
                print("Telefono:", proveedor.telefono)
                print("Correo:", proveedor.correo)

            else:

                print("\nProveedor no encontrado.")

            pausa()

        elif opcion == "5":

            ids = input(
                "Ingrese los IDs separados por coma: "
            )

            ids = [
                int(id_proveedor.strip())
                for id_proveedor in ids.split(",")
            ]

            lista = get_proveedores(ids)

            titulo("PROVEEDORES ENCONTRADOS")

            if not lista:

                print("No se encontraron proveedores.")

            else:

                for proveedor in lista:

                    print(
                        f"ID: {proveedor.id_proveedor} | "
                        f"Nombre: {proveedor.nombre} | "
                        f"Telefono: {proveedor.telefono}"
                    )

            pausa()

        elif opcion == "0":

            break

        else:

            print("\nOpcion invalida.")


# ============================================================
# METODO DE PAGO
# ============================================================

def menu_metodo_pago():

    while True:

        titulo("CRUD METODO DE PAGO")

        print("1. Crear")
        print("2. Editar")
        print("3. Eliminar")
        print("4. Get(Id)")
        print("5. Get(Lista)")
        print("0. Volver")

        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":

            id_metodo_pago = int(
                input("ID metodo de pago: ")
            )

            nombre = input("Nombre: ")
            tipo = input("Tipo: ")

            metodo = MetodoPago(
                id_metodo_pago,
                nombre,
                tipo
            )

            crear_metodopago(metodo)

            print("\nMetodo de pago creado correctamente.")

            pausa()

        elif opcion == "2":

            id_metodo_pago = int(
                input("ID metodo de pago: ")
            )

            nombre = input("Nuevo nombre: ")
            tipo = input("Nuevo tipo: ")

            resultado = editar_metodopago(
                id_metodo_pago,
                nombre,
                tipo
            )

            if resultado:

                print(
                    "\nMetodo de pago actualizado correctamente."
                )

            else:

                print("\nMetodo de pago no encontrado.")

            pausa()

        elif opcion == "3":

            id_metodo_pago = int(
                input("ID metodo de pago: ")
            )

            resultado = eliminar_metodopago(
                id_metodo_pago
            )

            if resultado:

                print(
                    "\nMetodo de pago eliminado correctamente."
                )

            else:

                print("\nMetodo de pago no encontrado.")

            pausa()

        elif opcion == "4":

            id_metodo_pago = int(
                input("ID metodo de pago: ")
            )

            metodo = get_metodo_pago(
                id_metodo_pago
            )

            if metodo:

                print(
                    "\nID:",
                    metodo.id_metodo_pago
                )

                print(
                    "Nombre:",
                    metodo.nombre_metodo_pago
                )

                print(
                    "Tipo:",
                    metodo.tipo_metodo_pago
                )

            else:

                print("\nMetodo de pago no encontrado.")

            pausa()

        elif opcion == "5":

            ids = input(
                "Ingrese los IDs separados por coma: "
            )

            ids = [
                int(id_metodo.strip())
                for id_metodo in ids.split(",")
            ]

            lista = get_metodos_pago(ids)

            titulo("METODOS DE PAGO ENCONTRADOS")

            if not lista:

                print("No se encontraron metodos de pago.")

            else:

                for metodo in lista:

                    print(
                        f"ID: {metodo.id_metodo_pago} | "
                        f"Nombre: {metodo.nombre_metodo_pago} | "
                        f"Tipo: {metodo.tipo_metodo_pago}"
                    )

            pausa()

        elif opcion == "0":

            break

        else:

            print("\nOpcion invalida.")


# ============================================================
# INVENTARIO
# ============================================================

def menu_inventario():

    while True:

        titulo("CRUD INVENTARIO")

        print("1. Crear")
        print("2. Editar")
        print("3. Eliminar")
        print("4. Get(Id)")
        print("5. Get(Lista)")
        print("0. Volver")

        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":

            id_producto = int(input("ID producto: "))

            # =================================================
            # CAMBIO RELACION:
            # El inventario se relaciona con Producto mediante
            # id_producto.
            #
            # Validamos que el producto exista antes de crear
            # su registro de inventario.
            # =================================================

            producto = get_producto(id_producto)

            if not producto:

                print(
                    "\nNo existe el producto."
                )

                pausa()
                continue

            nombre = input("Nombre producto: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))

            inventario = Inventario(
                id_producto,
                nombre,
                precio,
                cantidad
            )

            crear_inventario(inventario)

            print("\nInventario creado correctamente.")

            pausa()

        elif opcion == "2":

            id_producto = int(input("ID producto: "))
            nombre = input("Nuevo nombre: ")
            precio = float(input("Nuevo precio: "))
            cantidad = int(input("Nueva cantidad: "))

            resultado = editar_inventario(
                id_producto,
                nombre,
                precio,
                cantidad
            )

            if resultado:

                print("\nInventario actualizado correctamente.")

            else:

                print("\nInventario no encontrado.")

            pausa()

        elif opcion == "3":

            id_producto = int(input("ID producto: "))

            resultado = eliminar_inventario(
                id_producto
            )

            if resultado:

                print("\nInventario eliminado correctamente.")

            else:

                print("\nInventario no encontrado.")

            pausa()

        elif opcion == "4":

            id_producto = int(input("ID producto: "))

            inventario = get_inventario(
                id_producto
            )

            if inventario:

                print(
                    "\nID producto:",
                    inventario.id_producto
                )

                print(
                    "Nombre:",
                    inventario.nombre
                )

                print(
                    "Precio:",
                    inventario.precio
                )

                print(
                    "Cantidad:",
                    inventario.cantidad
                )

            else:

                print(
                    "\nNo existe el producto o no hay inventario."
                )

            pausa()

        elif opcion == "5":

            ids = input(
                "Ingrese los IDs de producto separados por coma: "
            )

            ids = [
                int(id_producto.strip())
                for id_producto in ids.split(",")
            ]

            lista = get_inventarios(ids)

            titulo("INVENTARIO ENCONTRADO")

            if not lista:

                print(
                    "No existe el producto o no hay inventario."
                )

            else:

                for inventario in lista:

                    print(
                        f"Producto: {inventario.id_producto} | "
                        f"Nombre: {inventario.nombre} | "
                        f"Precio: {inventario.precio} | "
                        f"Cantidad: {inventario.cantidad}"
                    )

            pausa()

        elif opcion == "0":

            break

        else:

            print("\nOpcion invalida.")


# ============================================================
# VENTA
# ============================================================

def menu_venta():

    while True:

        titulo("CRUD VENTA")

        print("1. Crear")
        print("2. Editar")
        print("3. Eliminar")
        print("4. Get(Id)")
        print("5. Get(Lista)")
        print("0. Volver")

        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":

            id_venta = int(input("ID venta: "))
            fecha = input("Fecha: ")
            total = float(input("Total: "))
            usuario_id = int(input("ID usuario: "))
            sucursal_id = int(input("ID sucursal: "))

            # =================================================
            # CAMBIO RELACION:
            # Venta depende de:
            #
            # Usuario
            # Sucursal
            #
            # Validamos ambas relaciones antes de crear la
            # venta.
            # =================================================

            usuario = get_usuario(usuario_id)
            sucursal = get_sucursal(sucursal_id)

            if not usuario:

                print(
                    "\nERROR: El usuario no existe."
                )

                pausa()
                continue

            if not sucursal:

                print(
                    "\nERROR: La sucursal no existe."
                )

                pausa()
                continue

            venta = Venta(
                id_venta,
                fecha,
                total,
                usuario_id,
                sucursal_id
            )

            crear_venta(venta)

            print("\nVenta creada correctamente.")

            pausa()

        elif opcion == "2":

            id_venta = int(input("ID venta: "))
            fecha = input("Nueva fecha: ")
            total = float(input("Nuevo total: "))
            usuario_id = int(input("Nuevo ID usuario: "))
            sucursal_id = int(input("Nuevo ID sucursal: "))

            usuario = get_usuario(usuario_id)
            sucursal = get_sucursal(sucursal_id)

            if not usuario:

                print(
                    "\nERROR: El usuario no existe."
                )

                pausa()
                continue

            if not sucursal:

                print(
                    "\nERROR: La sucursal no existe."
                )

                pausa()
                continue

            resultado = editar_venta(
                id_venta,
                fecha,
                total,
                usuario_id,
                sucursal_id
            )

            if resultado:

                print("\nVenta actualizada correctamente.")

            else:

                print("\nVenta no encontrada.")

            pausa()

        elif opcion == "3":

            id_venta = int(input("ID venta: "))

            # =================================================
            # CAMBIO RELACION:
            # Una Venta no debe eliminarse si tiene:
            #
            # - Detalles de venta
            # - Factura
            #
            # Esto evita dejar registros huérfanos.
            # =================================================

            detalle = buscar_por_id(
                detalles_venta,
                "id_venta",
                id_venta
            )

            factura = buscar_por_id(
                facturas,
                "id_venta",
                id_venta
            )

            if detalle:

                print(
                    "\nNo se puede eliminar la venta."
                )

                print(
                    "La venta tiene detalles asociados."
                )

            elif factura:

                print(
                    "\nNo se puede eliminar la venta."
                )

                print(
                    "La venta tiene una factura asociada."
                )

            else:

                resultado = eliminar_venta(id_venta)

                if resultado:

                    print("\nVenta eliminada correctamente.")

                else:

                    print("\nVenta no encontrada.")

            pausa()

        elif opcion == "4":

            id_venta = int(input("ID venta: "))

            venta = get_venta(id_venta)

            if venta:

                print("\nID:", venta.id)
                print("Fecha:", venta.fecha)
                print("Total:", venta.total)
                print("Usuario:", venta.usuario_id)
                print("Sucursal:", venta.sucursal_id)

            else:

                print("\nVenta no encontrada.")

            pausa()

        elif opcion == "5":

            ids = input(
                "Ingrese los IDs de venta separados por coma: "
            )

            ids = [
                int(id_venta.strip())
                for id_venta in ids.split(",")
            ]

            lista = get_ventas(ids)

            titulo("VENTAS ENCONTRADAS")

            if not lista:

                print("No se encontraron ventas.")

            else:

                for venta in lista:

                    print(
                        f"ID: {venta.id} | "
                        f"Fecha: {venta.fecha} | "
                        f"Total: {venta.total} | "
                        f"Usuario: {venta.usuario_id} | "
                        f"Sucursal: {venta.sucursal_id}"
                    )

            pausa()

        elif opcion == "0":

            break

        else:

            print("\nOpcion invalida.")


# ============================================================
# DETALLE DE VENTA
# ============================================================

def menu_detalle_venta():

    while True:

        titulo("CRUD DETALLE DE VENTA")

        print("1. Crear")
        print("2. Editar")
        print("3. Eliminar")
        print("4. Get(Id)")
        print("5. Get(Lista)")
        print("0. Volver")

        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":

            id_detalle = int(input("ID detalle: "))
            id_venta = int(input("ID venta: "))
            id_producto = int(input("ID producto: "))
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))

            # =================================================
            # CAMBIO RELACION:
            #
            # DetalleVenta depende de:
            #
            # Venta
            # Producto
            #
            # Validamos ambas relaciones antes de crear.
            # =================================================

            venta = get_venta(id_venta)
            producto = get_producto(id_producto)

            if not venta:

                print(
                    "\nERROR: La venta no existe."
                )

                pausa()
                continue

            if not producto:

                print(
                    "\nERROR: El producto no existe."
                )

                pausa()
                continue

            detalle = DetalleVenta(
                id_detalle,
                id_venta,
                id_producto,
                cantidad,
                precio
            )

            crear_detalle_venta(detalle)

            print(
                "\nDetalle de venta creado correctamente."
            )

            pausa()

        elif opcion == "2":

            id_detalle = int(input("ID detalle: "))
            id_venta = int(input("Nuevo ID venta: "))
            id_producto = int(input("Nuevo ID producto: "))
            cantidad = int(input("Nueva cantidad: "))
            precio = float(input("Nuevo precio: "))

            venta = get_venta(id_venta)
            producto = get_producto(id_producto)

            if not venta:

                print(
                    "\nERROR: La venta no existe."
                )

                pausa()
                continue

            if not producto:

                print(
                    "\nERROR: El producto no existe."
                )

                pausa()
                continue

            resultado = editar_detalle_venta(
                id_detalle,
                id_venta,
                id_producto,
                cantidad,
                precio
            )

            if resultado:

                print(
                    "\nDetalle actualizado correctamente."
                )

            else:

                print(
                    "\nDetalle no encontrado."
                )

            pausa()

        elif opcion == "3":

            id_detalle = int(
                input("ID detalle: ")
            )

            resultado = eliminar_detalle_venta(
                id_detalle
            )

            if resultado:

                print(
                    "\nDetalle eliminado correctamente."
                )

            else:

                print(
                    "\nDetalle no encontrado."
                )

            pausa()

        elif opcion == "4":

            id_detalle = int(
                input("ID detalle: ")
            )

            detalle = get_detalle_venta(
                id_detalle
            )

            if detalle:

                print(
                    "\nID:",
                    detalle.id_detalle
                )

                print(
                    "Venta:",
                    detalle.id_venta
                )

                print(
                    "Producto:",
                    detalle.id_producto
                )

                print(
                    "Cantidad:",
                    detalle.cantidad
                )

                print(
                    "Precio:",
                    detalle.precio
                )

            else:

                print(
                    "\nDetalle no encontrado."
                )

            pausa()

        elif opcion == "5":

            lista = get_detalles_venta()

            titulo("DETALLES DE VENTA")

            if not lista:

                print(
                    "No existen detalles de venta."
                )

            else:

                for detalle in lista:

                    print(
                        f"ID: {detalle.id_detalle} | "
                        f"Venta: {detalle.id_venta} | "
                        f"Producto: {detalle.id_producto} | "
                        f"Cantidad: {detalle.cantidad} | "
                        f"Precio: {detalle.precio}"
                    )

            pausa()

        elif opcion == "0":

            break

        else:

            print("\nOpcion invalida.")


# ============================================================
# FACTURA
# ============================================================

def menu_factura():

    while True:

        titulo("CRUD FACTURA")

        print("1. Crear")
        print("2. Editar")
        print("3. Eliminar")
        print("4. Get(Id)")
        print("5. Get(Lista)")
        print("0. Volver")

        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":

            id_factura = int(
                input("ID factura: ")
            )

            id_venta = int(
                input("ID venta: ")
            )

            numero = input(
                "Numero de factura: "
            )

            fecha = input(
                "Fecha: "
            )

            total = float(
                input("Total: ")
            )

            # =================================================
            # CAMBIO RELACION:
            #
            # Factura depende de Venta mediante id_venta.
            #
            # Validamos que la venta exista antes de crear
            # la factura.
            # =================================================

            venta = get_venta(id_venta)

            if not venta:

                print(
                    "\nERROR: La venta no existe."
                )

                pausa()
                continue

            factura = Factura(
                id_factura,
                id_venta,
                numero,
                fecha,
                total
            )

            crear_factura(factura)

            print(
                "\nFactura creada correctamente."
            )

            pausa()

        elif opcion == "2":

            id_factura = int(
                input("ID factura: ")
            )

            id_venta = int(
                input("Nuevo ID venta: ")
            )

            numero = input(
                "Nuevo numero: "
            )

            fecha = input(
                "Nueva fecha: "
            )

            total = float(
                input("Nuevo total: ")
            )

            venta = get_venta(id_venta)

            if not venta:

                print(
                    "\nERROR: La venta no existe."
                )

                pausa()
                continue

            resultado = editar_factura(
                id_factura,
                id_venta,
                numero,
                fecha,
                total
            )

            if resultado:

                print(
                    "\nFactura actualizada correctamente."
                )

            else:

                print(
                    "\nFactura no encontrada."
                )

            pausa()

        elif opcion == "3":

            id_factura = int(
                input("ID factura: ")
            )

            resultado = eliminar_factura(
                id_factura
            )

            if resultado:

                print(
                    "\nFactura eliminada correctamente."
                )

            else:

                print(
                    "\nFactura no encontrada."
                )

            pausa()

        elif opcion == "4":

            id_factura = int(
                input("ID factura: ")
            )

            factura = get_factura(
                id_factura
            )

            if factura:

                print(
                    "\nID:",
                    factura.id_factura
                )

                print(
                    "Venta:",
                    factura.id_venta
                )

                print(
                    "Numero:",
                    factura.numero
                )

                print(
                    "Fecha:",
                    factura.fecha
                )

                print(
                    "Total:",
                    factura.total
                )

            else:

                print(
                    "\nFactura no encontrada."
                )

            pausa()

        elif opcion == "5":

            lista = get_facturas()

            titulo("FACTURAS")

            if not lista:

                print(
                    "No existen facturas."
                )

            else:

                for factura in lista:

                    print(
                        f"ID: {factura.id_factura} | "
                        f"Venta: {factura.id_venta} | "
                        f"Numero: {factura.numero} | "
                        f"Fecha: {factura.fecha} | "
                        f"Total: {factura.total}"
                    )

            pausa()

        elif opcion == "0":

            break

        else:

            print("\nOpcion invalida.")


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def main():

    while True:

        titulo("SISTEMA DE SUPERMERCADO")

        print("1. Categoria")
        print("2. Producto")
        print("3. Usuario")
        print("4. Sucursal")
        print("5. Proveedor")
        print("6. Metodo de Pago")
        print("7. Inventario")
        print("8. Venta")
        print("9. Detalle de Venta")
        print("10. Factura")
        print("0. Salir")

        opcion = input(
            "\nSeleccione una opcion: "
        )

        if opcion == "1":

            menu_categoria()

        elif opcion == "2":

            menu_producto()

        elif opcion == "3":

            menu_usuario()

        elif opcion == "4":

            menu_sucursal()

        elif opcion == "5":

            menu_proveedor()

        elif opcion == "6":

            menu_metodo_pago()

        elif opcion == "7":

            menu_inventario()

        elif opcion == "8":

            menu_venta()

        elif opcion == "9":

            menu_detalle_venta()

        elif opcion == "10":

            menu_factura()

        elif opcion == "0":

            print(
                "\nPrograma finalizado."
            )

            break

        else:

            print(
                "\nOpcion invalida."
            )

# ============================================================
# EJECUCION
# ============================================================

if __name__ == "__main__":

    main()