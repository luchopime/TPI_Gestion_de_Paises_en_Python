def agregar_pais(paises):
    while  True:
        nombre_pais = input("Ingrese un país: ").strip().title()

        if nombre_pais == "":
            print("ERROR! El país no debe estar vacío!")
            continue

        existe = False

        for pais in paises:
            if pais["nombre"].lower() == nombre_pais.lower():
                existe = True
                break

        if existe:
            print("Ese país ya existe.")
        else:
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
        if continente != "":
            break
        else:
            print("ERROR! El continente no puede estar vacío.")

    nuevo_pais ={
        "nombre": nombre_pais,
        "población": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)

    print("¡País agregado correctamente!")