# 1.16 Factorial Finder
n = int(input("Enter a non-negative integer: "))
fact = 1

if n < 0:
    print("Factorial does not exist for negative numbers.")
else:
    for i in range(1, n + 1):
        fact *= i
    print(f"{n}! = {fact}")