def max_parked_spaces(parking_space):
    max_parked = -1
    max_row = -1

    for i, row in enumerate(parking_space):
        parked_count = sum(row)
        if parked_count > max_parked:
          max_parked = parked_count
          max_row = i + 1

    return max_row


parking_space = [[0,1,0], [1,1,1], [1,1,1]]

print(max_parked_spaces(parking_space))