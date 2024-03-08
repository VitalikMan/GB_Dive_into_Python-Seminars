# Задача:
# Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# Первое число int, второе - float разделены вертикальной чертой.
# Минимальное число - -1000, максимальное - +1000.
# Количество строк и имя файла передаются как аргументы функции.

from random import randint, uniform

MIN_NUM = -1000
MAX_NUM = 1000


def write_numbers(name, rows):
	with open(name, 'w') as f:
		for i in range(rows):
			f.write(f'{randint(MIN_NUM, MAX_NUM)} | {uniform(MIN_NUM, MAX_NUM)}\n')


if __name__ == '__main__':
	write_numbers('numbers1.txt', 20)
