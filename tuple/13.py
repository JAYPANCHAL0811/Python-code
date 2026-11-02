s = input("Enter String: ")

new = ""

for ch in s:

    if ch == 'o':
        new += "@"

    else:
        new += ch

print(new)