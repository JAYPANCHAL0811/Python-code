try:
    input_number = int(input("Enter an integer: "))
except ValueError:
    print("Invalid input.")
else:
    print("Square:", input_number * input_number)
finally:
    print("Program finished.")
