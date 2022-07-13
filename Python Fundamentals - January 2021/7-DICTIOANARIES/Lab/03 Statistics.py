"""
INPUT
bread: 4
cheese: 2
ham: 1
bread: 1
statistics

OUTPUTS
Products in stock:
- bread: 5
- cheese: 2
- ham: 1
Total Products: 3
Total Quantity: 8

"""

data = input()
prducts_dict = {}

while not data == "statistics":
    product, quantity = data.split(": ")
    quantity = int(quantity)
    if product not in prducts_dict:
        prducts_dict[product] = quantity
    else:
        prducts_dict[product] += quantity

    data = input()

print("Products in stock:")

for key, value in prducts_dict.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(prducts_dict)}")
print(f"Total Quantity: {sum(prducts_dict.values())}")