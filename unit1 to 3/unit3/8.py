# 3.8 2D Matrix (Nested List)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# (a) Display in tabular format
print("3x3 Matrix:")
for row in matrix:
    print(" ".join(f"{val:3d}" for val in row))

# (b) Calculate sum of each row
print("\nRow Sums:")
for idx, row in enumerate(matrix, start=1):
    print(f"  Row {idx} Sum: {sum(row)}")

# (c) Calculate sum of main diagonal
diagonal_sum = sum(matrix[i][i] for i in range(len(matrix)))
print(f"\nMain Diagonal Sum: {diagonal_sum}")