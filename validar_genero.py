def validar_genero():
    while True:
        genero = input("Ingrese el género del estudiante [F/M/X]: ")
        if genero == "f":
            genero = "F"
        elif genero == "m":
            genero = "M"
        elif genero == "x":
            genero = "X"
        else:
            print("Género inválido. Debe ser 'F', 'M' o 'X'.")
            continue
        return genero