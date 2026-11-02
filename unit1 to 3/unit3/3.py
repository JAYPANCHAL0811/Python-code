# 3.3 List Comprehension Lab

# (a) Squares of 1-20
squares = [x**2 for x in range(1, 21)]

# (b) Even numbers 1-50
evens = [x for x in range(1, 51) if x % 2 == 0]

# (c) Words longer than 4 characters
sentence = "Python list comprehension makes writing clear and readable code easy"
long_words = [word for word in sentence.split() if len(word) > 4]

# (d) Cubes of odd numbers 1-15
odd_cubes = [x**3 for x in range(1, 16) if x % 2 != 0]

print(f"(a) Squares (1-20)     : {squares}")
print(f"(b) Evens (1-50)       : {evens}")
print(f"(c) Words > 4 chars    : {long_words}")
print(f"(d) Odd Cubes (1-15)   : {odd_cubes}")