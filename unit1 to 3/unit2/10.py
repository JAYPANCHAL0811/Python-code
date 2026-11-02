# 3.10 Report Card with f-strings

student_name = "Alex Morgan"
roll_no = 20261012
marks = [85, 92, 78, 88, 95]

total = sum(marks)
percentage = total / len(marks)

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
else:
    grade = "C"

print("=" * 40)
print(f"{'STUDENT REPORT CARD':^40}")
print("=" * 40)
print(f"Name   : {student_name:<25}")
print(f"Roll No: {roll_no:<25}")
print("-" * 40)

# Loop with auto-incrementing index numbers
for idx, mark in enumerate(marks, start=1):
    print(f"Subject {idx} Marks : {mark:>5}")

print("-" * 40)
print(f"Total Marks     : {total:>5} / 500")
print(f"Percentage      : {percentage:>5.2f}%")
print(f"Grade Obtained  : {grade:>5}")
print("=" * 40)
