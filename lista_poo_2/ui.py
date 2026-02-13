from quest4 import Entrada
import os

class UserInterface:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            try:
                op = UserInterface.menu()
                if op == 1: UserInterface.entrada()
            except:
                print("Valor informado não é válido")    
        print("Tchau!!!")

    @staticmethod
    def menu():
        print("1 - Ingresso, 9 - Fim")
        op = int(input("Informe sua opção: "))
        return op

    @staticmethod
    def entrada():
        os.system('cls')
        a = Entrada()
        dia = input('Insira o dia da sessão: ')
        a.set_dia(dia)
        horario = int(input('Insira o horário da sessão: '))
        a.set_horario(horario)
        print(a)

UserInterface.main()
