# Задача:
# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
# Пример использования:
# На входе:
# file_path = "C:/Users/User/Documents/example.txt"
# На выходе:
# ('C:/Users/User/Documents/', 'example', '.txt')
import os


def get_file_info(file_path):
	dir_path, file_name = os.path.split(file_path)
	file_name, file_ext = os.path.splitext(file_name)
	return (dir_path + '/' if dir_path else '', file_name, file_ext)


file_path = 'file_in_current_directory.txt'
# file_path = "C:/Users/User/Documents/example.txt"

print(get_file_info(file_path))
