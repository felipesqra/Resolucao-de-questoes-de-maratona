num_casos = int(input())
 
def doces(num):
    cont = 0
    
    if num >= 3:
        num -= 1
        cont = num // 2
    
    return cont
 
 
 
lista = []
 
for i in range(num_casos):
    num_doces = int(input())
    lista.append(doces(num_doces))
 
 
for i in range(len(lista)):
    print(lista[i])