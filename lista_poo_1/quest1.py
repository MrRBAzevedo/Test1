import math

class circulo:
    def __init__(self):
        self.raio = 0
    def calc_circ(self):
        return self.raio * 2 * math.pi
    def calc_area(self):
        return self.raio ** 2 * math.pi

a = circulo()
a.raio = int(input('Insira o raio: '))

print(a.raio, a.calc_circ(), a.calc_area())