import math

class circulo:
    def __init__(self):
        self.__raio = float(0)  

    def set_raio(self, raio):
        if raio < 0:
            raise ValueError('O raio deve ser um valor positivo.')
        else:
            self.__raio = raio

    def get_raio(self):
        return self.__raio
    
    def calc_area(self):
        return math.pi * self.__raio ** 2
    
    def calc_circ(self):
        return math.pi * 2 * self.__raio
    
class UserInteface:
    @staticmethod
    def main():
        x = circulo()
        x.set_raio(float(input('Insira o raio do círculo: ')))

        print(f'''O raio do círculo é: {x.get_raio()}
A sua área é: {x.calc_area():.3f}
E sua circunferência é: {x.calc_circ():.3f}''')
        
UserInteface.main()
