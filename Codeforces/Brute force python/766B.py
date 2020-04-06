total = int(input())

linha = [int(v) for v in input().split()]

linha.sort()

def testa_existencia(a, b, c):
    if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b:
        return True

resultado = "NO"

for i in range(total):
    if i == 0:
        if testa_existencia(linha[i], linha[i+1], linha[i+2]) == True:
            resultado = "YES"
    elif i == total-1:
        if testa_existencia(linha[total-1], linha[total-2], linha[total-3]) == True:
            resultado = "YES"
    elif i == 1 or i == total - 2:
        if testa_existencia(linha[i], linha[i-1], linha[i+1]) == True:
            resultado = "YES"
    else:
        if testa_existencia(linha[i], linha[i-1], linha[i+1]) == True:
            resultado = "YES"
        if testa_existencia(linha[total-1], linha[total-2], linha[total-3]) == True:
            resultado = "YES"
        if testa_existencia(linha[i], linha[i+1], linha[i+2]) == True:
            resultado = "YES"

print(resultado)