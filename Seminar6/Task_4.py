# Задача:
# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.


def secrets(riddle: str, answers: list[str], counter: int) -> int:
	print(riddle)
	for i in range(counter):
		ans = input("Введите ответ: ")
		if ans in answers:
			return i + 1
	return 0


def test_storage():
	dict_riddle = {'Зимой и летом одним цветом': ['ель', 'ёлка', 'сосна'],
				   'Не лает, не кусает, в дом не пускает': ['замок'],
				   'Сидит дед во сто шуб одет': ['лук', 'луковица'], }

	for test_data in dict_riddle.items():
		print(secrets(*test_data, counter=3))


if __name__ == '__main__':
	# print(secrets('Зимой и летом одним цветом', ['ель', 'ёлка', 'сосна'], 3))
	print(test_storage())
