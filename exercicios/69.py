list_a = [1, 2, 3, 4, 5, 6]
list_b = [1, 2, 3, 4]

list_sum = zip(list_a, list_b)

list_sum = list(list_sum)

print([num_a + num_b for num_a, num_b in list_sum])
