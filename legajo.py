from constantes import CANTIDAD_MATERIAS

def buscar_por_legajo(nombres, generos, legajos, calificaciones, promedios):
    legajo_buscar = int(input("Ingrese el legajo a buscar: "))
    encontrado = False
    for i in range(len(legajos)):
        if legajos[i] == legajo_buscar:
            print("Estudiante encontrado:")
            print("Nombre:", nombres[i])
            print("Género:", generos[i])
            print("Legajo:", legajos[i])
            print("Calificaciones:", end=" ")
            for j in range(CANTIDAD_MATERIAS):
                print(calificaciones[i][j], end=" ")
            print()
            if len(promedios) > i:
                print("Promedio:", promedios[i])
            encontrado = True
    if not encontrado:
        print("No se encontró un estudiante con ese legajo.")