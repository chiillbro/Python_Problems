n = int(input('enter number of rows: '))
m = 1
p = int((n-1)/2)
for i in range(n):
    if i < (n+1)/2:
        print(' '*int((n-1)/2-i) + '*'*(2*i+1))
    else:
        while i:
            print(' '*m + '*'*(2*p-1))
            break
        m +=1
        p -=1