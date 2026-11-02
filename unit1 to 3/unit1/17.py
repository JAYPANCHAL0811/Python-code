# 1.17 Prime Number Checker & List
# Part (a): Check single number
num = int(input("Enter a number to check prime: "))
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{num} is a Prime number.")
else:
    print(f"{num} is NOT a Prime number.")

# Part (b): List all primes from 2 to N
N = int(input("\nEnter N to print primes up to N: "))
print(f"Prime numbers between 2 and {N}:")
for val in range(2, N + 1):
    flag = True
    for i in range(2, int(val**0.5) + 1):
        if val % i == 0:
            flag = False
            break
    if flag:
        print(val, end=" ")
print()