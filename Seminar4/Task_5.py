# Задание:
# Функция принимает на вход три списка одинаковой длины:
# - имена str,
# - ставка int,
# - премия str с указанием процентов вида “10.25%”.
# Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии


def calculate_salary(lst1: list[str], lst2: list[int], lst3: list[str]) -> dict[str, float]:
    result = {}
    for name, salary, bonus in zip(lst1, lst2, lst3):
        result[name] = round(salary * float(bonus.replace("%", "")) / 100, 2)
    return result

if __name__ == "__main__":
    lst1 = ["Python", "Rust", "Java"]
    lst2 = [100, 137, 89]
    lst3 = ["10.4%", "10.0%", "12.5%"]
    print(calculate_salary(lst1, lst2, lst3))
