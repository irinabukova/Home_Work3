# Задача 18: Требуется найти в массиве A[1..N] самый близкий
# по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

n = int(input('Ведите длину массива: '))
my_list = [random.randint(1,10) for i in range(n)]
print(my_list)

num_x = int(input('Введите искомое число: '))
my_list.append(num_x)
# print(my_list)
def max_ind (new_list: list):
    max = new_list[0]
    max_i = 0
    for i in range(len(my_list)):
        if max < my_list[i]:
            max = my_list[i]
            max_i = i
    return max_i

def sort (new_list: list):
    global sort_list
    sort_list = []
    for i in range(len(new_list)):
        sort_max = max_ind(new_list)
        sort_list.append(new_list.pop(sort_max))
    return sort_list

print (sort(my_list))

num = 0
for i in range(len(sort_list)):
    if num_x == sort_list[i]:
        num = sort_list[i+1]

print(f'Самый близкий по величине элемент к числу {num_x} - {num}')


