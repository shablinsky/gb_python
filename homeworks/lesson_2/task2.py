# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

user_str = input("Введите набор слов, что бы создать список: ")
user_list = user_str.split()
list_len = len(user_list)
start = 0
if list_len > 1:
    while start < list_len - 1:
        user_list[start], user_list[start + 1] = user_list[start + 1], user_list[start]
        start = start + 2

print(user_list)