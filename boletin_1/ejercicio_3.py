# Realizar un programa que lea un número por teclado. El programa debe
# imprimir en pantalla un mensaje con “El número xx es múltiplo de 2” o un mensaje
# con “El número xx es múltiplo de 3”. Si es múltiplo de 2 y de 3 deben aparecer los
# dos mensajes. Si no es múltiplo de ninguno de los dos el programa finaliza sin
# mostrar ningún mensaje.

def es_multiplo_de_dos(numero):
    """
    Comprueba si un numero es multiplo de dos
    :param numero: el numero a comprobar
    :return: si es o no es multiplo
    """
    return numero / 2 == 0


def es_multiplo_de_tres(numero):
    """
    comprueba si un numero es multiplo de tres
    :param numero: el numero a comprobar
    :return: si es o no es multiplo
    """
    return numero / 3 == 0


def solicitar_numero_entero():
    """
    solicita y valida que el numero sea entero
    :return: un numero entero
    """
    while True:
        try:
            numero = int(input("Introduce un numero entero:\n"))
            return numero
        except ValueError:
            print("Error: Formato no valido")


if __name__ == '__main__':
    numero = solicitar_numero_entero()
    if es_multiplo_de_dos(numero) and es_multiplo_de_tres(numero):
        print("El numero", numero, " es multiplo de dos y tres")
    elif es_multiplo_de_dos(numero):
        print("el numero", numero, " es multiplo de dos")
    else:
        print("El numero", numero, "es multiplo de tres")
