# Задание:
# Функция получает на вход список чисел и два индекса.
# Вернуть сумму чисел между переданными индексами.
# Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.
# Если нижняя граница меньше нуля, суммируем от начала.
# Если верхняя граница больше длины списка, до конца.
from __future__ import annotations


def sum_numbers_between_indices(numbers: list[int|float],
                                start_index: int,
                                end_index: int) -> int|float:
    if start_index > end_index:
        start_index, end_index = end_index, start_index
    if end_index > len(numbers):
        end_index = len(numbers)
    if start_index < 0:
        start_index = 0
    return sum(numbers[start_index:end_index])

numbers = [1, 2, 3, 4, 5, 76, 77, 8, 9]

result = sum_numbers_between_indices(numbers, 0, 3)
print(result)
