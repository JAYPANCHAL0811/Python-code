# Generating dictionaries using comprehension
numbers = [1, 2, 3, 4, 5]

# Squares dictionary
squares = {x: x**2 for x in numbers}
# Even squares only
even_squares = {x: x**2 for x in numbers if x % 2 == 0}

print("Squares:", squares)
print("Even Squares:", even_squares)