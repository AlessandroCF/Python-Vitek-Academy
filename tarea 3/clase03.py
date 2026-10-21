# TICKET 3 — Inventario de bodega (DistriPura)

inventario = {}


def agregar_producto(inventario, codigo, nombre, stock, minimo, precio):
    # Si el código ya existe, no lo sobrescribe
    if codigo in inventario:
        return False

    inventario[codigo] = {
        "nombre": nombre,
        "stock": stock,
        "minimo": minimo,
        "precio": precio
    }

    return True


def buscar_producto(inventario, codigo):
    return inventario.get(codigo, None)


def productos_bajo_minimo(inventario):
    resultado = []

    for codigo, producto in inventario.items():
        if producto["stock"] < producto["minimo"]:
            resultado.append(codigo)

    return resultado


def valor_total_inventario(inventario):
    total = 0

    for producto in inventario.values():
        total += producto["stock"] * producto["precio"]

    return total


def encontrar_duplicados(lista_codigos):
    conteo = {}

    for codigo in lista_codigos:
        conteo[codigo] = conteo.get(codigo, 0) + 1

    duplicados = {}

    for codigo, cantidad in conteo.items():
        if cantidad > 1:
            duplicados[codigo] = cantidad

    return duplicados


# Carga inventario inicial

agregar_producto(inventario, "P001", "Arroz 1kg", 120, 50, 1150)
agregar_producto(inventario, "P002", "Frijoles 1kg", 35, 40, 1450)
agregar_producto(inventario, "P003", "Aceite 1L", 18, 20, 2300)
agregar_producto(inventario, "P004", "Azúcar 2kg", 90, 30, 1900)
agregar_producto(inventario, "P005", "Jabón de barra", 12, 25, 650)