thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "item": "test"
}

"""chage the value"""
thisdict["year"] = 2018

"""
using update() method it will update the dictionary with the items from the given argument
The argument must be a dictionary, or an iterable object with key:value pairs.
"""
thisdict.update({"year": 2020})
thisdict.update({"colour": "black"})

print(thisdict)

""" pop() -> remove the item from the dictionary with spedcified key name """
thisdict.pop("item")
print(f"pop() -> {thisdict}")

""" 
popitem() -> remove the last inserted item from the dictionary 
(in versions before 3.7, a random item is removed instead):
"""
thisdict.popitem()
print(f"popitem() -> {thisdict}")

"""
del -> keyword removes the item with the specified key name from the dictionary
it also delete the dictionary permanently 
"""
del thisdict["model"]
print(f"del -> {thisdict}")

""" clear() -> empties the dictionary"""
thisdict.clear()
print(thisdict)  # {}

