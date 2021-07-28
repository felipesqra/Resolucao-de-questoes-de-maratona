inputs = int(input())

cont = 0

for i in range(inputs):
  line = input().split()
  if ((int(line[0]) + int(line[1]) + int(line[2])) > 1):
    cont += 1

print(cont)
