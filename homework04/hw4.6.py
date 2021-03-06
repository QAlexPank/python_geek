#6. Реализовать два небольших скрипта:
#а) итератор, генерирующий целые числа, начиная с указанного,
#б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
#Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
#Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

#Скрипт "а":
from itertools import count
print("'Итератор генерирующий целые числа, начиная с указанного'")
n = int(input("Укажите целое число:"))

for i in count(n):
    print(i)

#Скрипт "б":
from itertools import cycle
print("'Итератор повторяющий элементы некоторого списка, определенного заранее'")
list = [5, 3, 3, 1, 0, 4, 2, 4, 7, 3]
for i in cycle(list):
    print(i)