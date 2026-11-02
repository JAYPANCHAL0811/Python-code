# 3.12 Lambda Sort

students = [("Alice", 75), ("Bob", 45), ("Charlie", 92), ("Diana", 58), ("Ethan", 84)]

# Sort by marks descending using lambda
sorted_students = sorted(students, key=lambda student: student[1], reverse=True)

print("Students sorted by marks (Descending):")
for name, marks in sorted_students:
    print(f"  {name:<8}: {marks}")

# Filter students with marks >= 60 using lambda
passed_students = list(filter(lambda student: student[1] >= 60, sorted_students))

print("\nStudents with marks >= 60:")
for name, marks in passed_students:
    print(f"  {name:<8}: {marks}")
