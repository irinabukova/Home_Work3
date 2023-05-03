# *Задача 20:
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков; J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо
# только английские, либо только русские буквы.
#
# *Пример:*
# ноутбук
#     12
one = ('A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т')
two = ('D, G, Д, К, Л, М, П, У')
three = ('B, C, M, P, Б, Г, Ё, Ь, Я')
four = ('F, H, V, W, Y, Й, Ы')
five = ('K, Ж, З, Х, Ц, Ч')
six = ('J, X, Ш, Э, Ю')
ten = ('Q, Z, Ф, Щ, Ъ')

word = input('Введите слово: ')
word = word.upper()
sum = 0

for skr in one:
    for char in word:
        if char == skr:
            sum +=1

for skr in two:
    for char in word:
        if char == skr:
            sum +=2

for skr in three:
    for char in word:
        if char == skr:
            sum += 3
for skr in four:
    for char in word:
        if char == skr:
            sum += 4
for skr in five:
    for char in word:
        if char == skr:
            sum += 5
for skr in six:
    for char in word:
        if char == skr:
            sum += 6

for skr in ten:
    for char in word:
        if char == skr:
            sum += 10
print(sum)