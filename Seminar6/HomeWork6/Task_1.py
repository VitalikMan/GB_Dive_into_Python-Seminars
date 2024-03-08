# Задание:
# Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем.
# На вход будет подаваться дата в формате "день.месяц.год".
# Ваша задача - создать программу, которая проверяет, является ли введенная дата корректной или нет.
# Ваша программа должна предоставить ответ "True" (дата корректна) или "False" (дата некорректна)
# в зависимости от результата проверки.
#
# Пример использования:
# На входе:
date_to_prove = '15.4.2023'
# На выходе:
# True
#
# На входе:
# date_to_prove = '31.6.2022'
# На выходе:
# False


MONTHS = {
	1: range(1, 32),
	2: range(1, 29),
	3: range(1, 32),
	4: range(1, 31),
	5: range(1, 32),
	6: range(1, 31),
	7: range(1, 32),
	8: range(1, 32),
	9: range(1, 31),
	10: range(1, 32),
	11: range(1, 31),
	12: range(1, 32)
}


def parser_date(date: str) -> bool:
	d, m, y = map(int, date.split('.'))
	return _y_is_valid(y) and _m_is_valid(m) and _d_is_valid(d, m, y)


def _d_is_valid(d: int, m: int, y: int) -> bool:
	if _is_leap_year(y) and m == 2:
		return d in range(1, 30)
	return d in MONTHS[m]


def _m_is_valid(m) -> bool:
	return m in range(1, 13)


def _y_is_valid(y) -> bool:
	return y in range(1, 3_000)


def _is_leap_year(y):
	return y % 4 == 0 and y % 100 != 0 or y % 400 == 0


print(parser_date(date_to_prove))
