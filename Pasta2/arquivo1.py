fim = int(input())
numero = 2
soma = 0

while numero < fim:
    divisor = 2
    
    while divisor < numero:
        if numero % divisor == 0:
            break

        divisor += 1
    else:
        soma += numero
        
    numero += 1
    
print(soma)
