print("Sort the list alphabetically: ")
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
print(thislist)
thislist.sort()
print(thislist)
# ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

print("\nSort the list numerically: ")
thislist = [100, 50, 65, 82, 23]
print(thislist)
thislist.sort()
print(thislist)
# [23, 50, 65, 82, 100]

print("\nSort the list descending")
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
print(thislist)
thislist.sort(reverse=True)
print(thislist)
# ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

print("\nSort the list descending")
thislist = [100, 50, 65, 82, 23]
print(thislist)
thislist.sort(reverse=True)
print(thislist)
# [100, 82, 65, 50, 23]