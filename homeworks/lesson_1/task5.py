# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек,
# или убыток — издержки больше выручки. Выведите соответствующее сообщение.
#
# Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке. Далее запросите численность сотрудников фирмы
# и определите прибыль фирмы в расчёте на одного сотрудника.
print('Проверь свой бизнес.')
plus_cash = float(input('Напиши сколько выручки: '))
minus_cash = float(input('Напиши сколько издержек: '))
if plus_cash > minus_cash:
    print('Бизнес прибыльный. Выручка больше издержек.')
    ros = (plus_cash / minus_cash) * 100
    print('Рендаблиность на уровне: ', "{:.2f}".format(ros), '%')
    clear_profit = plus_cash - minus_cash
    print('Чистая прибыль: ', "{:.2f}".format(clear_profit))
    employees = int(input('Сколько работников?: '))
    salary = clear_profit / employees
    print('Зарплата одному работнику : ', "{:.2f}".format(salary))
else:
    print('Бизнес убыточен, издержек больше чем выручки')
    print('Нужно что-то менять')
print('Оценка бизнеса выполнена, скрипт завершен')
