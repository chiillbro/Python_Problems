num = int(input('enter your number: '))
temp = num
sum = 0
for i in range(len(str(num))):
    remainder = int(temp%10)
    temp = temp / 10
    sum = sum*10 + remainder
if sum == num:
    print(num, 'is a palindrome')
else:
    print(num, 'is not a palindrome')