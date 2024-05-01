'''rows = int(input('enter the number of rows: '))
columns = int(input('enter the number of columns: '))

for i in range(rows):
    for j in range(columns):
        if i == 0 or i == rows-1 or j == 0 or j == columns-1:
            print('*', end='')
        else:
            print(' ', end='')
    print()'''


a = int(input()) # rows
b = int(input()) # columns
for i in range(a):
 print('*'*b if i == 0 or i == a-1 else '*'+' '*(b-2)+'*')