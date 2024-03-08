# Задание:
# Функция получает на вход список чисел.
# Отсортируйте его элементы in place без использования встроенных в язык сортировок.
# Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.
from random import random


def buble_sort(list_numbers: list[int]) -> None:
    for i in range(len(list_numbers) - 1):
        for j in range(i + 1, len(list_numbers)):
            if list_numbers[i] > list_numbers[j]:
                list_numbers[i], list_numbers[j] = list_numbers[j], list_numbers[i]


list_numbers = [1, 34, 67, 8884, 54]
buble_sort(list_numbers)
print(list_numbers)
