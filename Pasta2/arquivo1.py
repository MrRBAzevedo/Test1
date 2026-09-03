matriz = [[0 for n in range(10)] for i in range(3)]

print(*matriz)

while True:
    entrada = int(input())
    if entrada == -1: break

    if entrada % 2 == 1: indice = 0
    else: indice = 2

    matriz[indice].append(entrada)

    if matriz[indice][0] != 0: 
        matriz[1].append(matriz[indice][0])
        matriz[1] = matriz[1][1:11]

    matriz[indice] = matriz[indice][1:11]

print(matriz)