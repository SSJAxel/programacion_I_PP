def get_int(mensaje="Ingrese un número entero: "):
    while True:
        entrada = input(mensaje)
        es_numero = True
        if entrada == "":
            es_numero = False
        else:
            for c in entrada:
                if c < "0" or c > "9":
                    es_numero = False
        if es_numero:
            # Convertir a entero manualmente
            numero = 0
            for c in entrada:
                numero = numero * 10 + (ord(c) - ord("0"))
            return numero
        else:
            print("¡Error! Debe ingresar un número entero válido.")