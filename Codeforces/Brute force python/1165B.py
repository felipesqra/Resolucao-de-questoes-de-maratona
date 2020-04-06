qtd = int(input())
linha = input().split()

lista = list(map(int, linha))

lista.sort()

soma = 0
dias = 1
for i in range(qtd):
    if lista[i] >= dias:
        soma += 1
        dias += 1



print(soma)
