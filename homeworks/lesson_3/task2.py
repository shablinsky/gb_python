# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_data(name, surname, birth_year, town, email, phone_number):
    print(f'Имя: {name}, Фамилия:{surname}, Год рождения:{birth_year}, Город:{town}, Почта:{email}, Номер телефона: {phone_number}')


n = input('введите имя: ')
s = input("введите фамилию: ")
b = input("введите год рождения: ")
t = input("введите город проживания: ")
e = input("введите email: ")
p = input("введите номер телфона: ")
user_data(name=n, surname=s, birth_year=b, town=t, email=e, phone_number=p)

