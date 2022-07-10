def add(n1, n2):
    return n1 + n2


def subtract(res_add, n3):
    return res_add - n3


def add_and_sub(n1, n2, n3):
    result = add(n1, n2)
    return subtract(result, n3)


num1 = int(input())
num2 = int(input())
num3 = int(input())

print(add_and_sub(num1, num2, num3))
