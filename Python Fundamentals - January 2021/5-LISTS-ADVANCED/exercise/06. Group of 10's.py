nums = [int(el) for el in input().split(", ")]

group = 10

while nums:
    nums_group = []

    for num in nums:
        if num in range(group - 10, group + 1):
            nums_group.append(num)

    for num in nums_group:
        nums.remove(num)
    print(f"Group of {group}'s: {nums_group}")
    group += 10

"""
input example: 
1, 3, 3, 4, 34, 35, 25, 21, 33

expected output:
Group of 10's: [1, 3, 3, 4]
Group of 20's: []
Group of 30's: [25, 21]
Group of 40's: [34, 35, 33]
"""