# Задача 2:
# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и значение по умолчанию.
# При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.

def get_value(dictionary, key, default_value=None):
	try:
		return dictionary[key]
	except KeyError:
		return default_value


my_dict = {'one': 1, 'two': 2, 'three': 3}

key1 = 'two'
print(get_value(my_dict, key1))
print(get_value(my_dict, 'fsdfsd', default_value=12))
