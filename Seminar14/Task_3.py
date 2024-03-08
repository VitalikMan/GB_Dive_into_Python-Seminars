# Задача 3:
# Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
from Task_2 import clear_text
import unittest


class TestClearText(unittest.TestCase):
	def test_no_changes(self):
		self.assertEqual(clear_text('hello world'), 'hell world', msg='Строка вернулась с изменениями')

	def test_register(self):
		self.assertEqual(clear_text('Hello world'), 'hello world')

	def test_delete_punctuation(self):
		self.assertEqual(clear_text('Hello world!'), 'hello world')

	def test_delete_foreign_alpha(self):
		self.assertEqual(clear_text('Hello мир'), 'hello ')

	def test_all(self):
		self.assertEqual(clear_text('Hello, world или мир!'), 'hello world  ')


if __name__ == '__main__':
	unittest.main(verbosity=4)
