# Задание:
# Пользователь вводит строку из четырёх или более целых чисел, разделённых символом “/”.
# Сформируйте словарь, где:
# - второе и третье число являются ключами
# - первое число является значением для первого ключа
# - четвертое и все возможные последующие числа хранятся в кортеже как значения второго ключа

numbers = list(map(int, input("Введите 4 числа, разделенных / : ").split('/')))
numbers_dict = {numbers[1]: numbers[0], numbers[2]: tuple(numbers[3:])}
print(numbers_dict)