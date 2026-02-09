class conta:
    def __init__(self):
        self.titular = 'Renan'
        self.num = 3262
        self.saldo = 0
    def creditar(self):
        self.saldo += 100
    def debitar(self):
        self.saldo -= 100

a = conta()

a.creditar()
a.creditar()
a.debitar()

print(f'''Titular da conta = {a.titular}
Número da conta = {a.num}
Saldo da conta = {a.saldo} reais
''')