# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

enter_user = 0
enter_number = []

while True:

    enter_number = input("Enter number by spaces : ").split()
    print(enter_number)
    enter_number = list(enter_number)

    if enter_number == ["q"]:
        print("Yours exit")
        break
    else:
        for x in enter_number:
            enter_user += int(x)
            print(f"sum yours numbers: {enter_user}")