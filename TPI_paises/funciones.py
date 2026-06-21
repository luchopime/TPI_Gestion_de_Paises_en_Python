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

import csv

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

def buscar_pais(lista):
    nombre_buscado = input("Ingrese el nombre del pais: ").lower()

    encontrados = []

    for pais in lista:
        if nombre_buscado in pais["nombre"].lower():
            encontrados.append(pais)

    if len(encontrados) == 0:
        print("No se encontraron paises.")
    else:
        print("\nPaises encontrados:")
        for pais in encontrados:
            print(pais)
            
#op 4


def ordenar_paises(lista):

    print("\n1. Ordenar por nombre")
    print("2. Ordenar por poblacion")
    print("3. Ordenar por superficie")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":

        ordenados = sorted(lista, key=lambda pais: pais["nombre"])

    elif opcion == "2":

        ordenados = sorted(lista, key=lambda pais: pais["poblacion"])

    elif opcion == "3":

        ordenados = sorted(lista, key=lambda pais: pais["superficie"])

    else:
        print("Opcion invalida")
        return

    for pais in ordenados:
        print(pais)      

def estadisticas(lista):

    mayor = max(lista, key=lambda pais: pais["poblacion"])
    menor = min(lista, key=lambda pais: pais["poblacion"])

    promedio_poblacion = sum(
        pais["poblacion"] for pais in lista
    ) / len(lista)

    promedio_superficie = sum(
        pais["superficie"] for pais in lista
    ) / len(lista)

    continentes = {}

    for pais in lista:

        continente = pais["continente"]

        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    print("\n===== ESTADISTICAS =====")

    print(
        f"Mayor poblacion: {mayor['nombre']} ({mayor['poblacion']})"
    )

    print(
        f"Menor poblacion: {menor['nombre']} ({menor['poblacion']})"
    )

    print(
        f"Promedio poblacion: {promedio_poblacion:.2f}"
    )

    print(
        f"Promedio superficie: {promedio_superficie:.2f}"
    )

    print("\nCantidad de paises por continente:")

    for continente, cantidad in continentes.items():
        print(f"{continente}: {cantidad}")      

def mostrar_todos(lista):

    for pais in lista:
        print(
            f"{pais['nombre']} - "
            f"Poblacion: {pais['poblacion']} - "
            f"Superficie: {pais['superficie']} km² - "
            f"Continente: {pais['continente']}"
        )