from funciones import *
from opcion1 import *

paises = cargar_csv("TPI_paises/paises.csv")

while True:
    menu()

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        print("Agregar pais")
        agregar_pais(paises)

    elif opcion == "2":
        print("Actualizar pais")

    elif opcion == "0":
        print("Fin del programa")
        break

    else:
        print("Opcion invalida")