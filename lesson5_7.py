# 7. Создать (не программно) текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
from json import dump

key = {}
count = 0
average = 0
with open("text_5_7", "r", encoding="utf-8") as file:
    lines = file.read().splitlines()
    for line in lines:
        firm_list = line.split()
        name_firm = firm_list[0]
        salary_firm = int(firm_list[2])
        loss_firm = int(firm_list[3])
        sum_salary_firm = salary_firm - loss_firm
        key[name_firm] = sum_salary_firm
    for value in key.values():
        if value < 0:
            continue
        else:
            count += 1
            average += value
    average /= count
    print(average)

final = [key, {}]
final[1]["average_profit"] = average
print(final)

with open("test_5_7", "w")as file:
    dump(final, file)

# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
