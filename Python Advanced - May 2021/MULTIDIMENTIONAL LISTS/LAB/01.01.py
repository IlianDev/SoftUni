rows, cols = [int(el) for el in input().split(", ")]

matrix = []
result = 0
for row in range(rows):
    current_row_els = []
    for el in input().split(", "):
        current_row_els.append(int(el))
    matrix.append(current_row_els)
    result += sum(matrix[row])

print(result)
print(matrix)