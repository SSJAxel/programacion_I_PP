def get_int(mensaje="Ingrese un número entero: "):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("¡Error! Debe ingresar un número entero válido.")