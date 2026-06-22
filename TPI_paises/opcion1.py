def agregar_pais(paises):
    while  True:
        nombre_pais = input("Ingrese un país: ").strip().title()

        if not nombre_pais:
            print("ERROR! El campo no puede estar completamente vacío.")
            continue

        elif not nombre_pais.replace(" ", "").isalpha():
            print("ERROR! No se permiten números ni caracteres especiales.")
            continue

        existe = False

        for pais in paises:
            if pais["nombre"].strip().lower() == nombre_pais.strip().lower():
                existe = True
                break

        if existe:
            print("Ese país ya existe.")
            continue
        break

    while True:
        poblacion = input(f"Ingrese la población de {nombre_pais}: ")
        if poblacion.isdigit() and int(poblacion) > 0:
            poblacion = int(poblacion)
            break
        else:
            print("ERROR! Debe ingresar un número entero positivo.")

    while True:
        superficie = input(f"Ingrese la superficie de {nombre_pais}: ")
        if superficie.isdigit() and int(superficie) > 0:
            superficie = int(superficie)
            break
        else:
            print("ERROR! Debe ingresar un número entero positivo.")

    while True:
        continente = input(f"Ingrese el continente de {nombre_pais}: ").strip().title()
        if not continente:
            print("ERROR! El campo no puede estar completamente vacío.")
        elif not continente.replace(" ", "").isalpha():
            print("ERROR! No se permiten números ni caracteres especiales.")
        else:
            break

    nuevo_pais ={
        "nombre": nombre_pais,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)

    print("¡País agregado correctamente!")

    if __name__=="__main__":
        agregar_pais(paises)