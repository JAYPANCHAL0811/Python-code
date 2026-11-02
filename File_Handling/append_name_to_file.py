with open("names.txt", "w") as opened_file:
    opened_file.write("Kavya\nRohan\n")
person_name = input("Enter another name: ")
with open("names.txt", "a") as opened_file:
    opened_file.write(person_name + "\n")
with open("names.txt", "r") as opened_file:
    print(opened_file.read())
