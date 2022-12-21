 # Программа запрашивает у пользователя строку чисел, разделённых пробелом.
 # При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
 # Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
 # Но если вместо числа вводится специальный символ, выполнение программы завершается.
 # Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу

def func_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введите число или Х для выхода: ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == 'х' or number[el] == 'Х':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Сумма: {sum_res}')
    print(f'Итоговая сумма: {sum_res}')

print(func_sum())