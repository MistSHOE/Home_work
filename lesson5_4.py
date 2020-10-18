# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

translations = {"one": "один", "two": "два", "three": "три", "four": "четыре"}

with open('text_5_4', 'r', encoding="utf-8") as file:
    for line in file:
        line_split = line.strip().split("-")
        print(line)
        for i in translations:
            i = translations.values()


print(type(translations))


# count_personal = 0
# total = 0
# name_staff = []
# with open('text_5_3', 'r', encoding="utf-8") as file:
#     my_text = list(line.strip('\n') for line in file)
#
#     for i in my_text:
#         name, salary = i.strip().split()
#         count_personal += 1
#         total += int(salary)
#         if int(salary) < 20000:
#             name_staff += (name,)
#
#
# total = total / count_personal
# print(name_staff)
# print(total)



# file = open('text_5_3', encoding="utf-8")
#
# count_line = 0
# for lines in file:
#     count_line += 1
#     check = 0
#     word = 0
#     for symbol in lines:
#         if symbol != ' ' and check == 0:
#             word += 1
#             check = 1
#         elif symbol == ' ':
#             check = 0
#     print(f"{lines} символов: {len(lines)}  кол-во слов: {word} строка №: {count_line}")
#     print(type(lines))
# print(f"Всего {count_line} строк.")
# file.close()


# file_name = input("Введите название файла: ")
# file = open(file_name, 'a+')
# print(" В файле " + str(len(file.read())) + " символов ")
#
# strings = file.readlines()
# print("напечатал строку: " + strings)
# file.close()
# file = open("text.txt", "r", encoding="utf-8")
# # цыкл для принта каждой строки
# enemy_line = 0
# word = []
# for line_text in file:
#     # print(line_text)
#     word.append( line_text.split())
#     # print(word)
#
#     # print(line_text.split())
#     enemy_line += 1
#     # print(type(line_text))
# print(f'Кол-во строк в вашем файле: {enemy_line}')
#     # цыкл для принта каждого символа
#     # for symbol in line_text:
#         # print(symbol)
#
# print(word)
# print(type(word))
# count_word = 0
# for list_word in word:
#     print(list_word)
#     for enemy_word in list_word:
#         count_word += 1
#         # print(enemy_word)
#         print(count_word)
#