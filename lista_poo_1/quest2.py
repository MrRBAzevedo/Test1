class viagem:
    def __init__(self):
        self.dist = 200
        self.temp = 3
    def velocidade_media(self):
        return self.dist / self.temp

a = viagem()

print(a.velocidade_media())
