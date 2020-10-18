# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open("text_5_5", "w") as file:
    list_number = [1, 2, 3, 4, 5]
    for i in range(len(list_number)):
        list_number[i] = str(list_number[i])
    line = " ".join(list_number)

    file.write(line)

with open("text_5_5", "r") as file:
    line = file.read()
    list_number = line.split(" ")
    for i in range(len(list_number)):
        list_number[i] = int(list_number[i])
    sum_number = sum(list_number)
    print(sum_number)



