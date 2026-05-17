# Realizar un programa que lea el estado civil de una persona (S-Soltero, CCasado, V-Viudo y D-Divorciado) y su edad. Después debe mostrar por pantalla el
# porcentaje de retención que debe aplicársele de acuerdo con las siguientes reglas:
# • A los solteros o divorciados menores de 35 años, un 12%
# • Todas las personas mayores de 50 años, un 8.5%
# • A los viudos o casados menores de 35 años, un 11.3%
# • Al resto de casos se le aplica un 10.5%
from utils.mi_entrada_salida import MiEntradaSalida
from sys import maxsize as max

PORCENTAJE_RETENCION_SOLTEROS_O_DIVORCIADOS_MENORES_DE_35 = 0.12
PORCENTAJE_RETENCION_VIUDOS_O_CASADOS_MENORES_DE_35 = 0.113
PORCENTAJE_RETENCION_MAYORES_DE_50 = 0.085
PORCENTAJE_RETENCION_RESTO_DE_CASOS = 0.105


def solicitar_estado_civil():
    estado_civil = input(
        "Selecciona el CARACTER correspondiente a tu estado civil: S-Soltero, C-Casaso, V-Viudo, D-Divorciado\n").lower()
    while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
        estado_civil = input(
            "Selecciona el CARACTER correspondiente a tu estado civil: S-Soltero, C-Casaso, V-Viudo, D-Divorciado\n").lower()
    return estado_civil


def solicitar_edad():
    return MiEntradaSalida.leer_entero_en_rango("Introduce tu edad:\n", 0, max)


def mostrar_porcentaje(estado_civil, edad):
    if (estado_civil == 's' or estado_civil == 'd') and edad < 35:
        print("Te corresponde un porcentaje del ", PORCENTAJE_RETENCION_SOLTEROS_O_DIVORCIADOS_MENORES_DE_35)
    elif (estado_civil == 'v' or estado_civil == 'c') and edad < 35:
        print("Te corresponde un descuento del", PORCENTAJE_RETENCION_VIUDOS_O_CASADOS_MENORES_DE_35)
    elif edad > 50:
        print("Te corresponde un porcentaje del", PORCENTAJE_RETENCION_MAYORES_DE_50)
    else:
        print("Te corresponde un porcentaje del", PORCENTAJE_RETENCION_RESTO_DE_CASOS)


def programa():
    estado_civil = solicitar_estado_civil()
    edad = solicitar_edad()
    mostrar_porcentaje(estado_civil, edad)


if __name__ == '__main__':
    programa()
