t = int(input())
 
alfa = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
 
result = []
 
def fun(lista):
    s = ""
 
    n = lista[0]
    a = lista[1]
    b = lista[2]
 
    while len(s) < n:
        for i in range(b):
            if len(s) < n:
                s += alfa[i]
   
    return s
 
 
for i in range(t):
    linha = [int(i) for i in input().split()]
    result.append(fun(linha))
 
for i in range(len(result)):
    print(result[i])