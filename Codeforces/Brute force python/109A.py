objetivo = int(input())

def fun(objetivo): 
    resultado = ""
    
    quatros = 0
    setes = 0
    
    resto = objetivo
    
    while resto >= 4:
        if resto % 7 == 0:
            setes += resto / 7
            resto -= 7*(resto/7)
        if resto >= 4:
            resto -= 4
            quatros += 1

    resultado += "4"*quatros
    
    resultado += "7"*int(setes)
    
    
    if resultado == "" or 0 < resto:
        return -1
    else:
        return resultado

print(fun(objetivo))