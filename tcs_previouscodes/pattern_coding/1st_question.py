'''n = int(input('enter number of lines: '))

for i in range(n):
 for j in range(i+1):
      print('*', end='')
 print()  '''

n = int(input("Enter the number: "))
for i in range(n+1):
 print('*'*i)
