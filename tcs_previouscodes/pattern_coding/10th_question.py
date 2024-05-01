n = int(input('enter a number: '))
#j = 1
for i in range(0, n):
    if i == 0:
        print(' '*(n-1) + '*')
    else:
        #while j>=i:
             
         print(' '*(n-1-i) + '*'*(i*2+1))
         #break
        #j +=2