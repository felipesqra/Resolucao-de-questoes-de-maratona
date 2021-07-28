inputs = input().split()
grades = input().split()

cont = 0

for i in range(len(grades)):
  if (int(grades[i]) >= int(grades[int(inputs[1])-1]) and int(grades[i]) != 0):
    cont += 1

print(cont)