import math
# 1.5 Area & Perimeter
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))
rect_area = length * breadth
rect_perimeter = 2 * (length + breadth)
circle_area = math.pi * (length ** 2)
print(f"Rectangle Area: {rect_area:.2f}")
print(f"Rectangle Perimeter: {rect_perimeter:.2f}")
print(f"Circle Area (Radius = {length}): {circle_area:.2f}")
