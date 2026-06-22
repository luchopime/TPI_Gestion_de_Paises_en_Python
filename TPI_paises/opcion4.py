def filtrar_pais(paises):
    
    print('''
    ---FILTRAR CONTINENTES---
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
        for pais in paises:
            if pais["continente"].lower() == continente.lower():
                print(pais)
                encontrado = True

        if not encontrado:
            print("No se encontraron países de ese continente.")

    elif opcion == "2":

        while True:
            minimo = input("Ingrese la población mínima: ")

            if minimo.isdigit() and int(minimo) >= 0:
                minimo = int(minimo)
                break
            else:
                print("ERROR! Ingrese un número válido.")

        while True:
            maximo = input("Ingrese la población máxima: ")

            if maximo.isdigit() and int(maximo) >= 0:
                maximo = int(maximo)
                break
            else:
                print("ERROR! Ingrese un número válido.")

        if minimo > maximo:
            print("ERROR! La población mínima no puede ser mayor que la máxima.")

        else:
            encontrado = False

            for pais in paises:
                if minimo <= pais["poblacion"] <= maximo:
                    print(pais)
                    encontrado = True

            if not encontrado:
                print("No se encontraron países en ese rango.")

    elif opcion == "3":

        while True:
            minimo = input("Ingrese la superficie mínima: ")

            if minimo.isdigit() and int(minimo) >= 0:
                minimo = int(minimo)
                break
            else:
                print("ERROR! Ingrese un número válido.")

        while True:
            maximo = input("Ingrese la superficie máxima: ")

            if maximo.isdigit() and int(maximo) >= 0:
                maximo = int(maximo)
                break
            else:
                print("ERROR! Ingrese un número válido.")

        if minimo > maximo:
            print("ERROR! La superficie mínima no puede ser mayor que la máxima.")

        else:
            encontrado = False

            for pais in paises:
                if minimo <= pais["superficie"] <= maximo:
                    print(pais)
                    encontrado = True

            if not encontrado:
                print("No se encontraron países en ese rango.")

    else:
        print("Opción inválida.")

        
    if __name__=="__main__":
        filtrar_pais(paises)