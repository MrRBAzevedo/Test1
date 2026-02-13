import os

class Entrada:
    def __init__(self):
        self.__dia = 'quarta'
        self.__horario = 16

    def set_dia(self, dia):
        dia = dia.lower()
        
        if dia not in ['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado']:
            raise ValueError('Insira um dia válido!')
        else:
            self.__dia = dia
        
    def set_horario(self, horario):
        if horario < 0 or horario > 24:
            raise ValueError('Insira um horário válido')
        else:
            self.__horario = horario                      
               
    def meia_entrada(self):
        return self.get_preco() / 2

    def get_preco(self):
        if self.__dia in ['segunda', 'terça', 'quinta']:
            return 16 if (self.__horario < 17) else 24
        elif self.__dia in ['sexta', 'sábado', 'domingo']:
            return 20 if (self.__horario < 17) else 30
        else:
            return 8

    def __str__(self):
        return f'''\nSua sessão será {self.__dia} às {self.__horario}h.
Meia-entrada: {self.meia_entrada():.2f} reais
Entrada inteira: {self.get_preco():.2f} reais\n'''


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

    