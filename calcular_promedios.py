def calcular_promedios(calificaciones):
    promedios = [0] * 30
    for i in range(30):
        suma = 0
        for j in range(5):
            suma = suma + calificaciones[i][j]
        promedios[i] = suma / 5
    return promedios