# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month = input('Введите цифрами месяц:' )
# dict method
season_year_dict = {
'12': "winter", '1': "winter", '2': "winter",
'3': "spring", '4': "spring", '5': "spring",
'6': "summer", '7': "summer", '8': "summer",
'9': "fall", '10': "fall", '11': "fall"
}
print(f'result_dict_method: {season_year_dict[month]}')

# list_method
season_year_list = ["winter", "winter", "spring", "spring", "spring", "summer",
                    "summer", "summer", "fall", "fall", "fall", "winter"]
print(f'result_list_method: {season_year_list[int(month) - 1]}')


