import random
import os
os.system('cls')

task = int(input("Введите номер задания(16, 18 или 20): "))
if task == 16:
    print("Задача №16")
        # Задача 16:
    # Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
    # Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
    # Заполните массив случайными натуральными числами от 1 до N/2.
    # Выведите, сколько раз X встречается в массиве.

    # Ввод: 5
    # Ввод: 1

    # 1 2 1 2 2
    # Вывод: 2

    N = int(input("Введите количество элементов массива: "))
    rand = []
    for i in range(0, 10):
        rand.append(random.randint(1, N//2))
    print(rand)

    X = int(input("Введите число для проверки: "))

    count = 0
    for i in range(0, N):
        if rand[i] == X:
            count += 1
    print(f"Число {X} встречается в последовательности {count} раз(-а)")    
#############################################

if task == 18:
    print("Задача №18")
    # Задача 18:
    # Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
    # Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
    # Заполните массив случайными натуральными числами от 1 до N.
    # Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.

    # Ввод: 10
    # Ввод: 7
    # 1 2 1 8 9 6 5 4 3 4
    # Вывод: 6
    # import math

    N = int(input("Введите количество элементов массива: "))
    B = []
    for i in range(0, 10):
        B.append(random.randint(1, N))
    print(B)

    A = sorted(B)

    X = int(input("Введите число для проверки: "))

    number = 0
    temp = abs(A[0] - X)
    for i in range (1, N):
        if X == A[i] or X == A[0]:
            print("Такой элемент есть в данной последовательности")
            quit()

        if abs(A[i] - X) < temp:
            temp = abs(A[i] - X)
            number = A[i]

    if number == 0:
        number = A[0]
        
    print (f"Искомое число = {number}")           

    for i in range (0,N):
        if (X - (number - X)) == A[i]:
            temp_2 = A[i]
            print (f"Второе число, равноудаленное от искомого с большей стороны = {temp_2}")
            quit()
#############################################

if task == 20:
    print("Задача №20")
    # Задача 20:

    # Напишите программу, которая вычисляет стоимость введенного пользователем слова.
    # Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

    # Ввод: ноутбук
    # Вывод: 12

    dictionary = \
        {
        "A" :1, "E" :1, "I" :1, "O" :1, "U" :1, "L" :1, "N" :1, "S" :1, "T" :1, "R" :1, "А" :1, "В" :1, "Е" :1, "И" :1, "Н" :1, 
        "О" :1, "Р" :1, "С" :1, "Т" :1,
        "D" :2, "G" :2, "Д" :2, "К" :2, "Л" :2, "М" :2, "П" :2, "У" :2,
        "B" :3, "C" :3, "M" :3, "P" :3, "Б" :3, "Г" :3, "Ё" :3, "Ь" :3, "Я" :3,
        "F" : 4, "H" : 4, "V" : 4, "W" : 4, "Y" : 4, "Й" : 4, "Ы" : 4,
        "K" :5, "Ж" :5, "З" :5, "Х" :5, "Ц" :5, "Ч" :5,
        "J" :8, "X" :8, "Ш" :8, "Э" :8, "Ю" :8,
        "Q" :10, "Z" :10, "Ф" :10, "Щ" :10, "Ъ" :10
        }

    word = input ("Введите слово для проверки (ТОЛЬКО на русском или английском языке!): ")
    word = word.upper()
    itog = 0

    for i in word:
        itog += dictionary[i]

    print (f"Стоимость слова {word} составляет {itog} единиц")

else:
    print("Такой задачи не делали")