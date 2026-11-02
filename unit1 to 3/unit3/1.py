# 3.1 List Statistics
numbers = [23, 89, 12, 45, 67, 90, 34]

print(f"(a) Original List : {numbers}")
print(f"(b) Sorted List   : {sorted(numbers)}")
print(f"(c) Reversed List : {list(reversed(numbers))}")
print(f"(d) Maximum       : {max(numbers)}")
print(f"(e) Minimum       : {min(numbers)}")
print(f"(f) Sum           : {sum(numbers)}")
print(f"(g) Average       : {sum(numbers) / len(numbers):.2f}")