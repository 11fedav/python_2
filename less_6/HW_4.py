# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("{} поехала!".format(self.name))

    def stop(self):
        print("{} остановилась".format(self.name))

    def turn(self, direction):
        print("{} повернула направо".format(self.name, direction))

    def show_speed(self):
        print("Текущая скорость автомобиля: {}".format(self.speed))

class TownCar(Car):
    def show_speed(self):

        if self.speed > 60:
            print("Вы привышаете скорость!", self.speed)
        else:
            print("Вы едите с оптимальной скоростью", self.speed)

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Вы привышаете скорость!", self.speed)
        else:
            print("Вы едите с оптимальной скоростью", self.speed)

class PoliceCar(Car):
    pass

town_car = TownCar(60, 'Белая', 'Alfa Romeo', False)
town_car.go()
town_car.show_speed()
town_car.turn('Повернула налево')

sport_car = SportCar(350, 'Желтая', 'Lamborghini', False)
sport_car.go()
sport_car.show_speed()
sport_car.stop()

work_car = WorkCar(50, 'Коричневая', 'Ford Transit', False)
work_car.go()
work_car.show_speed()
work_car.turn("Повернула направо")

police_car = PoliceCar(100, 'Белая с синими полосками', 'Toyota Camry', True)
police_car.go()
police_car.show_speed()