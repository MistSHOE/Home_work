# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния
# (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# (Для ожидания нескольких секунд можно использовать метод стандартной библиотеки time.sleep())

import time


# class TrafficLight:
#     times = [7, 2, 5]
#     colors = ["red", "yellow", "green"]
#
#     def change_light(self, new_light):
#         if new_light in self.colors:
#             self.state = new_light
#         else:
#             print("Bad color")
#
#     def show_light(self):
#         print(self.state)
#
#     def rotate_lights(self):
#         while True:
#             for color, timeout in zip(self.colors, self.times):
#                 self.change_light(color)
#                 self.show_light()
#                 time.sleep(timeout)

#
# trafficLight = TrafficLight()
# trafficLight.rotate_lights()

class TrafficLight:
    times = [7, 2, 5]
    colors = ["red", "yellow", "green"]

    def rotate_lights(self):

        while True:

            for color, timeout in zip(self.colors, self.times):

                time.sleep(timeout)
                print(color)


trafficLight = TrafficLight()
trafficLight.rotate_lights()