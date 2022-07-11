print("\tUsing end= :")
thislist = ["apple", "banana", "cherry"]
[print(f"{x}", end=", ") for x in thislist]

print("\n\tUsing join:")
thislist = ["apple", "banana", "cherry"]
result = ", ".join(thislist)
print(result)
