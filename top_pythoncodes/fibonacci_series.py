num = int(input("enter an integer: "))
n1 = 0
n2 = 1
lst = [n1, n2]
print('Fibonacci series:', n1, n2, end=' ')      #---------------FIRST METHOD(SIMPLE ITERATIVE METHOD)---------------
for i in range(2, num):
    n3 = n1+n2
    n1 = n2
    n2 = n3
    print(n3, end=' ')
    lst.append(n3)
print('\n')
print('last term of the fibonanci series is:', lst[::-1][0])





''''def fibonacci_series(i):
    if i<=1:
     return i
    else:
     return(fibonacci_series(i-1) + fibonacci_series(i-2))        #---------SECOND METHOD(RECURSIVE METHOD)---------
num = int(input('enter an integer:'))

if num < 0:

 print("enter a positive number")

else:
 print('fibonacci series: ', end=' ')

for i in range(num):
 print(fibonacci_series(i), end=' ') '''




'''import math

def fibonacci_series(phi, n):
   
   for i in range(n):
      result = round(pow(phi, i) / math.sqrt(5))      #FORMULA METHOD Fn = {[(1+sqrt5)/2]^n}/sqrt5
      print(result, end=' ')

num = int(input('enter a number:'))
phi = (math.sqrt(5) + 1) / 2
fibonacci_series(phi, num)'''