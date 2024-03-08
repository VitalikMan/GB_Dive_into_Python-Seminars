# Задача:
# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# - Строки нумеруются начиная с единицы.
# - Слова выводятся отсортированными согласна кодировки Unicode.
# - Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.

text_user = "Пользователь вводит строку текста. Вывести каждое слово с новой строки."
text = text_user.split(" ")
text.sort()
print(text)
max_word = max(text, key=len)

for i, word in enumerate(text, 1):
    print(f"{i:>2}| {word:>{len(max_word)}}")
