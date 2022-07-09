factor = int(input("factor: "))
count = int(input("count: "))

length = factor * count
new_list = []

for x in range(factor, length + 1, factor):
    new_list.append(x)
print(new_list)
