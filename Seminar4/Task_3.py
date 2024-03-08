# Задача:
# - Функция получает на вход строку из двух чисел через пробел.
# - Сформируйте словарь, где ключом будет символ из Unicode, а значением — целое число.
# - Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.

def get_unicode_dict(diapason: str) -> dict[str, int]:
	"""'
	Возвращает словарь, где ключом будет символ из Unicode, а значением — целое число.
	:param diapason:
	:return:
	>>> get_unicode_dict("1 10")
	1     1
	2     2
	3     3
	4     4
	5     5
	6     6
	7     7
	8     8
	9     9
	10   10
	"""''
	start, end = map(int, diapason.split())
	result = {}
	for i in range(min(start, end), max(start, end)):
		result[chr(i)] = i
	return result


print(get_unicode_dict("1 10"))
