import math

def finding_fare(source, destination):

    route = [['TH', 'GA', 'IC', 'HA', 'TE', 'LU', 'NI', 'CA'], [800, 600, 750, 900, 1400, 1200, 1100, 1500]]

    fare = 0.0

    if not (source in route[0] or destination in route[0]):
        print('INVALID INPUT, enter your source and destination as per stations listed', ['TH', 'GA', 'IC', 'HA', 'TE', 'LU', 'NI', 'CA'])
        exit()

    elif route[0].index(source) < route[0].index(destination):
        for i in range(route[0].index(source), route[0].index(destination)):
            fare += route[1][i]
    
    elif route[0].index(destination) < route[0].index(source):
        for i in range(route[0].index(source), len(route[1])):
         fare += route[1][i]
        
        for i in range(0, route[0].index(destination)):
            fare += route[1][i]

    return float(math.ceil(fare*0.005))

source = input("enter your source station from ['TH', 'GA', 'IC', 'HA', 'TE', 'LU', 'NI', 'CA']: ")
destination = input("enter your destination station from ['TH', 'GA', 'IC', 'HA', 'TE', 'LU', 'NI', 'CA']: ")
print(finding_fare(source, destination))