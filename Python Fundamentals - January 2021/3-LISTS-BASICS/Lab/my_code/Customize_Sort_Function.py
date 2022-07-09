print("key = function: ")
print("Sort the list based on how close the number is to 50:")


def myfunc(n):
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
print(f"original list: {thislist}")
thislist.sort(key=myfunc)
print(f"sorted: {thislist}")

"""
By default the sort() method is case sensitive, 
resulting in all capital letters being sorted before lower case letters:
"""
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
# ['Kiwi', 'Orange', 'banana', 'cherry']

"""
Perform a case-insensitive sort of the list
"""
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)
# ['banana', 'cherry', 'Kiwi', 'Orange']
