consultas = int(input())
resultados = []
for i in range(consultas):
    madeiras = int(input())

    comprimentos = [int(v) for v in input().split()]

    comprimentos.sort()

    menorT = int(comprimentos[len(comprimentos)-2]) - 1

    if len(comprimentos)-2 >= menorT:
        resultados.append(menorT)
    elif len(comprimentos)-2 < menorT:
        resultados.append(len(comprimentos)-2)

for i in range(len(resultados)):
    print(resultados[i])