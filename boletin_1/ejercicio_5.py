# Realizar un programa que solicite 4 números e imprima la media de los
# números. También debe imprimir aquellos números que son superiores a la media.

def calcular_media(num_1, num_2, num_3, num_4):
    """
    devuelve la media de 4 numeros
    :param num_1: el primer numero
    :param num_2: el segundo numero
    :param num_3: el tercer numero
    :param num_4: el cuarto numero
    :return: la media
    """
    return (num_1 + num_2 + num_3 + num_4) / 4


def solicitar_numero():
    """
    solcita y valida un numero entero al usuario
    :return: un numero entero
    """
    while True:
        try:
            numero = int(input("introduce un numero entero"))
            return numero
        except ValueError:
            print("Error: ha introducido un dato incorrecto. Intentelo de nuevo")


def programa():
    numero_1 = solicitar_numero()
    numero_2 = solicitar_numero()
    numero_3 = solicitar_numero()
    numero_4 = solicitar_numero()
    media = calcular_media(numero_1, numero_2, numero_3, numero_4)

    print("La media de los numeros introducidos es", media)

    if numero_1 > media:
        print("El numero", numero_1, "es mayor que la media")
    if numero_2 > media:
        print("El numero", numero_2, "es mayor que la media")
    if numero_3 > media:
        print("el numero", numero_3, " es mayor que la media")
    if numero_4 > media:
        print("El numero", numero_4, " es mayor que la media")

if __name__ == '__main__':
    programa()