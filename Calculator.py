def add(a, b):
    return a + b


def subtract(a, b):
    return a-b


def multiple(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        print("Zero division!")
        exit()
    


first_num = int(input("Give first number:"))
second_num =int(input("Give second number:"))
