formato = int(input())
horario = input().split(":")
 
 
def monta_string(formato, lista):
    saida = ""

    if formato == 24:
        if int(lista[0]) >= formato:
            saida += "1"
            saida += lista[0][1]
        else:
            saida += lista[0]
    if formato == 12:
        if int(lista[0]) > formato :        
            saida += "0"
            saida += lista[0][1]
        else:
            saida += lista[0]
        
        if int(saida) == 0:
                saida = "10"
    saida += ":"
    if int(lista[1]) > 59:
        saida += "0"
        saida += lista[1][1]
    else:
        saida += lista[1]
    return saida 
 
print(monta_string(formato, horario))