# 3.7 Modular Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed!"

def power(a, b):
    return a ** b

def calculator():
    print(" --- Modular Calculator ---")
    print("1. Add | 2. Subtract | 3. Multiply | 4. Divide | 5. Power | 6. Exit")
    
    choice = input("Enter choice (1-6): ")
    
    if choice == '6':
        print("Exiting Calculator.")
        return
        
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == '1':
        print(f"Result: {add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Result: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"Result: {divide(num1, num2)}")
    elif choice == '5':
        print(f"Result: {power(num1, num2)}")
    else:
        print("Invalid Choice!")

# Example execution call
calculator()
