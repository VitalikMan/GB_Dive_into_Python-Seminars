# Задание:
# Продолжаем развивать задачу 2.
# Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.


text = "Самостоятельно сохраните в переменной строку текста."
my_dict = {item: ord(item) for item in text}
print(my_dict)

my_dict_iterator = iter(my_dict.items())

for _ in range(5):
	print(next(my_dict_iterator))

# print(item)
#
# item = next(my_dict_iterator)
# print(item)
#
# item = next(my_dict_iterator)
# print(item)
#
# item = next(my_dict_iterator)
# print(item)
#
# item = next(my_dict_iterator)
# print(item)
