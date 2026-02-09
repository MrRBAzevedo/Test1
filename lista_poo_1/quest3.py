class conta:
    def __init__(self):
        self.titular = 'Renan'
        self.num = 3262
        self.saldo = 0
    def creditar(self, valor):
        self.saldo += valor
    def debitar(self, valor):
        self.saldo -= valor

a = conta()

a.creditar(2000)
a.debitar(100)

print(f'''Titular da conta = {a.titular}
Número da conta = {a.num}
Saldo da conta = {a.saldo} reais
''')