# Задача:
# На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
# Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

frac1 = "1/2"
frac2 = "1/3"

# Вычисление суммы дробей
numerator_frac1, denominator_frac1 = map(int, frac1.split("/"))
numerator_frac2, denominator_frac2 = map(int, frac2.split("/"))

if denominator_frac1 != denominator_frac2:
    Sum_of_fractions = (f"{(numerator_frac1 * denominator_frac2 + numerator_frac2 * denominator_frac1)}/"
                        f"{denominator_frac1 * denominator_frac2}")
else:
    Sum_of_fractions = f"{numerator_frac1 + numerator_frac2}/{(denominator_frac1 or denominator_frac2)}"

print(f"Сумма дробей: {Sum_of_fractions}")

# Вычисление произведения дробей
product_of_fractions = f"{numerator_frac1 * numerator_frac2}/{denominator_frac1 * denominator_frac2}"
print(f"Произведение дробей: {product_of_fractions}")

# Проверка
print("\nПроверка: ")
def sum_and_product(a, b):
    # Преобразование строк в объекты дробей
    fraction1 = Fraction(a)
    fraction2 = Fraction(b)

    # Сумма дробей
    summa_result = fraction1 + fraction2

    # Произведение дробей
    product_of_fractions = fraction1 * fraction2

    return summa_result, product_of_fractions

# Входные строки с дробями
a = frac1
b = frac2

# Вызов функции и получение результата
summa_result, product_of_fractions = sum_and_product(a, b)

# Вывод результата
print("Сумма дробей:", summa_result)
print("Произведение дробей:", product_of_fractions)
