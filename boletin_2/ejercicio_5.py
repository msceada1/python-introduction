from utils.mi_entrada_salida import MiEntradaSalida

SEGUNDOS_DE_UNA_HORA = 3600


def convertir_horas_a_segundos(horas):
    return horas * SEGUNDOS_DE_UNA_HORA


if __name__ == '__main__':
    horas = MiEntradaSalida.leer_entero_positivo("Introduce un numero de horas")
    print("Las horas introducidas en segundos equivalen a ", convertir_horas_a_segundos(horas))
