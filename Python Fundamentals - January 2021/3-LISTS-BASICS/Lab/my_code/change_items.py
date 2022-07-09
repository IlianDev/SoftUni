thislist = ["apple", "banana", "cherry"]
thislist[1] = "none"
print(thislist)
# ['apple', 'none', 'cherry']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["none1", "none2"]
print(thislist)
# ['apple', 'none1', 'none2', 'orange', 'kiwi', 'mango']


# Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
# ['apple', 'watermelon']

# Insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
# ['apple', 'banana', 'watermelon', 'cherry']
