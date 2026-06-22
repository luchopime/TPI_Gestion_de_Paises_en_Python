def agregar_pais(paises):

    while True:
        nombre_pais = input("Ingrese un país: ").strip().title()

        if not nombre_pais:
            print("ERROR! El campo no puede estar vacío.")
            continue

        elif not all(part.isalpha() for part in nombre_pais.split()):
            print("ERROR! No se permiten números ni caracteres especiales.")
            continue

        if any(pais["nombre"].lower() == nombre_pais.lower() for pais in paises):
            print("Ese país ya existe.")
            continue

        break

    while True:
        poblacion = input(f"Ingrese la población de {nombre_pais}: ")
        if poblacion.isdigit() and int(poblacion) > 0:
            poblacion = int(poblacion)
            break
        print("ERROR! Debe ingresar un número entero positivo.")

    while True:
        superficie = input(f"Ingrese la superficie de {nombre_pais}: ")
        if superficie.isdigit() and int(superficie) > 0:
            superficie = int(superficie)
            break
        print("ERROR! Debe ingresar un número entero positivo.")

    while True:
        continente = input(f"Ingrese el continente de {nombre_pais}: ").strip().title()
        if not continente:
            print("ERROR! El campo no puede estar vacío.")
        elif not continente.replace(" ", "").isalpha():
            print("ERROR! No se permiten números ni caracteres especiales.")
        else:
            break

    paises.append({
        "nombre": nombre_pais,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    })

    print("¡País agregado correctamente!")