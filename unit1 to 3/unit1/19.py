# 1.19 Number Reversal & Palindrome
num = int(input("Enter a number: "))

original = num
reversed_num = 0

# Part (a): Reverse using while loop
temp = abs(num)
while temp > 0:
    digit = temp % 10
    reversed_num = (reversed_num * 10) + digit
    temp //= 10

if num < 0:
    reversed_num = -reversed_num

print(f"Reversed Number: {reversed_num}")

# Part (b): Check Palindrome
if original == reversed_num:
    print(f"{original} is a Palindrome.")
else:
    print(f"{original} is NOT a Palindrome.")


"""
# 1. Take input from the user
text = input("Enter a string: ")

# 2. Reverse the string using a simple loop
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text  # Adds each letter to the front

# 3. Compare original and reversed text
if text == reversed_text:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
"""