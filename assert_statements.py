def divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors


def run():
    num = input("Enter a number: ")
    assert num.isnumeric() and int(num) > 0, "Debes ingresar un número positivo válido"
    print(divisors(int(num)))


if __name__ == "__main__":
    run()
