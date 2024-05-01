'''num = int(input('enter your number: '))
temp = num
factorial = 1
for i in range(num):
    second_nmbr = temp - 1
    factorial *=temp
    temp = second_nmbr
if num<0:
    print('factorial not possible, enter a positive number: ')
else:
    print('factorial of', num, 'is', factorial)

'''
def factorial(num):
    if num == 0:
      return 1
    
    return num * factorial(num-1)
nmbr = int(input('enter a number: '))
print(factorial(nmbr))