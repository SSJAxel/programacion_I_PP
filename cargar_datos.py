from constantes import CANTIDAD_ESTUDIANTES, CANTIDAD_MATERIAS
from validar_genero import validar_genero
from import_pp import get_int

def cargar_datos():
    nombres = [""] * CANTIDAD_ESTUDIANTES
    for i in range(CANTIDAD_ESTUDIANTES):
        while True:
            nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
            vacio = True
            for c in nombre:
                if c != " ":
                    vacio = False
            if not vacio:
                nombres[i] = nombre
                break
            else:
                print("El nombre no puede estar vacío. Pruebe nuevamente.")

    genero = [""] * CANTIDAD_ESTUDIANTES
    for i in range(CANTIDAD_ESTUDIANTES):
        genero[i] = validar_genero()

    calificaciones = [[0]*CANTIDAD_MATERIAS for _ in range(CANTIDAD_ESTUDIANTES)]
    for i in range(CANTIDAD_ESTUDIANTES):
        for j in range(CANTIDAD_MATERIAS):
            while True:
                nota = get_int(f"Ingrese la calificación {j+1} del estudiante {i+1} (1 a 10): ")
                if 1 <= nota <= 10:
                    calificaciones[i][j] = nota
                    break
                else:
                    print("La calificación debe ser un número entre 1 y 10.")   

    legajo = [0] * CANTIDAD_ESTUDIANTES
    for i in range(CANTIDAD_ESTUDIANTES):
        while True:
            leg = get_int(f"Ingrese el legajo del estudiante {i+1} (5 cifras): ")
            if 10000 <= leg <= 99999:
                if leg not in legajo[:i]:
                    legajo[i] = leg
                    break
                else:
                    print("Ese legajo ya fue ingresado. Debe ser único.")
            else:
                print("El legajo debe ser un número entero de 5 cifras.")
    
    return nombres, genero, legajo, calificaciones