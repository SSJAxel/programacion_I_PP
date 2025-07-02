from constantes import CANTIDAD_ESTUDIANTES, CANTIDAD_MATERIAS

def mostrar_todos_los_datos(nombres, generos, legajos, calificaciones):
    print("Legajo   Nombre                Género  Calificaciones")
    print("-" * 60)
    for i in range(CANTIDAD_ESTUDIANTES):
        print(legajos[i], nombres[i], generos[i], end="  ")
        for j in range(CANTIDAD_MATERIAS):
            print(calificaciones[i][j], end=" ")
        print()