def limpiar_espacios(palabra: str) -> str:
    lista_frase = ""
    for caracter in palabra:
        if caracter != " ":
            lista_frase += caracter
    return lista_frase