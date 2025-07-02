from constantes import CANTIDAD_ESTUDIANTES, CANTIDAD_MATERIAS

def calcular_promedios(calificaciones):
    promedios = [0] * CANTIDAD_ESTUDIANTES
    for i in range(CANTIDAD_ESTUDIANTES):
        suma = 0
        for j in range(CANTIDAD_MATERIAS):
            suma = suma + calificaciones[i][j]
        promedios[i] = suma / CANTIDAD_MATERIAS
    return promedios