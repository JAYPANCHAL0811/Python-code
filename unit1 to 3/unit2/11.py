# 3.11 Default Parameter Function

def display_info(name, city="Ahmedabad", programme="M.Sc. IT"):
    print(f"Name: {name:<10} | City: {city:<10} | Programme: {programme}")

print("(a) Calling with all 3 arguments:")
display_info("John Doe", "Mumbai", "M.Tech")

print("\n(b) Calling with only 'name':")
display_info("Alex")

print("\n(c) Calling with 'name' and 'city':")
display_info("Priya", "Surat")
