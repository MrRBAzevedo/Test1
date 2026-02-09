class circulo:
    def __init__(self):
        self.raio = 10
    def calc_circ(self):
        return self.raio * 2 * 3.14
    def calc_area(self):
        return self.raio ** 2 * 3.14
    
a = circulo()

print(a.raio, a.calc_circ(), a.calc_area())