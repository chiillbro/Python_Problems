n = int(input('enter a number: '))
m = n
for i in range(n):

  while i<n:
    print(' '*i + '*'*(2*(m+1)-3))
    break
  m -=1