lata = int(input())
nomes = ["Sheldon","Leonard","Penny","Rajesh","Howard"]
latas_bebidas = [0,0,0,0,0]

cont = 1
soma = 0

for i in range(lata):
    if soma < lata:
        latas_bebidas[0] += cont
        soma += cont
    if soma < lata:
        latas_bebidas[1] += cont
        soma += cont
    if soma < lata:
        latas_bebidas[2] += cont
        soma += cont
    if soma < lata:
        latas_bebidas[3] += cont
        soma += cont
    if soma < lata:
        latas_bebidas[4] += cont
        soma += cont
    else:
        break
    cont *= 2


retorno = ""

for i in range(4, -1, -1):
    if latas_bebidas[i] < latas_bebidas[i-1]:
        retorno = nomes[i-1]
        break

if retorno == "":
    retorno = nomes[4]

print(retorno)