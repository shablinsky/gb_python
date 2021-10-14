# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

name = input('Введите имя: ')
age = int(input('Введите свой возраст: '))
adult = age > 18

my_first_tuple = (name, age, adult)
my_first_dict = {'a': name, 'b': age, 'c': adult}
my_first_list = [name, age, adult, my_first_dict, my_first_tuple]

for i in my_first_list:
    print(type(i))