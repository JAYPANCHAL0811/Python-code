with open("sentence.txt", "w") as opened_file:
    opened_file.write("Regular practice makes programming concepts easier to understand")
with open("sentence.txt", "r") as opened_file:
    message_text = opened_file.read()
word_list = message_text.split()
print("Number of words:", len(word_list))
