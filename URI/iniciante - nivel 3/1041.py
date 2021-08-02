input = input().split()
x = float(input[0])
y = float(input[1])

if (x == y and x == 0):
  print('Origem')
elif(x > 0 or x < 0):
  if (y > 0 or y < 0):
    if (x > 0 and y < 0):
      print("Q4")
    elif (x > 0 and y > 0):
      print("Q1")
    elif (x < 0 and y > 0):
      print("Q2")
    elif (x < 0 and y < 0):
      print("Q3")
  else:
    print("Eixo X")
else:
  print("Eixo Y")




