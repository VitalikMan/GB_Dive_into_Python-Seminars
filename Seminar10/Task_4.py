# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть шестизначный идентификационный номер и уровень доступа
# (остаток от суммы цифр id делённой на семь)
from Task_3 import Person


# Version 1
# class Employee(Person):
# 	def __init__(self, name: str, surname: str, age: int, emp_id: int = 1):
# 		if len(str(emp_id)) != 6:
# 			raise ValueError("Некорректный идентификационный номер")
# 		self.emp_id = emp_id
# 		self.level = sum(map(int, str(emp_id))) % 7
#
# 		super().__init__(name, surname, age)
#
#
# if __name__ == '__main__':
# 	e = Employee("Александр", "Пушкин", 19, 123321)
# 	print(f"{e.emp_id=}, {e.level=}")


# Version 2
class Employee(Person):
	def __init__(self, emp_id: int = 1, *args, **kwargs):
		if len(str(emp_id)) != 6:
			raise ValueError('Некорректный идентификационный номер')
		self.emp_id = emp_id
		self.level = sum(map(int, str(emp_id))) % 7

		super().__init__(*args, **kwargs)


if __name__ == '__main__':
	e = Employee(123321, 'Александр', 'Пушкин', 19)
	print(f'{e.emp_id=}, {e.level=}')
