file_path = input("Enter a file name: ")
try:
    with open(file_path, "r") as opened_file:
        print(opened_file.read())
except FileNotFoundError:
    print("File does not exist.")
