'''num = int(input('enter a number: '))
temp = num
digit, sum = 0, 0
length = len(str(num))
for i in range(length):
    digit = int(temp%10)
    temp = temp/10
    sum+=pow(digit, length)
if sum == num:
    print('Armstrong')
else:
    print('not an Armstrong')    '''





low, high = int(input(('enter your first number: '))), int(input(('enter your second number: ')))

for n in range(low, high + 1):

    # order of number
    order = len(str(n))

    # initialize sum
    sum = 0

    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if n == sum:
        print(n, end=", ")