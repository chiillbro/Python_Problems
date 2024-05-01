'''num = int(input('enter a nmbr:'))
for i in range(2, num):
    if num%i == 0:
     print(num, 'not a prime')
     break
    else:
     print(num, 'is a prime')
     break'''



low = int(input('enter your first number: '))
high = int(input('enter your second number: '))
primes = []


for i in range(low, high+1):
    flag = 0
    if i<2:
     continue
    if i == 2:                          #TO FIND THE LIST OF PRIMES IN THE MENTIONED RANGE
     primes.append(2)
     continue
    for x in range(2, i):
     if i%x == 0:
      flag =1
      break
    if flag == 0:
     primes.append(i)
print(primes)
