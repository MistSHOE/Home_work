# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def function_division():
    number_1 = int(input("enter number one: "))
    number_2 = int(input("enter number two: "))
    # number_1 = 10
    # number_2 = 5
    try:
        result = number_1 / number_2
        print(result)
    except ZeroDivisionError:
        print("Деление на 0 невозможно")
        result = 0
        print(result)
        
function_division()