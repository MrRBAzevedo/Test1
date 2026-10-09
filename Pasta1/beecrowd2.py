n = int(input())
cidades = []

while n != 0:
    cidade = []

    for i in range(n):
        x, y = map(int, input().split())

        cidade.append((y, x))
        cidade.sort()

    cidades.append(cidade)
    n = int(input())

for cidade in cidades:
    print(cidade)