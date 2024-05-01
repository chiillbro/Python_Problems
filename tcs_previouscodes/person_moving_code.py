n = int(input('enter the number of turns: '))
case = 'R'
distance = 10
x, y = 0, 0
for i in range(n):
    if case == 'R':
      x +=distance
      case = 'U'
      distance +=10
    elif case == 'U':
      y +=distance
      case = 'L'
      distance +=10
    elif case == 'L':
       x -=distance
       case = 'D'
       distance +=10
    elif case == 'D':
       y -=distance
       case = 'A'
       distance +=10
    elif case == 'A':
       x +=distance
       case = 'R'
       distance +=10

print(x, y)