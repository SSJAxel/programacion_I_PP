def materia_mayor_promedio(calificaciones):
    promedios_materias = [0] * 5  

    for j in range(5):  # 
        suma = 0
        for i in range(30):  # todas las notas de esa sola materia tengo que sumar
            suma = suma + calificaciones[i][j]
        promedio = suma / 30
        promedios_materias[j] = promedio  

    max_prom = promedios_materias[0]
    for k in range(1, 5):
        if promedios_materias[k] > max_prom:
            max_prom = promedios_materias[k]

    for l in range(5):
        if promedios_materias[l] == max_prom:
            print(f"Materia_N{l+1} tiene el mayor promedio: {promedios_materias[l]}")
