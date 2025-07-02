from validar_genero import validar_genero
from import_pp import get_int

def cargar_datos():
    # cargamos los datos de cada alumno
    #tenemos en cuenta las validaciones para cada una
    
    nombres = [""] * 30
    for i in range(30):
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


    genero = [""] * 30
    for i in range(30):
        genero[i] = validar_genero()



    calificaciones = [[0]*5 for _ in range(30)]
    for i in range(30):
        for j in range(5):
            while True:
                nota = get_int(f"Ingrese la calificación {j+1} del estudiante {i+1} (1 a 10): ")
                if 1 <= nota <= 10:
                    calificaciones[i][j] = nota
                    break
                else:
                    print("La calificación debe ser un número entre 1 y 10.")   



    legajo = [0] * 30
    for i in range(30):
        while True:
            leg = get_int(f"Ingrese el legajo del estudiante {i+1} (5 cifras): ")
            if 10000 <= leg <= 99999:
                #me aseguro que no esté ya en la lista
                if leg not in legajo[:i]:  # Solo compara con los ya ingresados
                    legajo[i] = leg
                    break
                else:
                    print("Ese legajo ya fue ingresado. Debe ser único.")
            else:
                print("El legajo debe ser un número entero de 5 cifras.")
    
    return nombres, genero, legajo, calificaciones