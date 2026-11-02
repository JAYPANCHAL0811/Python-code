# 1.20 Star Pattern Collection
rows = 5

print("(a) Right-angled Triangle:")
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()

print("\n(b) Inverted Triangle:")
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

print("\n(c) Diamond Pattern:")
# Upper part
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()
# Lower part
for i in range(rows - 1, 0, -1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()