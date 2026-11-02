# 3.10 Duplicate Remover
nums_list1 = [10, 20, 30, 20, 40, 10, 50, 30, 60]
nums_list2 = [30, 40, 70, 80]

print(f"List 1: {nums_list1}")
print(f"List 2: {nums_list2}")

# (a) Remove duplicates using set
unique_list = list(set(nums_list1))
print(f"\n(a) Duplicates Removed (List 1): {unique_list}")

# (b) Elements in List 1 but not List 2
diff_elements = list(set(nums_list1) - set(nums_list2))
print(f"(b) In List 1 but not List 2   : {diff_elements}")

# (c) Count occurrences of each number in List 1
counts = {num: nums_list1.count(num) for num in set(nums_list1)}
print("(c) Element Occurrences (List 1):")
for num, count in sorted(counts.items()):
    print(f"    Element {num:2d} -> Appears {count} time(s)")