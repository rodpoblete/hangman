def run():
    # Método 1
    lista = [i for i in range(1, 10000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]

    # Método 2 encontrando el mínimo común múltiplo de los 3 números entregados (4, 6 ,9)
    lista2 = [i for i in range(1, 10000) if i % 36 == 0]
    
    
    print(lista[:5])
    print(lista2[:5])


if __name__ == '__main__':
    run()