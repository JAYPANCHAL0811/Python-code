# 1.13 Number Classifier
num = float(input("Enter a number: "))

# (a) Positive/Negative/Zero
if num > 0:
    pos_neg = "Positive"
elif num < 0:
    pos_neg = "Negative"
else:
    pos_neg = "Zero"

# (b) Even or Odd
even_odd = "Even" if num % 2 == 0 else "Odd"

# (c) Divisible by 5
div_by_5 = "Divisible by 5" if num % 5 == 0 else "Not divisible by 5"

print(f"Result: {pos_neg}, {even_odd}, {div_by_5}")