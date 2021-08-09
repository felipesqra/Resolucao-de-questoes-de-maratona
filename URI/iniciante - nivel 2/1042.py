input = input().split()

def convert(x):
  return int(x)

input_ints = list(map(convert, input))

def ord_one_time(list):
  for i in range(3):
    if ( i != 2):
      if list[i] > list[i+1]:
        pivor = list[i]
        list[i] = list[i+1]
        list[i+1] = pivor

  return list

result = ord_one_time(input_ints)
result = ord_one_time(result) + [''] + input_ints

for i in range(len(result)):
  print(result[i])






  
    




