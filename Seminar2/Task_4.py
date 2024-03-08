# Задание:
# - Напишите программу, которая решает квадратные уравнения даже если
# дискриминант отрицательный.
# - Используйте комплексные числа для извлечения квадратного корня.
import cmath

a = -1  # float(input('>>> '))
b = 3  # float(input('>>> '))
c = 0  # float(input('>>> '))

discriminant = b**2 - 4*a*c

print('Дискриминант = ' + str(discriminant))

if discriminant < 0:
    real_path = x = -b / (2 * a)
    image_path = cmath.sqrt(-discriminant / (2 * a))
    x1 = complex(real_path, image_path)
    x2 = complex(real_path, -image_path)
    print('x1 = ' + str(x1))
    print('x2 = ' + str(x2))

elif discriminant == 0:
    x = -b / (2 * a)
    print('x = ' + str(x))
else:
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    print('x1 = ' + str(x1))
    print('x2 = ' + str(x2))
