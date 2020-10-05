# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def data_user(name, **information):
    print(f"Name: {name}")
    for x, y in information.items():
        print(f"{x}: {y}")


data_user("Tao", surname="Bloody", phone="8-999-999-99-99", email="123456789@mail.com", city="Moscow", years="25")


def information(name, **data):
    print(f"Name: {name}, {data}")


information("Mistrun", surname="Bloody", phone="8-999-999-99-99",
