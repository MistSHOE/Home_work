# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

name = "Tao"
data_human = dict(
    name="Tao",
    years="20",
    city="Moscow",
    email="Tao@mail.ru",
    phone="8-999-999-99-99")

print(*data_human)
print(data_human.items())
print(data_human.values())
print(data_human.keys())
print(data_human.get("name"))


# def information_collection(data_human):
#     for data in data_human.items():
#         print(f"{data}")
#     print()
#
#
# information_collection(data_human)

