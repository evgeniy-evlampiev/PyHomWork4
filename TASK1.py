# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

n = int(input('Введи кол-во элементов 1-ого множества: '))
m = int(input('Введи кол-во элементов 2-ого множества: '))
list_1 = set(map(int, input(f'Введи {n} числа через пробел: ').split()))
list_2 = set(map(int, input(f'Введи {m} числа через пробел: ').split()))
n = len(list_1)
m = len(list_2)
list_3 = list_1.intersection(list_2)

print(f'список уникальных чисел {sorted(list_3)}')
