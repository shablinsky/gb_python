class Road:
    def __init__(self, lenght, width):
        self._length = lenght
        self._width = width

    def get_weight(self, spec_grav, thick):
        return self._length * self._width * spec_grav * thick / 1000

r = Road(5000, 20)
print(r.get_weight(25, 5))
