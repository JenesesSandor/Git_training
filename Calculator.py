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

def square(a,b):
    pass



first_num = int(input("Give first number:"))
second_num =int(input("Give second number:"))
print(add(first_num,second_num))
print(subtract(first_num,second_num))
print(multiple(first_num,second_num))
print(divide(first_num,second_num))
