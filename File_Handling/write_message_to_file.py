message_text = input("Enter a message: ")
with open("message.txt", "w") as opened_file:
    opened_file.write(message_text)
print("Message saved.")
