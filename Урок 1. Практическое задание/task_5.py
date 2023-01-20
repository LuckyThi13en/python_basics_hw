"""
Задание 5.

Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите
прибыль фирмы в расчете на одного сотрудника.

Пример:
Введите выручку фирмы: 1000
Введите издержки фирмы: 500
Финансовый результат - прибыль. Ее величина: 500
Значит вычисляем рентабельность выручки (соотношение прибыли к выручке)
Рентабельность выручки = 0.5
Введите численность сотрудников фирмы: 10
Прибыль фирмы в расчете на одного сотрудника = 50.0
"""
proc = int(input('Введите выручку фирмы:'))
costs = int(input('Введите издержки фирмы:'))
fin_result = proc - costs
if fin_result < 0:
    print('Финансовый результат - убыток. Ее величина:', fin_result)
else:
    print('Финансовый результат - прибыль. Ее величина:', fin_result)
    rent = costs / proc
    print('Рентабельность выручки =', rent)
    souls = int(input('Введите численность сотрудников фирмы:'))
    proc_per_soul = fin_result / souls
    print('Рентабельность выручки =', proc_per_soul)
