# 3.4 Multi-Return Function

def stats(a, b, c):
    total_sum = a + b + c
    avg = total_sum / 3.0
    minimum = min(a, b, c)
    maximum = max(a, b, c)
    return total_sum, avg, minimum, maximum

# Unpacking the returned tuple
s, a, mn, mx = stats(15, 42, 8)

print(f"Sum: {s}")
print(f"Average: {a:.2f}")
print(f"Minimum: {mn}")
print(f"Maximum: {mx}")
