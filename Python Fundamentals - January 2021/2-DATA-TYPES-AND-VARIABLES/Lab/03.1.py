n = int(input())
special = [5, 7, 11]

for i in range(1, n + 1):
    digits_sum = 0
    for digit in str(i):
        digits_sum += int(digit)
    is_special = digits_sum in special
    print(f'{i} -> {is_special}')

