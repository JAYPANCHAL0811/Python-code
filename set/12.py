# Generating sets using comprehensions
numbers = range(1, 11)

even_squares = {x**2 for x in numbers if x % 2 == 0}
print("Even Squares Set:", even_squares)