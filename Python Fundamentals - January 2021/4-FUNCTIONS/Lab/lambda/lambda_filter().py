numbers_list = [1, 2, 3, 4, 5, 6]

even_nums = list(filter((lambda x: x % 2 == 0), numbers_list))
print(even_nums)
# [2, 4, 6]
