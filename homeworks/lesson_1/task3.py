# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.
print('Этот скрипт занимается вычеслениями по ТЗ')
str_n = input('Введите число: ')
str_nn = str_n * 2
str_nnn = str_n * 3
n_int = int(str_n)
nn_int = int(str_nn)
nnn_int = int(str_nnn)
result = n_int + nn_int + nnn_int
print('Ваш ответ:', result)
print('Конец скрипта.')
