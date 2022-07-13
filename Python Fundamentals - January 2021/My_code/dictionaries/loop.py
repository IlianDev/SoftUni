thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "item": "test"
}

for x in thisdict:
    print(x)
print("1. print the keys using thisdict.keys()")
for x in thisdict.keys():
    print(x)

print("1. print the values using thisdict[x]")
for x in thisdict:
    print(thisdict[x])

print("2. print the values using thisdict.values()")
for x in thisdict.values():
    print(x)

print("print the keys: values pairs using thisdict.items()")
for x, y in thisdict.items():
    print(x, y)
    print(f"{x}: {y}")
