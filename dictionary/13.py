# Building a frequency counter dictionary
text = "apple banana apple cherry banana apple"
words = text.split()

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print("Word Frequencies:", freq)