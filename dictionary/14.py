# Reading and updating nested values
students = {
    "S101": {"name": "Aarav", "grade": "A"},
    "S102": {"name": "Diya", "grade": "B"}
}

# Read nested item
print("S101 Name:", students["S101"]["name"])

# Update nested item
students["S102"]["grade"] = "A+"
print("Updated S102:", students["S102"])