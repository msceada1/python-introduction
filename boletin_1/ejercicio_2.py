# Realizar un programa que solicite dos números por teclado e imprima en
# pantalla si son iguales, el primero mayor que el segundo o el primero más pequeño
# que el segundo.

def comprobar_mayor_menor_igual(num_1, num_2):
    """
    Comprueba si dos numeros son iguales o uno es mayor/menor que otro
    :param num_1: el primer numero a evaluar
    :param num_2: el segundo numero a evaluar
    """
    if num_1 > num_2:
        print("El numero", num_1, "es mayor que el numero", num_2)
    elif num_2 > num_1:
        print("El numero", num_2, "es mayor que el numero", num_1)
    else:
        print("Los numeros", num_1, "y", num_2, "son iguales")


def solicitar_numero():
    """
    solicita un numero entero por consola
    :return: un numero entero
    """
    while True:
        try:
            numero = int(input("Introduce un numero:\n"))
            return numero
        except ValueError:
            print("Error: Debes introducir un numero entero")


if __name__ == '__main__':
    comprobar_mayor_menor_igual(solicitar_numero(), solicitar_numero())
