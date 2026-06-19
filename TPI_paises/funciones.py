import csv

pais = {
    "nombre": "Argentina",
    "poblacion": 45376763,
    "superficie": 2780400,
    "continente": "America"
}

lista_paises = []

def menu():
    print("\n===== GESTION DE PAISES =====")
    print("1. Agregar pais")
    print("2. Actualizar pais")
    print("3. Buscar pais")
    print("4. Filtrar paises")
    print("5. Ordenar paises")
    print("6. Estadisticas")
    print("7. Mostrar todos")
    print("0. Salir")


def cargar_csv(nombre_archivo):
    paises = []

    try:
        with open(nombre_archivo, encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                pais = {
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                }

                paises.append(pais)

    except Exception as error:
        print("Error al leer CSV:", error)

    return paises

