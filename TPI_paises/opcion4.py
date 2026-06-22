def filtrar_pais(paises):

    print('''
    ---FILTRAR PAISES---
    1. Continente
    2. Población
    3. Superficie
    ''')

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        while True:
            continente = input("Ingrese un continente: ").strip().title()

            if not continente:
                print("ERROR! El campo no puede estar completamente vacío.")

            elif not continente.replace(" ", "").isalpha():
                print("ERROR! No se permiten números ni caracteres especiales.")

            else:
                break

        encontrado = False

        for pais in paises:

            if pais["continente"].lower() == continente.lower():

                print(
                    f"{pais['nombre']} - "
                    f"Poblacion: {pais['poblacion']} - "
                    f"Superficie: {pais['superficie']} km² - "
                    f"Continente: {pais['continente']}"
                )

                encontrado = True

        if not encontrado:
            print("No se encontraron países para ese continente.")


    elif opcion == "2":

        while True:
            minimo = input("Ingrese población mínima: ")
            if minimo.isdigit():
                minimo = int(minimo)
                break
            print("ERROR! Debe ser un número válido.")

        while True:
            maximo = input("Ingrese población máxima: ")
            if maximo.isdigit():
                maximo = int(maximo)
                break
            print("ERROR! Debe ser un número válido.")

        if minimo > maximo:
            print("ERROR! El mínimo no puede ser mayor que el máximo.")
            return

        encontrado = False

        for pais in paises:
            if minimo <= pais["poblacion"] <= maximo:
                print(
                    f"{pais['nombre']} - "
                    f"Poblacion: {pais['poblacion']} - "
                    f"Superficie: {pais['superficie']} km² - "
                    f"Continente: {pais['continente']}"
                )
                encontrado = True

        if not encontrado:
            print("No se encontraron países en ese rango.")


    elif opcion == "3":

        while True:
            minimo = input("Ingrese superficie mínima: ")
            if minimo.isdigit() and int(minimo) >= 0:
                minimo = int(minimo)
                break
            print("ERROR! Debe ser un número válido.")

        while True:
            maximo = input("Ingrese superficie máxima: ")
            if maximo.isdigit():
                maximo = int(maximo)
                break
            print("ERROR! Debe ser un número válido.")

        if minimo > maximo:
            print("ERROR! El mínimo no puede ser mayor que el máximo.")
            return    

        encontrado = False

        for pais in paises:
            if minimo <= pais["superficie"] <= maximo:

                print(
                    f"{pais['nombre']} - "
                    f"Poblacion: {pais['poblacion']} - "
                    f"Superficie: {pais['superficie']} km² - "
                    f"Continente: {pais['continente']}"
                )

                encontrado = True

        if not encontrado:
            print("No se encontraron países en ese rango.")

    else:
        print("Opción inválida.")