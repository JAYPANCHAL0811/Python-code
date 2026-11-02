# 1.10 BMI Calculator
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in metres: "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi <= 24.9:
    category = "Normal"
elif 25 <= bmi <= 29.9:
    category = "Overweight"
else:
    category = "Obese"
print(f"BMI: {bmi:.2f}")
print(f"Category: {category}")
