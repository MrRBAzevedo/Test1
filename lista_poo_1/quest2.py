class viagem:
    def __init__(self):
        self.dist = 0
        self.temp = 0
    def velocidade_media(self):
        return self.dist / self.temp

a = viagem()

dist = int(input('Insira a distância: '))
hora = int(input('Insira as horas: '))
minuto = int(input('Insira os minutos: '))
temp = hora + minuto / 60

a.dist = dist
a.temp = temp


print(a.velocidade_media())
