# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def function_max_number(a, b, c):
    # a = int(input("enter one number: "))
    # b = int(input("enter two number: "))
    # c = int(input("enter three number: "))
    result = [a, b, c]
    print(max(result))
    return max(a, b, c)


function_max_number(100, 20, 5)