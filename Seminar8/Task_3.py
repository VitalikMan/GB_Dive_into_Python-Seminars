# Задача:
# Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
import csv
import json


def save_to_csv(json_in: str, csv_out: str) -> None:
	with(
		open(json_in, 'r', newline='', encoding='utf-8') as f_in,
		open(csv_out, 'w', newline='', encoding='utf-8') as f_out,
	):
		data = json.load(f_in)
		# print(data)
		all_data = []
		csv_write = csv.DictWriter(f_out, fieldnames=['level', 'id', 'name'])
		for level, inner_dict in data.items():
			for id_, name in inner_dict.items():
				all_data.append({"id": id_, "level": level, "name": name})
		csv_write.writeheader()
		csv_write.writerows(all_data)


if __name__ == '__main__':
	save_to_csv('users.json', 'users.csv')
