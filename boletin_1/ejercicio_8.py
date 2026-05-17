# Realizar un programa que lea un carácter y dos números enteros por teclado.
# Si el carácter leído es un operador aritmético, calcular la operación correspondiente,
# si es cualquier otro debe mostrar un error.

def solicitar_numero():
    while True:
        try:
            numero = int(input("Introduce un numero entero:\n"))
            return numero
        except ValueError:
            print("Error de entrada de dato. Por favor intente de nuevo")


def solicitar_caracter():
    return input("introduce un operador aritmetico:\n")


def programa():
    numero_1 = solicitar_numero()
    numero_2 = solicitar_numero()
    caracter = solicitar_caracter()

    if caracter == '+':
        print(numero_1 + numero_2)
    elif caracter == '-':
        print(numero_1 - numero_2)
    elif caracter == '*':
        print(numero_1 * numero_2)
    elif caracter == '/':
        print(numero_1 / numero_2)
    else:
        print("ERROR")

if __name__ == '__main__':
    programa()