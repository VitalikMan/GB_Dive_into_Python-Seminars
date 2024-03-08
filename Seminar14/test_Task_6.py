# Задача 6:
from rectrangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
	def setUp(self):
		self.r1 = Rectangle(4, 8)
		self.r2 = Rectangle(2, 4)

	def test_init_rectangle(self):
		self.assertIsNotNone(self.r1)

	def test_init_rectangle_incorrect(self):
		with self.assertRaises(ValueError):
			Rectangle(-4, 8)

	def test_is_area_int(self):
		self.assertIsInstance(self.r1.area(), int)

	def test_add_is_rectangle(self):
		self.assertIsInstance(self.r1 + self.r2, Rectangle)
