letras = int(input())

linha = input().split()
certo = 0
cont = 0

for i in range(len(linha)):
    if linha[i] == "1":
        certo += 1

cont2 = 0

for i in range(len(linha)):
    if linha[i] == "1":
        cont += 1
        cont2 += 1
        if i < len(linha)-1 :
            if linha[i+1] == "0" and cont2 < certo:
                cont += 1

print(cont)