# 1.9 Swap Without Temp
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
print(f"\nOriginal Values: a = {a}, b = {b}")
# Method 1: Tuple Swap
a, b = b, a
print(f"After Tuple Swap: a = {a}, b = {b}")
# Method 2: Arithmetic Swap
a = a + b
b = a - b
a = a - b
print(f"After Arithmetic Swap (back to original): a = {a}, b = {b}")
