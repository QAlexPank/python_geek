# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

total_list = [7, 14.5, "I'm not ashamed", ["a", "2"], {"name": "Max", "age": 23}, True, 15-2j, None]

for var in total_list:
    print(f"{var} is {type(var)}")
