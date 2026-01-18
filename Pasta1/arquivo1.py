salario = float(input())

if salario <= 400:
    reajuste = 15
elif salario <= 800:
    reajuste = 12
elif salario <= 1200:
    reajuste = 10
elif salario <= 2000:
    reajuste = 7
else:
    reajuste = 4

print(f'Novo salario: {salario + salario * reajuste * 0.01:.2f}')
print(f'Reajuste ganho: {salario * reajuste * 0.01:.2f}')
print(f'Em percentual: {reajuste} %')