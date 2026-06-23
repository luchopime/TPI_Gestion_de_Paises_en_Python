import csv
print("CSV cargado correctamente")  

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

#Opcion 3
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

# Opcion 5
def ordenar_paises(lista):

    if len(lista) == 0:
        print("No hay paises cargados.")
        return

    print("\n1. Ordenar por nombre")
    print("2. Ordenar por poblacion")
    print("3. Ordenar por superficie")

    opcion = input("Seleccione una opcion: ")

    print("\n1. Ascendente")
    print("2. Descendente")

    orden = input("Seleccione el tipo de orden: ")

    reverse = False

    if orden == "2":
        reverse = True

    if opcion == "1":

        ordenados = sorted(
            lista,
            key=lambda pais: pais["nombre"],
            reverse=reverse
        )

    elif opcion == "2":

        ordenados = sorted(
            lista,
            key=lambda pais: pais["poblacion"],
            reverse=reverse
        )

    elif opcion == "3":

        ordenados = sorted(
            lista,
            key=lambda pais: pais["superficie"],
            reverse=reverse
        )

    else:
        print("Opcion invalida")
        return

    print("\n===== PAISES ORDENADOS =====")

    for pais in ordenados:
        print(
            f"{pais['nombre']} - "
            f"Poblacion: {pais['poblacion']} - "
            f"Superficie: {pais['superficie']} km² - "
            f"Continente: {pais['continente']}"
        )      

# Opcion 6
def estadisticas(lista):

    if len(lista) == 0:
        print("No hay paises cargados.")
        return

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
        f"Pais con mayor poblacion: {mayor['nombre']} "
        f"({mayor['poblacion']:,})"
    )

    print(
        f"Pais con menor poblacion: {menor['nombre']} "
        f"({menor['poblacion']:,})"
    )

    print(
        f"Promedio de poblacion: {promedio_poblacion:,.2f}"
    )

    print(
        f"Promedio de superficie: {promedio_superficie:,.2f} km²"
    )

    print("\nCantidad de paises por continente:")

    for continente, cantidad in continentes.items():
        print(f"- {continente}: {cantidad}")

#Opcion 7 
def mostrar_todos(lista):

    for pais in lista:
        print(
            f"{pais['nombre']} - "
            f"Poblacion: {pais['poblacion']} - "
            f"Superficie: {pais['superficie']} km² - "
            f"Continente: {pais['continente']}"
        )