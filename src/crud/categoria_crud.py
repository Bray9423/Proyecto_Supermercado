from src.entities.categoria import Categoria

categorias = []


# Crear
def crear_categoria(categoria):
    categorias.append(categoria)


# Editar
def editar_categoria(id_categoria, nombre):
    categoria = get_categoria(id_categoria)

    if categoria:
        categoria.nombre = nombre
        return True

    return False


# Eliminar
def eliminar_categoria(id_categoria):
    categoria = get_categoria(id_categoria)

    if categoria:
        categorias.remove(categoria)
        return True

    return False


# Get(Id)
def get_categoria(id_categoria):
    for categoria in categorias:
        if categoria.id_categoria == id_categoria:
            return categoria

    return None


# Get(Lista)
def get_categorias():
    return categorias