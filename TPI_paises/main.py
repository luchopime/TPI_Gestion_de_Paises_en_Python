from funciones import *
from opcion1 import *
from opcion2 import *
from opcion4 import *

paises = cargar_csv("TPI_paises/paises.csv")

while True:
    menu()

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        print("Agregar pais")
        agregar_pais(paises)

    elif opcion == "2":
        print("Actualizar pais")
        actualizar_pais(paises)
    
    elif opcion == "3":
        print("Buscar pais")
        buscar_pais(lista)

    elif opcion == "4":
        print("Filtrar paises")
        filtrar_pais(paises)

    elif opcion == "5":
        print("Ordenar paises")
        ordenar_paises(lista)    

    elif opcion == "6":
        print("Estadisticas")
        estadisticas(lista)
    
    elif opcion == "7":
        print("Mostrar todos")
        mostrar_todos(paises)   
        
    elif opcion == "0":
        print("Fin del programa")
        break    