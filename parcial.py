#trabajo practico para el parcial 
from import_pp import get_int 
from cargar_datos import cargar_datos
from ordenar_prom import ordenar_por_promedio
from ordenar_mayor import materia_mayor_promedio
from legajo import buscar_por_legajo
from contar_notas import contar_calificaciones
from calcular_promedios import calcular_promedios
from validar_genero import validar_genero
from mostrar_todos_los_datos import mostrar_todos_los_datos

CANTIDAD_ESTUDIANTES = 3  # Cambia a 30 para la entrega final
CANTIDAD_MATERIAS = 2     # Cambia a 5 para la entrega final

datos_cargados = False
while True:
    print("""
    1 - CARGAR DATOS
    2 - MOSTRAR TODOS LOS DATOS
    3 - CALCULAR PROMIEDOS
    4 - ORDENAR POR PROMIEDO
    5 - MATERIA(S) CON MAYOR PROMEDIO
    6 - BUSCAR ESTUDIANTE(POR LEGAJO)
    7 - CONTAR REPETICIONES DE UNA CALIFICACION POR MATERIA
    8 - Salir
    """)
    opcion = get_int("Seleccione una opción: ")
    match opcion:
        case 1:
            nombres, genero, legajo, calificaciones = cargar_datos()
            datos_cargados = True
            promedios = [] 
        case 2:
            if datos_cargados:
                mostrar_todos_los_datos(nombres, genero, legajo, calificaciones)
            else:
                print("Primero debe cargar los datos.")
        case 3:
            if datos_cargados:
                promedios = calcular_promedios(calificaciones)
                print("Promedios de cada estudiante:")
                for i in range(len(promedios)):
                    print(f"{nombres[i]} (Legajo {legajo[i]}): {promedios[i]:.2f}")
            else:
                print("Primero debe cargar los datos.")
        case 4:
            if datos_cargados:
                if not promedios:
                    promedios = calcular_promedios(calificaciones)
                datos_ordenados = ordenar_por_promedio(nombres, genero, legajo, calificaciones, promedios, descendente=True)
                print("Estudiantes ordenados por promedio (descendente):")
                for prom, nom, gen, leg, calif in datos_ordenados:
                    print(f"{nom} | Género: {gen} | Legajo: {leg} | Calificaciones: {calif} | Promedio: {prom:.2f}")
            else:
                print("Primero debe cargar los datos.")
        case 5:
            if datos_cargados:
                materia_mayor_promedio(calificaciones)
            else:
                print("Primero debe cargar los datos.")
        case 6:
            if datos_cargados:
                if not promedios:
                    promedios = calcular_promedios(calificaciones)
                buscar_por_legajo(nombres, genero, legajo, calificaciones, promedios)
            else:
                print("Primero debe cargar los datos.")
        case 7:
            if datos_cargados:
                materia = get_int(f"Ingrese el número de la materia (1 a {CANTIDAD_MATERIAS}): ")
                if 1 <= materia <= CANTIDAD_MATERIAS:
                    conteo = contar_calificaciones(calificaciones, materia)
                    print(f"Repeticiones de cada calificación en MATERIA_{materia}:")
                    for i in range(len(conteo)):
                        print(f"Nota {i+1}: {conteo[i]} vez/veces")
                else:
                    print("Número de materia inválido.")
            else:
                print("Primero debe cargar los datos.")
        case 8:
            print("adios")
            break
        case _:
            print("Opción inválida.")