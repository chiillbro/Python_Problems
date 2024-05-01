n = int(input('enter number of rows: '))
m = 1
for i in range(1, n+1):
  if i<=(n+1)/2:
    print(' '*(int((n+1)/2)-i) + '*'*i)
  else:
    while i:
     print(' '*m + '*'*(n+1-i))
     break
    m +=1 