# Define una tupla llamada dias_semana con los nombres de los días de la semana.
# 1. Imprime el tercer día (miércoles) accediendo por su índice.
# 2. Intenta cambiar el primer elemento a "Domingo" y observa qué sucede. Explica por
# qué ocurre eso.













if __name__ == '__main__':
    dias_semana = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")

    print(dias_semana[2])

    #da error porque la tupla no admite duplicados
    dias_semana[0] = "Domingo"