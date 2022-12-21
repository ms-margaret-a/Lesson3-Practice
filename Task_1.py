# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division_1(num_1, num_2):
    try:
        return num_1/num_2
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'

try:
    num_1 = int(input("введите первое число: "))
    num_2 = int(input("введите второе число: "))
    print(division_1(num_1,num_2))
except ValueError:
    print ("Допустимы только числа!")