# Realizar un programa que lea la edad de una persona menor a 100 años e
# informe de si es un niño (0-12 años), un adolescente (13-17), un joven (18-29) o un
# adulto.
from utils.mi_entrada_salida import MiEntradaSalida


def solicitar_edad():
    return MiEntradaSalida.leer_entero_en_rango("introduce tu edad entre 0 y 100", 0, 100)


def informe_edad():
    edad = solicitar_edad()
    if edad >= 0 and edad <= 12:
        print("Eres un niño")
    elif edad >= 13 and edad <= 17:
        print("eres un adolescente")
    elif edad >= 18 and edad <= 29:
        print("eres jovencito")
    else:
        print("Ya eres un adulto")


if __name__ == '__main__':
    informe_edad()
