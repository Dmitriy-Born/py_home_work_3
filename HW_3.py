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

