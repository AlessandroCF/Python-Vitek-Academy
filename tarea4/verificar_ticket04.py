# -*- coding: utf-8 -*-
# Verificador del Ticket #4. Corre desde la carpeta donde está clase04.py:
#     python verificar_ticket04.py
# No te califica: te dice si tu programa da lo que el ticket espera, para que corrijas ANTES de entregar.
import contextlib
import importlib
import io
import os
import re
import sys
import tempfile

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

sys.path.insert(0, os.getcwd())
if not os.path.exists("clase04.py"):
    sys.exit("No encuentro clase04.py en esta carpeta.")

CSV = """id,cliente,peso_kg,zona
E001,Pulpería La Esquina,4,A
E002,Super San Rafael,12,B
E003,Abastecedor Los Ángeles,abc,A
E004,Minisuper El Roble,30,C
E005,Pulpería Doña Mary,-5,B
E006,Super Buenos Aires,8,D
E007,,6,A
E008,Pulpería El Progreso,50,C
E009,Minisuper Central,7,B
E010,Super Las Palmas,9
"""

TOTAL = 0
BIEN = 0


def comprobar(nombre, obtenido, esperado):
    global TOTAL, BIEN
    TOTAL += 1
    ok = obtenido == esperado
    BIEN += ok
    print(("  OK     " if ok else "  FALLA  ") + nombre + " -> " + repr(obtenido) + ("" if ok else "   (esperado: " + repr(esperado) + ")"))


def numero_de_linea(error):
    if isinstance(error, dict):
        for v in error.values():
            if isinstance(v, int):
                return v
        error = " ".join(str(v) for v in error.values())
    if isinstance(error, (tuple, list)):
        for v in error:
            if isinstance(v, int):
                return v
        error = " ".join(str(v) for v in error)
    hallado = re.search(r"\d+", str(error))
    return int(hallado.group()) if hallado else None


print("Verificador del Ticket #4")
print()
try:
    with contextlib.redirect_stdout(io.StringIO()):
        m = importlib.import_module("clase04")
except Exception as e:  # noqa: BLE001
    sys.exit("No pude importar clase04.py: %s: %s" % (type(e).__name__, e))

comprobar("existe la clase Envio", hasattr(m, "Envio"), True)
comprobar("existe la función cargar_envios", callable(getattr(m, "cargar_envios", None)), True)
if not (hasattr(m, "Envio") and callable(getattr(m, "cargar_envios", None))):
    sys.exit("\nFaltan la clase Envio o la función cargar_envios.")

ruta = os.path.join(tempfile.mkdtemp(), "envios.csv")
with open(ruta, "w", encoding="utf-8", newline="") as f:
    f.write(CSV)

with contextlib.redirect_stdout(io.StringIO()):
    resultado = m.cargar_envios(ruta)
try:
    validos, errores = resultado
except Exception:  # noqa: BLE001
    sys.exit("cargar_envios debe devolver DOS cosas: la lista de envíos válidos y la lista de errores.")

print("Resultado esperado del reporte")
comprobar("envíos válidos", len(validos), 5)
comprobar("líneas rechazadas", len(errores), 5)
total = None
try:
    total = sum(e.costo() for e in validos)
except Exception as e:  # noqa: BLE001
    print("  (no pude sumar e.costo(): %s)" % e)
comprobar("total cobrado", total, 51100)
comprobar("líneas rechazadas (número de línea; la 1 es el encabezado)", sorted(numero_de_linea(e) for e in errores), [4, 6, 7, 8, 11])
comprobar("cada error trae un motivo", all(len(str(e)) > 4 for e in errores), True)

print()
print("Requisitos del código")
codigo = open("clase04.py", encoding="utf-8").read()
comprobar("usa try / except", "try:" in codigo and "except" in codigo, True)
comprobar("lee con el módulo csv", "import csv" in codigo or "from csv" in codigo, True)

print()
print("Resultado: %d de %d comprobaciones correctas." % (BIEN, TOTAL))
print("Todo coincide. Pega estos resultados en tu entrega." if BIEN == TOTAL else
      "Revisa las líneas con FALLA, corrige y vuelve a correrlo. Puedes preguntarle al Tutor sin escribir «Entrega Clase 4».")
