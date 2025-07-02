def mostrar_todos_los_datos(nombres, generos, legajos, calificaciones):
    print("Legajo   Nombre                Género  Calificaciones")
    print("-" * 60)
    for i in range(30):
        print(legajos[i], nombres[i], generos[i], end="  ")
        for j in range(5):
            print(calificaciones[i][j], end=" ")
        print()