from constantes import CANTIDAD_ESTUDIANTES

def ordenar_por_promedio(nombres, generos, legajos, calificaciones, promedios, descendente=True):
    n = len(promedios)  # Usar el tamaño real de la lista de promedios
    for i in range(n-1):
        for j in range(n-1-i):
            if (descendente and promedios[j] < promedios[j+1]) or (not descendente and promedios[j] > promedios[j+1]):
                # Intercambiar en todas las listas
                aux = promedios[j]
                promedios[j] = promedios[j+1]
                promedios[j+1] = aux

                aux = nombres[j]
                nombres[j] = nombres[j+1]
                nombres[j+1] = aux

                aux = generos[j]
                generos[j] = generos[j+1]
                generos[j+1] = aux

                aux = legajos[j]
                legajos[j] = legajos[j+1]
                legajos[j+1] = aux

                aux = calificaciones[j]
                calificaciones[j] = calificaciones[j+1]
                calificaciones[j+1] = aux

    # Devolver los datos ordenados como tu menú espera
    datos_ordenados = []
    for i in range(n):
        datos_ordenados.append((promedios[i], nombres[i], generos[i], legajos[i], calificaciones[i]))
    return datos_ordenados