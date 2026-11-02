# 3.7 Set Operations Lab
set1 = {x for x in range(1, 16) if x % 2 != 0}   # Odd numbers 1-15
set2 = {x for x in range(1, 16) if x % 3 == 0}   # Multiples of 3 up to 15

print(f"Set 1 (Odds 1-15)         : {set1}")
print(f"Set 2 (Multiples of 3)     : {set2}")
print("-" * 50)
print(f"Union (Set1 | Set2)        : {set1 | set2}")
print(f"Intersection (Set1 & Set2) : {set1 & set2}")
print(f"Difference (Set1 - Set2)   : {set1 - set2}")
print(f"Difference (Set2 - Set1)   : {set2 - set1}")
print(f"Symmetric Difference       : {set1 ^ set2}")