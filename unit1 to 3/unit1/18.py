# 1.18 Fibonacci Series
n_terms = int(input("Enter the number of terms: "))

a, b = 0, 1
count = 0

print("Fibonacci Series:")
while count < n_terms:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
print()