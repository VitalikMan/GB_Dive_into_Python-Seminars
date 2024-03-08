# Задание:
# Создайте вручную список с повторяющимися элементами.
# Удалите из него все элементы, которые встречаются дважды.

my_list = [1, 2, 2, 3, 43, 7, 7, 1, 8, 1]
# print(set(my_list))

for i in set(my_list):
    counter = my_list.count(i)
    if counter > 1:
        for _ in range(counter):
            my_list.remove(i)

print(my_list)
