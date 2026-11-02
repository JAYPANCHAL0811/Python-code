# 2.1 Function Basics
def greet(name):
    print(f"Hello, {name}! Welcome to the course.")

def square(n):
    return n ** 2

def cube(n):
    return n ** 3

# Calling each function 3 times with different values
print("--- Greet Calls ---")
greet("Alice")
greet("Bob")
greet("Charlie")

print("\n--- Square Calls ---")
print(f"Square of 4: {square(4)}")
print(f"Square of 7: {square(7)}")
print(f"Square of 12: {square(12)}")

print("\n--- Cube Calls ---")
print(f"Cube of 2: {cube(2)}")
print(f"Cube of 3: {cube(3)}")
print(f"Cube of 5: {cube(5)}")