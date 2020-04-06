tamanho = int(input())

linha = input()

zero = 0
um = 0

for i in range(tamanho):
    if linha[i] == "1":
        um += 1
    if linha[i] == "0":
        zero += 1

resto = 0
total = 0

if zero > um:
    resto = zero - um
if um > zero:
    resto = um - zero
   
total = zero + um - resto


print(tamanho - total)