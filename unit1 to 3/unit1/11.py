# 1.11 Percentage Calculator
m1 = float(input("Enter marks for Subject 1: "))
m2 = float(input("Enter marks for Subject 2: "))
m3 = float(input("Enter marks for Subject 3: "))
m4 = float(input("Enter marks for Subject 4: "))
m5 = float(input("Enter marks for Subject 5: "))
total = m1 + m2 + m3 + m4 + m5
percentage = (total / 500.0) * 100
average = total / 5.0
print(f"\nTotal Marks: {total:.2f}/500")
print(f"Percentage: {percentage:.2f}%")
print(f"Average Marks: {average:.2f}")
