# 3.5 Phone Book
phone_book = {}

# (a) Add 5 contacts
phone_book["Alice"] = "9876543210"
phone_book["Bob"] = "8765432109"
phone_book["Charlie"] = "7654321098"
phone_book["David"] = "6543210987"
phone_book["Eva"] = "5432109876"

# (b) Search by name
search_name = "Charlie"
print(f"Search '{search_name}': {phone_book.get(search_name, 'Not Found')}")

# (c) Update a number
phone_book["Alice"] = "9998887770"
print(f"Updated Alice's number: {phone_book['Alice']}")

# (d) Delete a contact
deleted = phone_book.pop("David", None)
print(f"Deleted contact 'David': {deleted}")

# (e) Display all contacts sorted by name
print("\nContacts sorted by name:")
for name in sorted(phone_book.keys()):
    print(f"  {name:<10} : {phone_book[name]}")