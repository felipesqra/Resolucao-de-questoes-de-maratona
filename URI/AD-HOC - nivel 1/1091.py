

while(True):
  cases = int(input())
  
  if (cases == 0):
    break

  divisor_point = input().split()

  n = int(divisor_point[0])
  m = int(divisor_point[1])

  answers = []

  def quadrant_indentifier(n,m,x,y):
    answer = ""
    lest_west = x-n
    north_south = y-m

    if (north_south == 0 or lest_west == 0):
      answer = 'divisa'
    elif(lest_west != 0):
      if (north_south != 0):
        if (lest_west > 0 and north_south < 0):
          answer = "SE"
        elif (lest_west > 0 and north_south > 0):
          answer = "NE"
        elif (lest_west < 0 and north_south > 0):
          answer = "NO"
        elif (lest_west < 0 and north_south < 0):
          answer = "SO"
      else:
        answer = "divisa"
    else:
      answer = "divisa"

    return answer


  for i in range(cases):
    coord = input().split()
    x = int(coord[0])
    y = int(coord[1])

    answers.append(quadrant_indentifier(n,m,x,y))

  for i in range(len(answers)):
    print(answers[i])