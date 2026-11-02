# 1.3 Simple Interest Calculator
P = float(input("Enter Principal amount (P): "))
R = float(input("Enter Rate of Interest (R): "))
T = float(input("Enter Time in years (T): "))
SI = (P * R * T) / 100
total_amount = P + SI
print(f"Simple Interest: {SI:.2f}")
print(f"Total Amount: {total_amount:.2f}")
