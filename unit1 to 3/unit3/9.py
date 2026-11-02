# 3.9 Student Gradebook
gradebook = {
    "Alice": [88, 92, 95],
    "Bob": [70, 65, 80],
    "Charlie": [90, 94, 89],
    "David": [82, 85, 88]
}

# Calculate averages
averages = {student: sum(marks) / len(marks) for student, marks in gradebook.items()}

# Sort by average (highest first)
sorted_gradebook = sorted(averages.items(), key=lambda x: x[1], reverse=True)

print(f"{'Student Name':<15} | {'Average Mark':<12}")
print("-" * 32)
for student, avg in sorted_gradebook:
    print(f"{student:<15} | {avg:<12.2f}")

top_student = sorted_gradebook[0]
print("-" * 32)
print(f"Top Student: {top_student[0]} with Average: {top_student[1]:.2f}")