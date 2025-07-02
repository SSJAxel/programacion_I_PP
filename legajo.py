def buscar_por_legajo(nombres, generos, legajos, calificaciones, promedios):
    legajo_buscar = int(input("Ingrese el legajo a buscar: "))
    encontrado = False
    for i in range(30):
        if legajos[i] == legajo_buscar:
            print("Estudiante encontrado:")
            print("Nombre:", nombres[i])
            print("Género:", generos[i])
            print("Legajo:", legajos[i])
            print("Calificaciones:", calificaciones[i][0], calificaciones[i][1], calificaciones[i][2], calificaciones[i][3], calificaciones[i][4])
            if len(promedios) == 30:
                print("Promedio:", promedios[i])
            encontrado = True
    if not encontrado:
        print("No se encontró un estudiante con ese legajo.")