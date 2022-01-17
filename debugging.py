def divisors(num):
    if num <= 0:
        raise Exception("El número debe ser positivo")
    else:
        divisors = [i for i in range(1, num + 1) if num % i == 0]
        return divisors


def run():
    try:
        num = int(input("Enter a number: "))
        print(divisors(num))
    except ValueError:
        print("Sólo puedes ingresar números")


if __name__ == "__main__":
    run()
