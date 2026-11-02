# 1.7 Digit Extractor
num = int(input("Enter a 3-digit number: "))
hundreds = num // 100
tens = (num // 10) % 10
units = num % 10
digit_sum = hundreds + tens + units
digit_product = hundreds * tens * units
print(f"Hundreds Digit: {hundreds}")
print(f"Tens Digit: {tens}")
print(f"Units Digit: {units}")
print(f"Sum of Digits: {digit_sum}")
print(f"Product of Digits: {digit_product}")

