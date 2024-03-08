# Задача 1:
# Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор,
# пока он не введёт целое или вещественное число.
# Обрабатывайте не числовые данные как исключения.

def get_numbers():
	while True:
		try:
			number = float(input('Введите число: '))
			return number
		except ValueError:
			print('Введите число!')


number = get_numbers()
print(f'Вы ввели: {number}')

# Задач
