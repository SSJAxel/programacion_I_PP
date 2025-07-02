from constantes import CANTIDAD_ESTUDIANTES

def contar_calificaciones(calificaciones, materia):
    conteo = [0] * 10  # 0 para nota 1, 9 para nota 10
    for i in range(CANTIDAD_ESTUDIANTES):
        nota = calificaciones[i][materia - 1]
        conteo[nota - 1] = conteo[nota - 1] + 1
    return conteo