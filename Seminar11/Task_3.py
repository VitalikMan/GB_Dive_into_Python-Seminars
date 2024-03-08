# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста и для пользователя.

class Data_:
	_instance = None

	def __new__(cls, text, name):

		if cls._instance is None:
			cls._instance = super().__new__(cls)
			cls._instance.all_text = []
			cls._instance.all_name = []
		else:
			cls._instance.all_text.append(cls._instance.text)
			cls._instance.all_name.append(cls._instance.name)
		return cls._instance

	def __init__(self, text: str, name: str):
		self.text = text
		self.name = name

	def __str__(self):
		return f'{self.text} - {self.name}'

	def __repr__(self):
		return f'Data_({self.text=} - {self.name=})'


if __name__ == '__main__':
	c = Data_('Hello', 'Jo')
	print(c)
	print(repr(c))
