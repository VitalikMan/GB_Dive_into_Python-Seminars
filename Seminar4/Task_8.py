# Задача:
# Создайте несколько переменных заканчивающихся и не оканчивающихся на “s”.
# Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

number = 1
numbers = [1, 2]
s = 's'


def get_attributes_and_wth_s_():
	return list(filter(lambda v: not v.startswith('__')
								 and v.endswith('s')
								 and len(v) != 1,
					   globals()))


attributes_and_wth_s_ = get_attributes_and_wth_s_()
print(f'Res = {attributes_and_wth_s_}')

for attribute in attributes_and_wth_s_:
	globals()[attribute[:-1]] = globals()[attribute]
	globals()[attribute] = None

print(f'{number=}, {numbers=}')

# java, python, rust, javas, pythons, s = range(6)
#
#
# def fn():
#     for k, v in globals().items():
#         if len(k) > 1 and k.endswith("s"):
#             globals()[k] = None
#             globals()[k[:-1]] = v
#
#
# if __name__ == '__main__':
#     print(java, python, rust, javas, pythons, s)
#     fn()
#     print(java, python, rust, javas, pythons, s)
