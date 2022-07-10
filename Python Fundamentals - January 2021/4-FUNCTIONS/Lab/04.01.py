COFFEE = 1.50
WATER = 1.00
COKE = 1.40
SNACKS = 2.00


def solve(pr, q):
    result = None
    if pr == "coffee":
        result = COFFEE * q
    elif pr == 'water':
        result = WATER * q
    elif pr == 'coke':
        result = COKE * q
    elif pr == 'snacks':
        result = SNACKS * q
    return f"{result:.2f}"


products = input()
quantity = int(input())
print(solve(products, quantity))
