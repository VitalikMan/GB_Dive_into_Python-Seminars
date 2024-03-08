# Задача:
# Напишите функцию для транспонирования матрицы transposed_matrix,
# принимает в аргументы matrix, и возвращает транспонированную матрицу.

matrix = [[1, 2, 3],
		  [4, 5, 6],
		  [7, 8, 9]]


def transpose(matrix):
	return [list(i) for i in zip(*matrix)]


transposed_matrix = transpose(matrix)

print(transposed_matrix)
