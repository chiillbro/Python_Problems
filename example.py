def printOrder(arr, n):
 #arr.sort() 
 
 mid = n//2 
 s1 = arr[:mid]
 s1 = s1[::-1]
 s2 = arr[:mid-1:-1] 
 print(mid)
 print(s1)
 print(s2)
 print(s2+s1) # Driver code
arr = [ 5, 4, 6, 2, 1, 3, 8, -1 ]
print(arr[:5:-1])
n = len(arr)
printOrder(arr, n)