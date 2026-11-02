# 1.6 Salary Calculator
basic_salary = float(input("Enter basic salary: "))
hra = 0.20 * basic_salary
da = 0.10 * basic_salary

pf = 0.12 * basic_salary
gross_salary = basic_salary + hra + da
net_salary = gross_salary - pf
print(f"HRA: {hra:.2f}")
print(f"DA: {da:.2f}")
print(f"PF Deduction: {pf:.2f}")
print(f"Gross Salary: {gross_salary:.2f}")
print(f"Net Salary: {net_salary:.2f}")
