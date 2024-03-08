from decimal import Decimal, ROUND_DOWN

MULTIPLICITY = 50
MIN_REMOVAL = 0.01
MAX_REMOVAL = 0.1
RICHNESS_SUM = 1000000
RICHNESS_PERCENT = 0.001

balance = Decimal(0)
operations = []


def check_multiplicity(amount):
	if amount % MULTIPLICITY != 0:
		operations.append(f"Сумма должна быть кратной {MULTIPLICITY} у.е.")
		return False
	return True


def deposit(amount):
	if check_multiplicity(amount):
		global balance
		balance += Decimal(amount)
		operations.append(f"Пополнение карты на {amount} у.е. Итого {balance} у.е.")


def withdraw(amount):
	if check_multiplicity(amount):
		global balance
		if amount > balance:
			operations.append(
				f"Недостаточно средств. Сумма с комиссией {amount + amount * MAX_REMOVAL:.3f} у.е. На карте {balance} у.е.")
		else:
			commission = amount * MIN_REMOVAL
			balance -= amount + commission
			operations.append(
				f"Снятие с карты {amount} у.е. Процент за снятие {commission:.3f} у.е.. Итого {balance} у.е.")


def exit():
	global balance
	if balance > RICHNESS_SUM:
		tax = balance * RICHNESS_PERCENT
		balance -= tax
		operations.append(
			f"Вычтен налог на богатство {RICHNESS_PERCENT:.1%} в сумме {tax:.4f} у.е. Итого {balance:.4f} у.е.")
	operations.append(f"Возьмите карту на которой {balance:.4f} у.е.")


# Пример использования функций
deposit(10000)
withdraw(4000)
exit()
print(operations)
