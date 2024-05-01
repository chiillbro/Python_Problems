'''n = int(input('enter a number: '))

for i in range(n):
 for j in range(n):
     if i == 0 or i == n-1 or j == 0 or j == n-1:
        print('*', end='')
     else:
        print(' ', end='')
 print() '''


n=int(input())
t=2
for i in range(1,n+1):
 if i==1 or i==n:
  print('*'*n)
 else:
  l='*'+' '*(n-t)+'*'
  print(l)