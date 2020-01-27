from time import sleep
from itertools import cycle

class TrafficLight:
    #атрибут
    def __init__(self):
        self.__color = [("Красный", 7), ("Желтый", 2), ("Зеленый", 5)]

    #метод
    def running(self):
        for color, sec in cycle(self.__color):
            print(color)
            sleep(sec)

light = TrafficLight()
light.running()

