# # # Задача:
# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его
# за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина,
# а если попытки исчерпаны - ложь.
from random import randint as rnd


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
	print(guess(2, 5, 3))
