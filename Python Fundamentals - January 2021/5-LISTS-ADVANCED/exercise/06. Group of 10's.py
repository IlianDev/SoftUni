"""
input example:
8, 12, 38, 3, 17, 19, 25, 35, 50, 60, 65, 90, 95, 70, 45, 34, 101, 85, 87, 74, 72

expected output:
Group 10's [8, 3]
Group 20's [12, 17, 19]
Group 30's [25]
Group 40's [38, 35, 34]
Group 50's [50, 45]
Group 60's [60]
Group 70's [65, 70]
Group 80's [74, 72]
Group 90's [90, 85, 87]
Group 100's [95]
Group 110's [101]
"""

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

