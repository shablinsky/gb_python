# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
# полученной ранее сумме и после этого завершить программу.
def sum_elements_in_list(nums_str, stop):
    nums_list = nums_str.split(' ')
    sum_list = 0
    for i in nums_list:
        if i == stop:
            break
        sum_list = sum_list + int(i)
    return sum_list


stop_phrase = 'zzz'
finish = False
sum_symbols = 0
while not finish:
    user_phrase = input('Введите ваше сообщение: ')
    sum_symbols = sum_symbols + sum_elements_in_list(user_phrase, stop_phrase)
    finish = stop_phrase in user_phrase
    print(f'последнее сообщение: {user_phrase}, сумма: {sum_symbols}')

