# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь, от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

MAIN_CONDITION = 4
ADD_CONDITION = 100
YEAR_EXCEPTION = 400
year = int(input("Введите год: "))

if (year % MAIN_CONDITION == 0 and year % ADD_CONDITION != 0
        or year % YEAR_EXCEPTION == 0):
    result = "Високосный год"
else:
    result = "Не високосный год"

print(result)
