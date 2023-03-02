# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств


# первый вариант

import random
import time

n = int(input("Введите количество элементов первого множества: "))
f_list = [random.randint(0, 100) for _ in range(n)]

m = int(input("Введите количество элементов второго множества: "))
s_list = [random.randint(0, 100) for _ in range(m)]

print(f_list)
f_set = set(f_list)
print(f_set)

print(s_list)
s_set = set(s_list)
print(s_set)

start = time.perf_counter()
all_list = set()
for i in f_set:
    for j in s_set:
        if i == j:
            all_list.add(i)
end = time.perf_counter()
print(all_list)

print(end-start)


# второй вариант

n = int(input("Введите количество элементов первого множества: "))

first_list = set()

for i in range(n):
    first_list.add(input("Введите элементы первого множества: "))
print(first_list)

m = int(input("Введите количество элементов второго множества: "))
second_list = set()
for i in range(m):
    second_list.add(input("Введите элементы первого множества: "))
print(second_list)

new_list = first_list.intersection(second_list)
print(sorted(new_list))





# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.


n = int(input("Введите количество кустов: "))
garden_bed = [random.randint(1, 100) for _ in range(n)]

print(garden_bed)

max_sum = []
for i in range(0, len(garden_bed)-2):
    max_sum.append(garden_bed[i]+garden_bed[i+1]+garden_bed[i+2])
max_sum.append(garden_bed[0]+garden_bed[1]+garden_bed[-1])
max_sum.append(garden_bed[0]+garden_bed[-1]+garden_bed[-2])

print(max(max_sum))
