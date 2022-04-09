#5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def sum(list):
    items_sum = 0
    for item in list:
        try:
            items_sum += float(item)
        except ValueError:
            continue
    return items_sum


def sum_of_string(s):
    s = s.replace('$', '')
    s = s.replace(',', '.')
    numbers = s.split(' ')
    return sum(numbers)


numbers_sum = 0

while True:
    numbers_sting = input("Укажите строку чисел через пробел. Для завершения укажите символ '$'\n")
    numbers_sum += sum_of_string(numbers_sting)
    if numbers_sum != 0:
        print(f"Общая сумма указанных чисел = {numbers_sum}")
    if numbers_sting.count('$') > 0:
        break