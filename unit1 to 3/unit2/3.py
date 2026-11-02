# 3.3 Factorial Function

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Printing table headers with left-alignment
# :<10
# : mean format start
#  < mean left alignment
#  10 mean 10 spaces

print(f"{'Number':<10} | {'Factorial':<15}")
print("-" * 28)

# Displaying factorials for numbers 1 to 10
for i in range(1, 11):
    print(f"{i:<10} | {factorial(i):<15}")
