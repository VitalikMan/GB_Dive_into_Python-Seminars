# Задание:
# На выбор ОДНО ИЗ ДВУХ ЗАДАНИЙ:
# 1. Взять класс студент из дз 12-го семинара,
# 	добавить запуск из командной строки(передача в качестве аргумента название csv-файла с предметами),
# 	логирование и написать 3-5 тестов с использованием pytest.
# 2. Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# 	Соберите информацию о содержимом в виде объектов namedtuple.
# 	Каждый объект хранит:
# 		имя файла без расширения или название каталога,
# 		расширение, если это файл,
# 		флаг каталога,
# 		название родительского каталога.
# 	Написать 3-5 тестов к задаче.
#
# Сдавать дз ссылкой на репозиторий GitHub(проверьте что он не приватный перед отправкой).
# 1. Взять класс студент из дз 12-го семинара,
# добавить запуск из командной строки(передача в качестве аргумента название csv-файла с предметами),
# логирование и написать 3-5 тестов с использованием pytest.

import csv
import logging
import pytest

# Настройка логирования
logging.basicConfig(filename='student.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class Student:
	"""
	Класс, представляющий студента.

	Атрибуты:
	- name (str): ФИО студента
	- subjects (dict): словарь, содержащий предметы и их оценки и результаты тестов

	Методы:
	- __init__(self, name, subjects_file): конструктор класса
	- __setattr__(self, name, value): дескриптор, проверяющий ФИО на первую заглавную букву и наличие только букв
	- __getattr__(self, name): получение значения атрибута
	- __str__(self): возвращает строковое представление студента
	- load_subjects(self, subjects_file): загрузка предметов из файла CSV
	- get_average_test_score(self, subject): возвращает средний балл по тестам для заданного предмета
	- get_average_grade(self): возвращает средний балл по всем предметам
	- add_grade(self, subject, grade): добавление оценки по предмету
	- add_test_score(self, subject, test_score): добавление результата теста по предмету
	"""

	def __init__(self, name, subjects_file):
		self.name = name
		self.subjects = {}
		self.load_subjects(subjects_file)

	def __setattr__(self, name, value):
		if name == 'name':
			if not value.replace(' ', '').isalpha() or not value.istitle():
				raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
		super().__setattr__(name, value)

	def __getattr__(self, name):
		if name in self.subjects:
			return self.subjects[name]
		else:
			raise AttributeError(f"Предмет {name} не найден")

	def __str__(self):
		return f"Студент: {self.name}\nПредметы: {', '.join(self.subjects.keys())}"

	def load_subjects(self, subjects_file):
		with open(subjects_file, 'r', encoding='utf=8') as f:
			reader = csv.reader(f)
			for row in reader:
				subject = row[0]
				if subject not in self.subjects:
					self.subjects[subject] = {'grades': [], 'test_scores': []}

	def add_grade(self, subject, grade):
		if subject not in self.subjects:
			self.subjects[subject] = {'grades': [], 'test_scores': []}
		if not isinstance(grade, int) or grade < 2 or grade > 5:
			raise ValueError("Оценка должна быть целым числом от 2 до 5")
		self.subjects[subject]['grades'].append(grade)

	def add_test_score(self, subject, test_score):
		if subject not in self.subjects:
			self.subjects[subject] = {'grades': [], 'test_scores': []}
		if not isinstance(test_score, int) or test_score < 0 or test_score > 100:
			raise ValueError("Результат теста должен быть целым числом от 0 до 100")
		self.subjects[subject]['test_scores'].append(test_score)

	def get_average_test_score(self, subject):
		if subject not in self.subjects:
			raise ValueError(f"Предмет {subject} не найден")
		test_scores = self.subjects[subject]['test_scores']
		if len(test_scores) == 0:
			return 0
		return sum(test_scores) / len(test_scores)

	def get_average_grade(self):
		total_grades = []
		for subject in self.subjects:
			grades = self.subjects[subject]['grades']
			if len(grades) > 0:
				total_grades.extend(grades)
		if len(total_grades) == 0:
			return 0
		return sum(total_grades) / len(total_grades)


# Тесты
@pytest.fixture
def student():
	return Student('Иван Иванов', 'subjects.csv')


def test_init(student):
	assert student.name == 'Иван Иванов'
	assert student.subjects == {'математика': {'grades': [], 'test_scores': []},
								'русский язык': {'grades': [], 'test_scores': []},
								'английский язык': {'grades': [], 'test_scores': []},
								'физика': {'grades': [], 'test_scores': []}}


def test_setattr_name_valid(student):
	student.name = 'Петр Петров'
	assert student.name == 'Петр Петров'


def test_setattr_name_invalid(student):
	with pytest.raises(ValueError):
		student.name = '123'


def test_getattr_valid(student):
	assert student.математика == {'grades': [], 'test_scores': []}


def test_getattr_invalid(student):
	with pytest.raises(AttributeError):
		var = student.химия


def test_str(student):
	assert str(student) == "Студент: Иван Иванов\nПредметы: математика, русский язык, английский язык, физика"


def test_add_grade(student):
	student.add_grade('математика', 4)
	assert student.математика['grades'] == [4]


def test_add_grade_invalid_value(student):
	with pytest.raises(ValueError):
		student.add_grade('математика', 1)


def test_add_test_score(student):
	student.add_test_score('математика', 85)
	assert student.математика['test_scores'] == [85]


def test_add_test_score_invalid_value(student):
	with pytest.raises(ValueError):
		student.add_test_score('математика', 105)


def test_get_average_test_score(student):
	student.add_test_score('математика', 85)
	student.add_test_score('математика', 90)
	assert student.get_average_test_score('математика') == 87.5


def test_get_average_grade(student):
	student.add_grade('математика', 4)
	student.add_grade('математика', 5)
	student.add_grade('русский язык', 3)
	student.add_grade('русский язык', 4)
	assert student.get_average_grade() == 4.0


# Запуск из командной строки
if __name__ == '__main__':
	import sys

	if len(sys.argv) != 2:
		print("Использование: python student.py subjects.csv")
		exit(1)

	subjects_file = sys.argv[1]
	student = Student('Иван Иванов', subjects_file)
	print(student)
