# Задача:
# Пользователь вводит данные.
# Сделайте проверку данных и преобразуйте, если возможно в один из вариантов ниже:
# - целое положительное число
# - вещественное положительное или отрицательное число
# - строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
# - строку в верхнем регистре в остальных случаях

data = "5.1."
if data.isdigit():
    print("int")
elif ('.' in data
      and data.replace('-', '').replace('.', '', 1).isdigit()
      and '-' not in data[1:]):
    print('float')
elif data.lower() != data:
    print(data.lower())
else:
    print(data.upper())
