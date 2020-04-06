cidades = int(input())
coordenadas = [int(i) for i in input().split()]
menores = []
maiores = []

def maior(x,y,z):
    if z-y > y-x:
        return z-y
    else:
        return y-x

def menor(x,y,z):
    if z-y > y-x:
        return y-x
    else:
        return z-y

for i in range(cidades):
    if i == 0:
        menores.append(coordenadas[1]-coordenadas[0])
        maiores.append(coordenadas[cidades-1]-coordenadas[0])
    elif i == cidades-1:
        menores.append(coordenadas[cidades-1]-coordenadas[cidades-2])
        maiores.append(coordenadas[cidades-1]-coordenadas[0])
    else:
        maiores.append(maior(coordenadas[0], coordenadas[i], coordenadas[cidades-1]))
        menores.append(menor(coordenadas[i-1], coordenadas[i], coordenadas[i+1]))
    
for i in range(len(maiores)):
    print(str(menores[i]) + " " + str(maiores[i]))