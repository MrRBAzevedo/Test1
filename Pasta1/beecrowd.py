x, y = map(float, input().split())

resultado = ''

if x == 0: 
    if y == 0: resultado = 'Origem'
    else: resultado = 'Eixo Y'
elif y == 0: resultado = 'Eixo X'
elif x > 0:
    if y > 0: resultado = 'Q1'
    else: resultado = 'Q4'
else: 
    if y > 0: resultado = 'Q2'
    else: resultado = 'Q3'

print(resultado)