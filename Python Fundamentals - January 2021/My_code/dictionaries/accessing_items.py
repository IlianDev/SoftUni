import item as item

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# 1.
x = thisdict["model"]
print(x)

# 2. using get()
y = thisdict.get("year")
print(y)

# 3. keys() -> will return a list of all keys in the dictionary
keys = thisdict.keys()
print(f"keys() -> {keys}")  # dict_keys(['brand', 'model', 'year'])

# 4. values() -> will return a list of all values in the dictionary
values = thisdict.values()
print(f"values() -> {values}")

# 5. items() method will return each item in a dictionary, as tuples in a list.
items = thisdict.items()
print(f"items() -> {items}")

# 6. check if key exists in the dictionary
if "model" in thisdict:
    print("yes")
