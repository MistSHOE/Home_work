# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

name_file = input("Введите название файла: ")
create_file = open(name_file, 'a+', encoding="utf-8")

info_for_file = input("Ввод информации для файла: ")

while create_file.write(info_for_file + "," + "\n"):
    info_for_file = input("Ввод информации для файла: ")
    if info_for_file == '':
        break
print("Вы вышли из записи")

create_file.close()