# Задание:
# Напишите программу банкомат.
# - Начальная сумма равна нулю
# - Допустимые действия: пополнить, снять, выйти
# - Сумма пополнения и снятия кратны 50 у.е.
# - Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# - После каждой третей операции пополнения или снятия начисляются проценты - 3%
# - Нельзя снять больше, чем на счёте
# - При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# - Любое действие выводит сумму денег


class Bank:
    def __init__(self):
        self.balance = 0
        self.index = 0

    def deposit(self, money):
        self.__rich_comission()
        self.__print_balance()
        if money < 50:
            print("Сумма пополнения кратная 50 у.е.")
        else:
            self.balance += money
            self.__procents()

    def cash_withdrawal(self, money):
        self.__print_balance()
        self.__rich_comission()
        if money % 50:
            print("Сумма снятия кратная 50 у.е.")
            return
        if money + self.__comission(money) > self.balance:
            print("Операция не возможна")
        else:
            self.balance -= money
            self.__procents()

    def __procents(self):
        self.index += 1
        if self.index % 3 == 0:
            self.balance *= 1.03

    def __comission(self, money):
        com = money * 0.0015
        if com < 30:
            return 30
        if com > 600:
            return 600
        return com

    def __rich_comission(self):
        if self.balance > 5_000_000:
            self.balance *= 0.9

    def __print_balance(self):
        print(self.balance)


bank = Bank()
print(bank.balance)
bank.deposit(100000000000)
print(bank.balance)
bank.cash_withdrawal(30)
print(bank.balance)
bank.cash_withdrawal(50)
print(bank.balance)
