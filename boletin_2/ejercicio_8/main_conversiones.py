from utils.mi_entrada_salida import MiEntradaSalida
import conversiones

def solcitar_grados():
    return MiEntradaSalida.leer_entero_positivo("Introduce los grados:\n")

if __name__ == '__main__':
    print(conversiones.celsius_a_farenheit(solcitar_grados()))
    print(conversiones.farenheit_a_celsius(solcitar_grados()))