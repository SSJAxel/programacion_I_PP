def mostrar_todos_los_nombres(nombres, genero, legajo, calificaciones):
    for i in range(30):
        mostrar_un_nombre(i, nombres, genero, legajo, calificaciones)

def mostrar_un_nombre(i, nombres, genero, legajo, calificaciones):
    print(f"Estudiante {i+1}: {nombres[i]}, Género: {genero[i]}, Legajo: {legajo[i]}, Calificaciones: {calificaciones[i]}")
