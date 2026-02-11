import random

class conta:
    def __init__(self):
        self.__titular = ' '
        self.__numero = random.randint(1000, 9999)
        self.__saldo = 0

    def set_titular(self, name):
        self.__titular = name

    def depositar(self, valor):
        if valor >= 0:
            self.__saldo += valor
        else:
            raise ValueError('Você não pode depositar um valor negativo.')
        
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            raise ValueError('Você não pode sacar um valor negativo ou maior que seu saldo atual.')
        
    def __str__(self):
        return f'''O titular da conta é: {self.__titular}
O número da conta é: {self.__numero} 
O saldo atual é: {self.__saldo} reais'''
    
class UserInterface:
    @staticmethod
    def main():
        a = conta()
        a.set_titular(input('Insirar o nome do titular da conta: '))
        a.depositar(int(input('Insira o valor que deseja depositar: ')))
        a.sacar(int(input('Insira o valor que deseja sacar: ')))

        b = conta()
        b.set_titular(input('\nInsirar o nome do titular da conta: '))
        b.depositar(int(input('Insira o valor que deseja depositar: ')))
        b.sacar(int(input('Insira o valor que deseja sacar: ')))


        print(a, '\n')
        print(b)

UserInterface.main()