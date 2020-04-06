import math
qtd_circulos = int(input())

soma = 0
areas = [int(v) for v in input().split()]

areas.sort(reverse=True)
for i in range(qtd_circulos):
    if i%2 == 0:
        soma += (int(areas[i])**2)
    if i%2 != 0:
        soma -= (int(areas[i])**2)

print(round(math.pi*soma, 10))