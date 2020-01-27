class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        mass = self._length * self._width * 25 * 5 / 1000
        print(mass, 'т')

road = Road(length=int(input("Введите длину дорожного полотна: ")),
            width=int(input("Введите ширину дорожного полотна: ")))
road.mass()