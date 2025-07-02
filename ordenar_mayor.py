from constantes import CANTIDAD_ESTUDIANTES, CANTIDAD_MATERIAS

def materia_mayor_promedio(calificaciones):
    promedios_materias = [0] * CANTIDAD_MATERIAS  

    for j in range(CANTIDAD_MATERIAS):  
        suma = 0
        for i in range(CANTIDAD_ESTUDIANTES):  
            suma = suma + calificaciones[i][j]
        promedio = suma / CANTIDAD_ESTUDIANTES
        promedios_materias[j] = promedio  

    max_prom = promedios_materias[0]
    for k in range(1, CANTIDAD_MATERIAS):
        if promedios_materias[k] > max_prom:
            max_prom = promedios_materias[k]

    for l in range(CANTIDAD_MATERIAS):
        if promedios_materias[l] == max_prom:
            print(f"Materia_N{l+1} tiene el mayor promedio: {promedios_materias[l]}")
