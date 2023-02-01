"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""

def calc_sum(res_sum = 0):
    numbers = input('Введите числа разделенные пробелом или нажмите "Q" для выхода из программы: ').split()
    for i in numbers:
        if i != "Q":
            res_sum = res_sum + int(i)
        else:
            break
    print(res_sum)
    if 'Q' in numbers:
        exit("Выход из программы")
    else:
        calc_sum(res_sum)

calc_sum()