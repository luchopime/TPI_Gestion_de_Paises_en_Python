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
        print("Buscar pais")

    elif opcion == "4":
        print("Filtrar paises")

    elif opcion == "5":
        print("Ordenar paises")    

    elif opcion == "6":
        print("Estadisticas")
    
    elif opcion == "7":
        print("Mostrar todos")

    elif opcion == "0":
        print("Fin del programa")
        break

    else:
        print("Opcion invalida")