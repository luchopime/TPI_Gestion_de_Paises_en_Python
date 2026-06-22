def actualizar_pais(paises):

    nombre_pais = input("Ingrese el país que desea actualizar: ").strip()

    for pais in paises:
        if pais["nombre"].lower() == nombre_pais.lower():

            while True:
                nueva_poblacion = input(f"Ingrese la nueva población de {nombre_pais}: ")
                if nueva_poblacion.isdigit() and int(nueva_poblacion) > 0:
                    nueva_poblacion = int(nueva_poblacion)
                    break
                print("ERROR! Debe ingresar un número entero positivo.")

            while True:
                nueva_superficie = input(f"Ingrese la nueva superficie de {nombre_pais}: ")
                if nueva_superficie.isdigit() and int(nueva_superficie) > 0:
                    nueva_superficie = int(nueva_superficie)
                    break
                print("ERROR! Debe ingresar un número entero positivo.")

            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie

            print("¡País actualizado correctamente!")
            break

    else:
        print("ERROR! El país ingresado no existe.")