def limpiar_espacios(palabra:str)->str:
    lista_frase=""
    for i in range(len(palabra)):
        if palabra[i] != " ":
            lista_frase+=palabra[i]
    return lista_frase