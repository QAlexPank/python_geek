#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def calculator(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return
    return result


try:
    n1 = float(input("Введите 'a' = "))
    n2 = float(input("Введите  'b' = "))
    print(f"a / b = {calculator(n1, n2)}")
except ValueError:
    print("Указано не верное значение")