n = int(input())

pos = []
neg = []
for i in range(n):
    number_given = int(input())
    if number_given > 0:
        pos.append(number_given)
    else:
        neg.append(number_given)

pos_counter = 0
for a in range(len(pos)):
    pos_counter += 1

neg_sum = 0
for a in range(len(neg)):
    neg_sum += neg[a]

print(pos)
print(neg)

print(f"Count of positives are {pos_counter}. Count of negatives are {neg_sum}.")
