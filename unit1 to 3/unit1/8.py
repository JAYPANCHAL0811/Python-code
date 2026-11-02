# 1.8 Unit Converter
km = float(input("Enter distance in kilometres: "))
metres = km * 1000
centimetres = km * 100000
miles = km * 0.621371
feet = km * 3280.84

print(f"Metres: {metres:.2f} m")
print(f"Centimetres: {centimetres:.2f} cm")
print(f"Miles: {miles:.4f} mi")
print(f"Feet: {feet:.2f} ft")
