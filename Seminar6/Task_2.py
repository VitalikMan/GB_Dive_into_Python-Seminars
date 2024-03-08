# Задача:
# Улучшаем задачу 1.
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.
from random import randint as rnd
from sys import argv


def guess(min_numb, max_numb, count):
	random_numb = rnd(min_numb, max_numb)
	for i in range(count):
		numb = int(input('Введите число: '))
		if numb == random_numb:
			return True
		elif numb > random_numb:
			print("Меньше")
		else:
			print("Больше")
	return False


if __name__ == '__main__':
	print(guess(*list(map(int, argv[1:]))))
