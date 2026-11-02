# 1.23 Sum of Series
N = int(input("Enter N: "))

sum_natural = 0
sum_squares = 0
sum_cubes = 0

for i in range(1, N + 1):
    sum_natural += i
    sum_squares += i**2
    sum_cubes += i**3

print(f"Sum of first {N} natural numbers: {sum_natural}")
print(f"Sum of squares of first {N} natural numbers: {sum_squares}")
print(f"Sum of cubes of first {N} natural numbers: {sum_cubes}")