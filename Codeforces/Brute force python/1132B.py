qtd = int(input())
linha = input().split()
qtd_c = int(input())
s_linha = input().split()



precos = list(map(int, linha))
cupons = list(map(int, s_linha))

lista = sorted(precos, reverse = True)

soma_total = sum(lista)


for i in range(len(cupons)):
    print(soma_total-lista[cupons[i]-1])