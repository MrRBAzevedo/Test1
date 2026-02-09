class entrada:
    def __init__(self):
        self.dia = 'terça'
        self.hora = 16
    def calc_preco(self):
        if self.dia == 'segunda' or self.dia == 'terça' or self.dia == 'quinta':
            return 16 if (self.hora < 17) else 16 * 1.5
        elif self.dia == 'sexta' or self.dia == 'sabado' or self.dia == 'domingo':
            return 20 if (self.hora < 17) else 20 * 1.5
        else:
            return 8 
    def meia_entrada(self):
        if self.dia == 'quarta':
            return 8
        else:
            return self.calc_preco() / 2

        

a = entrada()

print(f'''Dia: {a.dia}
Hora: {a.hora}h
Preço da entrada inteira: {a.calc_preco():.2f} reais
Preço da meia-entrada {a.meia_entrada():.2f} reais''')