trainee_list = [[], [], [], []]
for i in range(3):
    for j in range(3):
        trainee_list[i].append(int(input("enter the oxygen level of trainee {0} in round {1}: ".format(i+1, j+1))))
        if trainee_list[i][-1] not in range(1,101):
            print('Invalid input')    
for i in range (3):
    trainee_list[3].append((trainee_list[0][i] + trainee_list[1][i] + trainee_list[2][i])//3)
    maximum  = max(trainee_list[3])
for i in trainee_list[3]:
    if i < 70:
        print('trainee {} is unfit'.format(trainee_list[3].index(i)+1))
for i in trainee_list:
    if i == maximum:
        print('fittest trainee: {}'.format(trainee_list[3].index(i)+1))

            