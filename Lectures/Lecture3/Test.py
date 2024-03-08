# arr = [2, 6, 8, 10, 12, 14, 16, 18]
#
# print(arr[2:6:2])
# print(arr.pop())
# print(arr.extend([314, 42]))
# print(arr)
# print(arr.sort(reverse=False))
# print(arr)

# my_set = frozenset({1, 2, 3, 4, 5, 6, 7})
# # my_set2 = {11, 12, 1, 3}
# #
# # new_set = my_set | my_set2
# # # print(new_set)
# #
# # # my_set.discard(8)
# # print(len(new_set))


text_eng = "Hello world!"
res = text_eng.encode("utf-8")
print(f'На английском: \n{res}, {type(res)}')
print(f'На английском: \n{res[:]}, {type(res)}')

text_ru = "Привет мир!"
res = text_ru.encode("utf-8")
print(f'На русском: \n{res}, {type(res)}')
print(f'На русском: \n{res[1::2]}, {type(res)}')

