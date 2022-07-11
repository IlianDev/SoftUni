string_list = ["1", "2", "3", "4", "5", "6"]
print(string_list)  # ['1', '2', '3', '4', '5', '6']
numbers_list = list(map(lambda x: int(x), string_list))
print(numbers_list)  # [1, 2, 3, 4, 5, 6]
