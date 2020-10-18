# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

key_data = {}
with open("text_5_6", "r", encoding="utf-8") as file:
    data = file.read().splitlines()
    # print(data)
    for i in data:
        key_value = i.split(": ")
        result = key_value[1].split(" ")
        sum_line = 0
        # print(result)
        for x in result:
            # print(x)

            if x == "—":
                continue
            else:
                number = x.split("(")[0]
                sum_line += int(number)
        key_data[key_value[0]] = sum_line
    print(key_data)




    # file.seek(0)
    # data = file.readlines()
    # print(data)
