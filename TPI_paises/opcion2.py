def actualizar_pais(paises):
    nombre_pais = input("Ingrese un país nuevo: ").strip().title()
    encontrado = False

    for pais in paises:
        if pais["nombre"].lower() == nombre_pais.lower():
            encontrado = True
            while True:
                nueva_poblacion = input(f"Ingrese la nueva población de {nombre_pais}")
                if nueva_poblacion.isdigit() and int(nueva_poblacion) > 0:
                    nueva_poblacion = int(nueva_poblacion)
                    break
                else:
                    print("ERROR! Debe ingresar un número entero positivo.")

            # VALIDAR SUPERFICIE
            while True:
                nueva_superficie = input(
                    f"Ingrese la nueva superficie de {nombre_pais}: "
                )

                if nueva_superficie.isdigit() and int(nueva_superficie) > 0:
                    nueva_superficie = int(nueva_superficie)
                    break
                else:
                    print("ERROR! Debe ingresar un número entero positivo.")

            # ACTUALIZAR EL DICCIONARIO
            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie

            print("¡País actualizado correctamente!")
            break

    if not encontrado:
        print("ERROR! El país ingresado no existe.")

    if __name__=="__main__":
        actualizar_pais(paises)