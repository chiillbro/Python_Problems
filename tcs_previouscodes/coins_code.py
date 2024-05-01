num = int(input('enter a number: '))
one_rupee = 0
two_rupee = 0
five_rupee = int((num - 4)/5)

if (num-5*five_rupee)%2 == 0:
    one_rupee = 2

else:
    one_rupee = 1

two_rupee = int((num - 5*five_rupee - one_rupee)/2)

print('total number of coins', one_rupee + two_rupee + five_rupee)
print('no.of one rupee coins', one_rupee)
print('no.of two rupee coins', two_rupee)
print('no.of five rupee coins', five_rupee)