# Задание:
# Напишите функцию, которая принимает строку текста.
# Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.

def generate_code_list(text: str) -> list[int]:
    list_unicode = set()
    for char in text:
        list_unicode.add(ord(char))
    return sorted(list_unicode, reverse=True)

text_user = "Напишите функцию, которая принимает строку текста."

print(generate_code_list(text_user))
