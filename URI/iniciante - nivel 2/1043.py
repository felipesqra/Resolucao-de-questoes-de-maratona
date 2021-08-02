input = input().split()
a = float(input[0])
b = float(input[1])
c = float(input[2])

primeira_condicao = (b-c)  < a and a < (b+c)
segunda_condicao = (a-c)  < b and b < (a+c)
terceira_condicao = (a-b)  < c and c < (a+b)

if (primeira_condicao and segunda_condicao and terceira_condicao):
  print('Perimetro = {:.1f}'.format(a+b+c))
else:
  print('Area = {:.1f}'.format(((a+b)*c)/2))
