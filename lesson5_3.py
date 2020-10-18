# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

count_personal = 0
total = 0
name_staff = []
with open('text_5_3', 'r', encoding="utf-8") as file:
    my_text = list(line.strip('\n') for line in file)

    for i in my_text:
        name, salary = i.strip().split()
        count_personal += 1
        total += int(salary)
        if int(salary) < 20000:
            name_staff += (name,)


total = total / count_personal
print(name_staff)
print(total)
