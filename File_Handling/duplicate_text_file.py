with open("source.txt", "w") as opened_file:
    opened_file.write("Welcome to the Python programming lab session.")
with open("source.txt", "r") as opened_file:
    message_text = opened_file.read()
with open("copy.txt", "w") as opened_file:
    opened_file.write(message_text)
print("File copied successfully.")
