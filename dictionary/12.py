# Sorting dictionary items by keys and values
marks = {"Rahul": 85, "Aniket": 92, "Bhavik": 78}

# Sort by keys
sorted_by_key = dict(sorted(marks.items()))
# Sort by values descending
sorted_by_val = dict(sorted(marks.items(), key=lambda item: item[1], reverse=True))

print("Sorted by Name:", sorted_by_key)
print("Sorted by Marks (Desc):", sorted_by_val)