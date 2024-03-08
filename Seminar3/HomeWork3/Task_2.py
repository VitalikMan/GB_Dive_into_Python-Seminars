# Задача:
# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# Слова разделяются пробелами.
# Такие слова как don t, it s, did n t и т.д. (после того, как убрали знак препинания апостроф) считать двумя словами.
# Цифры за слова не считаем.
# Отсортируйте по убыванию значения количества повторяющихся слов.
# Пример:
# На входе:
# text = 'Hello world. Hello Python. Hello again.'
# На выходе:
# [('hello', 3), ('world', 1), ('python', 1), ('again', 1)]
import string
from collections import Counter

delimiter_chars = set(string.punctuation.replace(" ", ""))  # генерируем список разделительных символов без пробела

text = "The quick brown fox jumps over the lazy dog. Lazy dog, lazy fox!"
text = text.lower()     # преобразуем всю строку к нижнему регистру
word_list = text.split()    # разделяем строку на список слов

text_without_characters = []
for word in word_list:
    if not any(char.isdigit() for char in word):    # проверяем, есть ли цифра в слове
        text_without_characters.append(word)        # если цифры нет в слове, то добавляем его в список

new_text = ' '.join(text_without_characters)   # объединяем слова обратно в строку с пробелами

for char in delimiter_chars:
    new_text = new_text.replace(char, " ")    # удаляем все разделительные символы

new_word_list = new_text.split()   # разделяем все слова и создаем из них список

number_of_each_word = Counter(new_word_list)     # подсчитываем количество каждого слова в списке
result = list(number_of_each_word.items())      # преобразования в список кортежей с помощью метода items()
# Сортировка по убыванию значения количества повторяющихся слов
result = sorted(result, key=lambda x: x[1], reverse=True)
print(result)
