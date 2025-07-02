def contar_calificaciones(calificaciones, materia):
    conteo = [0] * 10  # Índice 0 para nota 1, índice 9 para nota 10
    for i in range(30):
        nota = calificaciones[i][materia - 1]
        conteo[nota - 1] = conteo[nota - 1] + 1
    return conteo