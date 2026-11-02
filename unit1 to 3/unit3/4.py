# 3.4 Tuple Operations
marks = (85, 92, 78, 65, 90)

print(f"Original Tuple: {marks}")
print(f"Indexing (First Element): {marks[0]}")
print(f"Slicing (Middle 3)      : {marks[1:4]}")
print(f"Length                  : {len(marks)}")

# Demonstrating Immutability (TypeError)
print("\nAttempting to modify tuple element:")
try:
    marks[0] = 95
except TypeError as e:
    print(f"  TypeError caught successfully: {e}")

# Modifying via List conversion
temp_list = list(marks)
temp_list[0] = 95
marks = tuple(temp_list)
print(f"Tuple after modification via List conversion: {marks}")