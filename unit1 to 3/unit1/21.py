# 1.21 Armstrong Number Finder
# Part (a): Check single number
num = int(input("Enter a number: "))
order = len(str(num))
temp = num
sum_pow = 0

while temp > 0:
    digit = temp % 10
    sum_pow += digit**order
    temp //= 10

if num == sum_pow:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is NOT an Armstrong number.")

# Part (b): Armstrong numbers between 1 and 999
print("\nArmstrong numbers between 1 and 999:")
for i in range(1, 1000):
    p_order = len(str(i))
    t = i
    s = 0
    while t > 0:
        d = t % 10
        s += d**p_order
        t //= 10
    if i == s:
        print(i, end=" ")
print()