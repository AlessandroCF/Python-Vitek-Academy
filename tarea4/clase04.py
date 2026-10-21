import csv

# Tarifas del Ticket #2
BASE = {"A": 2500, "B": 3500, "C": 5000}
KG_INCLUIDOS = 5
COSTO_KG_EXTRA = 400
PESO_MAXIMO = 50


class Envio:
    def __init__(self, id_envio, cliente, peso_kg, zona):
        self.id = id_envio
        self.cliente = cliente
        self.peso_kg = peso_kg
        self.zona = zona

    def costo(self):
        costo = BASE[self.zona]

        if self.peso_kg > KG_INCLUIDOS:
            costo += (self.peso_kg - KG_INCLUIDOS) * COSTO_KG_EXTRA

        return costo


def cargar_envios(ruta):
    validos = []
    errores = []

    with open(ruta, "r", encoding="utf-8", newline="") as archivo:
        lector = csv.reader(archivo)

        # Saltar encabezado
        next(lector)

        for numero_linea, fila in enumerate(lector, start=2):

            # Validar cantidad de columnas
            if len(fila) != 4:
                errores.append(
                    f"Línea {numero_linea}: faltan columnas"
                )
                continue

            id_envio, cliente, peso_txt, zona = fila

            # Cliente vacío
            if cliente.strip() == "":
                errores.append(
                    f"Línea {numero_linea}: cliente vacío"
                )
                continue

            # Peso numérico
            try:
                peso = int(peso_txt)
            except ValueError:
                errores.append(
                    f"Línea {numero_linea}: peso no numérico"
                )
                continue

            # Peso positivo
            if peso <= 0:
                errores.append(
                    f"Línea {numero_linea}: peso negativo"
                )
                continue

            # Peso máximo
            if peso > PESO_MAXIMO:
                errores.append(
                    f"Línea {numero_linea}: peso excede máximo"
                )
                continue

            # Zona válida
            if zona not in BASE:
                errores.append(
                    f"Línea {numero_linea}: zona inválida"
                )
                continue

            validos.append(
                Envio(
                    id_envio,
                    cliente,
                    peso,
                    zona
                )
            )

    return validos, errores


if __name__ == "__main__":
    validos, errores = cargar_envios("envios.csv")

    print("Envíos válidos:", len(validos))
    print("Total cobrado:", sum(e.costo() for e in validos))

    print("\nErrores:")
    for error in errores:
        print(error)