from lib2to3.pytree import convert
import os
import random

# REGLAS
# Incorpora list comprehensions, manejo de errores y manejo de archivos
# Utiliza el archivo data.txt y leelo para obtener las palabras.

# AYUDAS Y PISTAS
# investiga la función enumerate()
# El método get de los diccionarios puede servirte
# La sentencia os.system("clear") puede ser útil para limpiar pantalla

# MEJORAR EL JUEGO
# Añade sistema de puntuación
# Dibuja el "Ahorcado" en cada jugada con Código ASCII
# Mejora la interfaz


def read_words():
    word_list = []
    dict_words = {}
    character = "_"
    revealed_word = []
    attempts = 0

    with open("./archivos/data.txt", "r", encoding="utf-8") as file:
        for line in file:
            word_list.append(line.strip())
    dict_words = dict(enumerate(word_list))
    random_word = dict_words.get(random.randint(0, len(dict_words)))

    size_word = len(random_word)
    revealed_word = list(random_word)
    hidden_word = [character for i in range(size_word)]
    hidden_word_to_string = " ".join([str(elem) for elem in hidden_word])

    while hidden_word != revealed_word:
        os.system("clear")
        print(random_word)
        print(hidden_word_to_string + "\n")
        letra = input("Ingrese una letra: ")
        for i in range(len(revealed_word)):
            if revealed_word[i] == letra:
                hidden_word[i] = letra
                hidden_word_to_string = " ".join([str(i) for i in hidden_word])
            else:
                attempts += 1
                continue
    os.system("clear")
    print(hidden_word_to_string + "\n")
    print("Felicidades, ganaste!")


def choice_word():
    pass


def run():
    read_words()


if __name__ == "__main__":
    run()
