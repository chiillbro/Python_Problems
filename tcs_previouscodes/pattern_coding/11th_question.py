n = int(input('enter a number: '))

for i in range(0, n):
    if i == 0:
        print(' '*(n-1) + '*')
    elif i == n-1:
        print('*'*(2*i+1))
    else:
        print(' '*(n-1-i) + '*' + ' '*((i-1)*2+1) +'*')