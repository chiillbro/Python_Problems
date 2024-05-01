'''num = int(input('enter your number: '))
i = 1
while i<=num:
    if num%i == 0:
        print(i, end=' ')
    i = i+1 '''
'''

n=int(input("enter a number : "))
l=[i for i in range(1,n+1) if(n%i==0)]
for j in l:
 print(j, end=' ')  '''


''''num = int(input('enter your number: '))
prime_factors = []
for i in range(2, num+1):
    #if i == 1:
       #continue
    if num%i == 0:
      flag = 0
      for x in range(2, i):
        if i%x == 0:
           flag = 1
           break
      if flag == 0:
         prime_factors.append(i)
print(prime_factors) '''

num = int(input('enter your number: '))
prime_factors = []
for i in range(1, num+1):
    #if i == 1:
       #continue
    if num%i == 0:
      count = 0
      for x in range(1, i+1):
        if i%x == 0:
           count +=1
      if count == 2:
         prime_factors.append(i)
print(prime_factors)

