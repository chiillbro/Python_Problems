'''n = int(input('enter a number: '))

for i in range(n):
    print(' '*i + '*'*n) '''

n=int(input())
for i in range(n):
 for j in range(n+i):
  if(j<i):
   print(' ',end='')
  else:
   print('*',end='')
 print()