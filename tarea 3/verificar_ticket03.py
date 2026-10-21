# -*- coding: utf-8 -*-
# Verificador del Ticket #3. Corre desde la carpeta donde está clase03.py:
#     python verificar_ticket03.py
# No te califica: te dice si tus funciones dan lo que el ticket espera, para que corrijas ANTES de entregar.
import contextlib
import importlib
import io
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

sys.path.insert(0, os.getcwd())
if not os.path.exists("clase03.py"):
    sys.exit("No encuentro clase03.py en esta carpeta.")

TOTAL = 0
BIEN = 0


def comprobar(nombre, obtenido, esperado):
    global TOTAL, BIEN
    TOTAL += 1
    ok = obtenido == esperado
    BIEN += ok
    print(("  OK     " if ok else "  FALLA  ") + nombre + " -> " + repr(obtenido) + ("" if ok else "   (esperado: " + repr(esperado) + ")"))


print("Verificador del Ticket #3")
print()
# Importar tu archivo sin que se ejecute su código de prueba ni sus print / input
silencio = io.StringIO()
try:
    with contextlib.redirect_stdout(silencio):
        m = importlib.import_module("clase03")
except Exception as e:  # noqa: BLE001
    sys.exit("No pude importar clase03.py: %s: %s" % (type(e).__name__, e))

nombres = ["agregar_producto", "buscar_producto", "productos_bajo_minimo", "valor_total_inventario", "encontrar_duplicados"]
for n in nombres:
    comprobar("existe la función %s" % n, callable(getattr(m, n, None)), True)
if not all(callable(getattr(m, n, None)) for n in nombres):
    sys.exit("\nFaltan funciones: créalas con esos nombres exactos y vuelve a correr.")

INICIAL = [("P001", "Arroz 1kg", 120, 50, 1150), ("P002", "Frijoles 1kg", 35, 40, 1450), ("P003", "Aceite 1L", 18, 20, 2300),
           ("P004", "Azúcar 2kg", 90, 30, 1900), ("P005", "Jabón de barra", 12, 25, 650)]
inv = {}
salida_funciones = io.StringIO()
with contextlib.redirect_stdout(salida_funciones):
    for cod, nom, stock, minimo, precio in INICIAL:
        m.agregar_producto(inv, cod, nom, stock, minimo, precio)

    r_bajo = sorted(m.productos_bajo_minimo(inv))
    r_total = m.valor_total_inventario(inv)
    r_buscar = m.buscar_producto(inv, "P999")
    r_dup = m.encontrar_duplicados(["P001", "P003", "P001", "P005", "P003", "P001"])
    antes = m.valor_total_inventario(inv)
    m.agregar_producto(inv, "P006", "Sal 1kg", 10, 5, 800)
    despues = m.valor_total_inventario(inv)
    m.agregar_producto(inv, "P001", "Otro arroz", 1, 1, 1)
    tras_duplicado = m.valor_total_inventario(inv)

print("Casos de prueba del ticket")
comprobar("productos_bajo_minimo(inventario)", r_bajo, ["P002", "P003", "P005"])
comprobar("valor_total_inventario(inventario)", r_total, 408950)
comprobar('buscar_producto(inventario, "P999")', r_buscar, None)
comprobar('encontrar_duplicados([...])', r_dup, {"P001": 3, "P003": 2})
comprobar("agregar un producto nuevo sube el valor total en stock x precio", despues - antes, 8000)

print()
print("Requisitos y casos límite")
comprobar("el inventario es un diccionario", isinstance(inv, dict), True)
comprobar("agregar_producto NO pisa un código que ya existe", tras_duplicado, despues)
comprobar("ninguna función imprime ni usa input()", salida_funciones.getvalue(), "")

print()
print("Resultado: %d de %d comprobaciones correctas." % (BIEN, TOTAL))
print("Todo coincide. Pega estos resultados en tu entrega." if BIEN == TOTAL else
      "Revisa las líneas con FALLA, corrige y vuelve a correrlo. Puedes preguntarle al Tutor sin escribir «Entrega Clase 3».")
