"""
Add a new item to the original dictionary, and see that the keys list gets updated as well:
"""
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

#ORIGINAL
x = car.keys()
y = car.values()
print(f"{x} ---- {y}")

# CHAGED
car["colour"] = "white"
print(f"{x} ---- {y}")

car["year"] = 2020
print(f"{x} ---- {y}")
