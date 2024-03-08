# Задача:
# Вспоминаем задачу 3 из прошлого семинара.
# Мы сформировали текстовый файл с псевдоименами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.
import json


def txt_to_json(source, output):
	data1 = {}
	with open(source, 'r') as f:
		data = f.read()

	for line in data.split('\n'):
		if ' ' in line:
			name, number = line.split(' ')
			data1[name.capitalize()] = float(number)

	with open(output, 'w') as f:
		json.dump(data1, f, indent=4)


txt_to_json('data.txt', 'output.json')
