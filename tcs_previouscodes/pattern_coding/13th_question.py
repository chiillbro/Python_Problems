n = int(input('enter a number: '))

for i in range(n):
    if i == 0:
     print('*'*(n*2-1))
    elif i == n-1:
       print(' '*(n-1) + '*')
    else:
       print(' '*i + '*' + ' '*(2*(n-1-i)-1) + '*')