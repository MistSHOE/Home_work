# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк,
# количества слов в каждой строке.

file = open('text_5_2', encoding="utf-8")

count_line = 0
for lines in file:
    count_line += 1
    check = 0
    word = 0
    for symbol in lines:
        if symbol != ' ' and check == 0:
            word += 1
            check = 1
        elif symbol == ' ':
            check = 0
    print(f"{lines} символов: {len(lines)}  кол-во слов: {word} строка №: {count_line}")
print(f"Всего {count_line} строк.")
file.close()