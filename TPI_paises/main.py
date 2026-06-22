from funciones import *

paises = cargar_csv("TPI_paises/paises.csv")

while True:
    menu()

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        print("Agregar pais")

    elif opcion == "2":
        print("Actualizar pais")

    elif opcion == "3":
        buscar_pais(paises)

    elif opcion == "5":
        ordenar_paises(paises)

    elif opcion == "6":
        estadisticas(paises)

    elif opcion == "7":
        mostrar_todos(paises)

    elif opcion == "0":
        print("Fin del programa")
        break    