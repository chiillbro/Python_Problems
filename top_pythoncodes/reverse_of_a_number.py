num = int(input('enter your number: '))
temp = num
sum = 0
for i in range(len(str(num))):
    remainder = int(temp%10)
    sum = sum*10 + remainder
    temp = temp / 10
if num < 10:
    print('enter a number other than one digit')
else:
    print('reverse of the number is:', sum)