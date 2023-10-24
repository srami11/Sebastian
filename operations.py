def add(num_1, num_2):
    num_1 = int(input("Ingrese el primer numero: "))
    num_2 = int(input("Ingrese el segundo numero: "))
    result = num_1 + num_2
    print(f'{num_1} + {num_2} is equal to {result}')
    return result


def sub(num_1, num_2):
    num_1 = int(input("Ingrese el primer numero: "))
    num_2 = int(input("Ingrese el segundo numero: "))
    result = num_1 - num_2
    print(f'{num_1} - {num_2} is equal to {result}')
    return result

def multi(num_1, num_2):
    num_1 = int(input("Ingrese el primer numero: "))
    num_2 = int(input("Ingrese el segundo numero: "))
    result = num_1 * num_2
    print(f'{num_1} * {num_2} is equal to {result}')
    return result

def div(num_1, num_2):
    num_1 = int(input("Ingrese el primer numero: "))
    num_2 = int(input("Ingrese el segundo numero: "))
    result = num_1 / num_2
    print(f'{num_1} / {num_2} is equal to {result}')
    return result

def pote(num_1, num_2):
    num_1 = int(input("Ingrese el primer numero: "))
    num_2 = int(input("Ingrese el segundo numero: "))
    result = num_1 ** num_2
    print(f'{num_1} ** {num_2} is equal to {result}')
    return result

def module(num_1, num_2):
    num_1 = int(input("Ingrese el primer numero: "))
    num_2 = int(input("Ingrese el segundo numero: "))
    result = num_1 % num_2
    print(f'{num_1} % {num_2} is equal to {result}')
    return result