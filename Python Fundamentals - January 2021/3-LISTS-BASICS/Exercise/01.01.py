num_input = [int(x) for x in input().split()]

new_list = []
for el in num_input:
    if el < 0:
        new_list.append(abs(el))
    else:
        new_list.append(-el)
print(new_list)
