# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

count = abs(int(input('Введите целое положительное число >>> ')))
max_count = count % 10
while count >= 1:
    count = count // 10
    if count % 10 > max_count:
        max_count = count % 10
    if count > 9:
        continue
    else:
        print("Максимальное цифра в числе ", max_count)
        break
