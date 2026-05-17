# Una pastelería nos ha pedido realizar un programa que calcule el
# presupuesto de las tartas que fabrica.
# El programa preguntará primero de qué tipo quiere la tarta (M- Manzana, F-Fresa o
# C-Chocolate). La tarta de manzana vale 12 euros y la de fresa 16. En caso de
# seleccionar la tarta de chocolate, el programa debe preguntar además si el
# chocolate es negro o blanco; la primera opción vale 14 euros y la segunda 15.
# Por último, en cualquiera de los tipos de tarta, se pregunta si se añade nata y si se
# personaliza con un nombre; la nata suma 2.50 y la escritura del nombre 2.75.
# Para simplificar el ejercicio, puede suponerse que los datos de entrada son
# correctos, es decir, no debe validarse ningún dato de entrada.
from utils.mi_entrada_salida import MiEntradaSalida

PRECIO_TARTA_MANZANA = 12
PRECIO_TARTA_FRESA = 16
PRECIO_TARTA_CHOCOLATE_NEGRO = 14
PRECIO_TARTA_CHOCOLATE_BLANCO = 16
PRECIO_NATA = 2.5
PRECIO_ESCRITURA = 2.75


def solicitar_tarta():
    tarta = input("¿Que tarta deseas? M-Manzana, F-Fresa, CN-Chocolate Negro, CB-Chocolate Blanco").lower()

    while tarta != "m" and tarta != "f" and tarta != "cn" and tarta != "cb":
        print("Por favor, seleccione un tipo de tarta")
        tarta = input("¿Que tarta deseas? M-Manzana, F-Fresa, CN-Chocolate Negro, CB-Chocolate Blanco").lower()

    return tarta


def solicitar_nata():
    respuesta = MiEntradaSalida.leer_caracter_sn("desea añadir nata a la tarta?").lower()
    if respuesta == 's':
        return True
    else:
        return False


def solicitar_escritura():
    respuesta = MiEntradaSalida.leer_caracter_sn("desea escribir algun nombre en la tarta?").lower()
    if respuesta == 's':
        return True
    else:
        return False


#def programa():
