# Задача:
# Напишите функцию группового переименования файлов в папке test_folder под названием rename_files.
# Она должна:
# a) Принимать параметр желаемое конечное имя файлов.
# 	 При переименовании в конце имени добавляется порядковый номер.
# b) Принимать параметр количество цифр в порядковом номере.
# c) Принимать параметр расширение исходного файла.
# 	 Переименование должно работать только для этих файлов внутри каталога.
# d) Принимать параметр расширение конечного файла.
# e) Принимать диапазон сохраняемого оригинального имени.
# 	 Например, для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# 	 К ним прибавляется желаемое конечное имя, если оно передано.
# 	 Далее счётчик файлов и расширение.
# f) Папка test_folder доступна из текущей директории
#
# Пример использования:
# На входе:
# rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")
# На выходе:
# new_file_008.doc, test.doc, new_file_004.doc, new_file_005.doc,\
# new_file_007.doc, new_file_001.doc, new_file_006.doc, new_file_003.doc,\
# new_file_002.doc, new_file_009.doc, new_file_010.doc
import os

# def rename_files(desired_name: str, num_digits: int, source_ext: str,
# 				 target_ext: str):
# 	# directory = "test_folder"
# 	directory = os.getcwd() + "/test_folder"
# 	list_dir = os.listdir(directory)
# 	for i, file in enumerate(list_dir):
# 		if file.endswith('.' + source_ext):
# 			file_name = os.path.splitext(file)[0]
# 			file_extension = '.' + os.path.splitext(file)[1]
# 			new_file_name = desired_name + f'{i + 1:0>{num_digits}}' + '.' + target_ext
# 			os.rename(os.path.join(directory, file), os.path.join(directory, new_file_name))
# 	print("Переименование файлов в папке test_folder успешно выполнено")
# 	print(os.listdir(directory))


directory = ['dafsdasdas.txt', 'asdsaa.txt', 'asdadsa.txt', 'khksa.txt', 'test.doc']


def rename_files(desired_name: str, num_digits: int, source_ext: str,
				 target_ext: str):
	for i, file in enumerate(directory):  # list_dir = os.listdir(directory)
		if file.endswith('.' + source_ext):
			# file_name = os.path.splitext(file)[0]
			# file_extension = '.' + os.path.splitext(file)[1]
			new_file_name = desired_name + f'{i + 1:0>{num_digits}}' + '.' + target_ext
			# os.rename(os.path.join(directory, file), os.path.join(directory, new_file_name))
			directory[i] = new_file_name
	return directory


print(rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc"))

# rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")
