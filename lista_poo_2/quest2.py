class Viagem:
    def __init__(self):
        self.__distancia = float(0)
        self.__tempo = float(0)
    
    def set_distancia(self, distancia):
        if distancia < 0:
            raise ValueError('A distância deve ser um valor positivo.')
        else:
            self.__distancia = distancia

    def set_tempo(self, horas, minutos):
        if horas < 0 or minutos < 0:
            raise ValueError('O tempo deve ser um valor positivo.')
        else:
            self.__tempo = horas + minutos / 60

    def get_distância(self):
        return self.__distancia
    
    def get_tempo(self):
        return self.__tempo
    
    def velociadade_media(self):
        return self.__distancia / self.__tempo
    
class UserInterface:
    @staticmethod
    def main():
        a = Viagem()
        a.set_distancia(float(input('Insira a distância percorrida: ')))
        a.set_tempo(float(input('Insira o número de horas: ')), float(input('Insira o número de minutos: ')))

        print(f'''Foram percorridos {a.get_distância()} km em {a.get_tempo():.2f} horas, logo, a velocidade média foi de {a.velociadade_media():.2f} km/h''')

UserInterface.main()