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
    with open("./archivos/data.txt", "r", encoding="utf-8") as file:
        for line in file:
            word_list.append(line.strip())
    dict_words = dict(enumerate(word_list))
    # return dict_words

    random_word = dict_words.get(random.randint(0, len(dict_words)))
    print(random_word)

    size_word = len(random_word)
    revealed_word = list(random_word)
    hidden_word = [character for i in range(size_word)]
    listToStr = " ".join([str(elem) for elem in hidden_word])

    letra = input("Ingrese una letra: ")
    for i in range(len(revealed_word)):
        if revealed_word[i] == letra:
            hidden_word[i] = letra
            listToStr = " ".join([str(i) for i in hidden_word])
    print(hidden_word)
    print(listToStr)
    # hidden_word[revealed_word.index(letra)] = letra
    # listToStr = " ".join([str(elem) for elem in hidden_word])
    # print(listToStr)

    # while True:
    #     os.system("clear")
    #     print(revealed_word)
    #     print(hidden_word)
    #     print(size_word)
    #     print(listToStr)
    #     letra = input("Ingrese una letra: ")
    #     filter_letter = filter(lambda a: letra in a, revealed_word)
    #     print(filter_letter)
    # if letra in revealed_word:
    #     hidden_word[revealed_word.index(letra)] = letra
    #     print(hidden_word)
    # else:
    #     continue


def choice_word():
    pass


def run():
    read_words()


if __name__ == "__main__":
    run()
