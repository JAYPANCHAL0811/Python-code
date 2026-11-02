try:
    num_one = int(input("Enter first number: "))
    num_two = int(input("Enter second number: "))
    print("Result:", num_one / num_two)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Please enter integers only.")
