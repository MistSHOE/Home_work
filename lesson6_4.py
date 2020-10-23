# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

import random


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f"Машина: {self.name}, скорость: {self.speed} км/ч")

    def go_car(self):
        print(f"Машина поехала: {self.speed} км/ч")

    def stop_car(self):
        print(f"Машина остановилась: {self.speed - self.speed} км/ч")

    def turn_car(self):
        derection = random.randint(1, 4)

        if derection == 1:
            print(f"Машина едет прямо, скорость: {self.speed} км/ч")
        elif derection == 2:
            print(f"Машина едет назад, скорость: {self.speed/2} км/ч")
        elif derection == 3:
            print(f"Машина едет направо, скорость: {self.speed/1.5} км/ч")
        elif derection == 4:
            print(f"Машина едет налево, скорость: {self.speed/1.5} км/ч")


class Town_car(Car):

    def show_speed(self):
        print(f"Машина: {self.name}, скорость: {self.speed} км/ч")

        if self.speed >= 60:
            print("Вы превысили скорость")
        else:
            print(f"Машина: {self.name}, скорость: {self.speed} км/ч")


class Work_car(Car):
    def show_speed(self):
        print(f"Машина: {self.name}, скорость: {self.speed} км/ч")

        if self.speed >= 40:
            print("Вы превысили скорость")
        else:
            print(f"Машина: {self.name}, скорость: {self.speed} км/ч")


class Sport_car(Car):
    def show_speed(self):
        print(f"Машина: {self.name}, скорость: {self.speed} км/ч")


class Police_car(Car):
    def show_speed(self):
        print(f"Машина: {self.name}, скорость: {self.speed} км/ч")


car_one_town = Car(100, "Green", "Tayota", True)
car_two_work = Car(40, "Black", "Lada", False)
car_three_sport = Car(250, "Red", "Ferari", False)
car_four_police = Car(200, "Blue", "Ford", True)

Town_car.show_speed(car_one_town)
Work_car.show_speed(car_two_work)
Sport_car.show_speed(car_three_sport)
Police_car.show_speed(car_four_police)

print(car_one_town.show_speed())
print(car_one_town.go_car())
print(car_one_town.stop_car())
print(car_one_town.turn_car())
