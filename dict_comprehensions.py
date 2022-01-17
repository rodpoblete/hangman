# RETO 1:
# Crear un diccionario cuyas keys sean los 100 primernos números naturales
# y cuyos valores sean esos números elevados al cubo.

# RETO 2:
# Crear un diccionario cuyas keys sean los 1000 primernos números naturales
# y cuyos valores sean las raíces cuadradas de esos números.

from math import sqrt


def run():
    # Reto 1:
    dict_nums = {i: i ** 3 for i in range(1, 101)}
    dict_nums_2 = {i: i ** 3 for i in range(1, 101) if i % 3 != 0}

    # print(dict_nums)
    # print(dict_nums_2)

    # Reto 2:
    dict_nums_3 = {i: round(sqrt(i), 2) for i in range(1, 1001)}

    print(dict_nums_3)


if __name__ == "__main__":
    run()
