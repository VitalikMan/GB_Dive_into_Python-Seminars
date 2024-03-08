# Задача:
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
# Под "успешной расстановкой ферзей" в данном контексте подразумевается такая расстановка ферзей
# на шахматной доске, в которой ни один ферзь не бьет другого.
# Другими словами, ферзи размещены таким образом, что они не находятся
# на одной вертикали,горизонтали или диагонали.
# Список из 4-х комбинаций координат сохраните в board_list.
# Дополнительно печатать его не надо.
# Пример использования:
# На входе:
# print(generate_boards())
# На выходе:
# [[(1, 4), (2, 7), (3, 1), (4, 8), (5, 5), (6, 2), (7, 6), (8, 3)],
#  [(1, 5), (2, 3), (3, 8), (4, 4), (5, 7), (6, 1), (7, 6), (8, 2)],
#  [(1, 3), (2, 6), (3, 8), (4, 2), (5, 4), (6, 1), (7, 7), (8, 5)],
#  [(1, 6), (2, 1), (3, 5), (4, 2), (5, 8), (6, 3), (7, 7), (8, 4)]]
#


from random import randint


def generate_board():
	board = []

	for i in range(1, 8 + 1):
		queen = (i, randint(1, 8))
		board.append(queen)
	return board


def generate_boards():
	count = 0
	board_list = []
	while count < 4:
		board = generate_board()
		if check_queens(board):
			count += 1
			board_list.append(board)
	return board_list


def is_attacking(q1, q2):
	if q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1]):
		return True
	return False


def check_queens(queens: list):
	for i in range(len(queens)):
		for j in range(i + 1, len(queens)):
			if is_attacking(queens[i], queens[j]):
				return False
	return True


print(generate_boards())
