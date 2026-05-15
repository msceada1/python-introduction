# Realizar un programa que lea la edad de una persona menor a 100 años e
# informe de si es un niño (0-12 años), un adolescente (13-17), un joven (18-29) o un
# adulto.
from utils.mi_entrada_salida import MiEntradaSalida


def solicitar_edad():
    return MiEntradaSalida.leer_entero_en_rango("introduce tu edad entre 0 y 100", 0, 100)
