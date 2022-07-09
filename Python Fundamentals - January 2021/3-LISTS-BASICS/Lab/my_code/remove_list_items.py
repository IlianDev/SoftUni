thislist = ["apple", "banana", "cherry"]
thislist.remove("apple")
print(thislist)
# ['banana', 'cherry']

# The pop() method removes the specified index.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
# ['apple', 'cherry']

# Remove the last item:
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
# ['apple', 'banana']

thislist = ["apple", "banana", "cherry"]
del thislist[1]
print(thislist)
# ['apple', 'cherry']