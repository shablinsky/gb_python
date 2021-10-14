# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input('Введите целое положительное число: '))
max_number = 0
while number < 0:
    number = int(input('Целое положительное число - это любое цисло больше нуля, введите такое число: '))
while number > 0:
    if number % 10 > max_number:
        max_number = number % 10
        if max_number == 9:
            break
    number = number // 10
print(max_number)
