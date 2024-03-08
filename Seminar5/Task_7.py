# Задание:
# Создайте функцию-генератор.
# Функция генерирует N простых чисел, начиная с числа 2.
# Для проверки числа на простоту используйте правило: «число является простым, если делится
# нацело только на единицу и на себя».


def is_simple(num: int) -> bool:
	if num < 2:
		return False
	for i in range(2, int(num ** 0.5) + 1):
		if num % i == 0:
			return False
	return True


def simple_generate(number: int):
	i = 2
	yield i
	i += 1
	while i <= number:
		if is_simple(i):
			yield i
		i += 2


a = simple_generate(27)
# for _ in range(27):
# 	print(next(a, "Число не простое!"), end=' ')

# если используется yield, вместо return
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a, None))
print(next(a, None))
print(next(a, None))
print(next(a, None))
print(next(a, None))

# def generate_primes(n):
# 	primes = []
# 	num = 2
# 	while len(primes) < n:
# 		is_prime = True
# 		for i in range(2, int(num ** 0.5) + 1):
# 			if num % i == 0:
# 				is_prime = False
# 				break
# 		if is_prime:
# 			primes.append(num)
# 		num += 1
# 	return primes
#
#
# test = generate_primes(10)
# print(test)
