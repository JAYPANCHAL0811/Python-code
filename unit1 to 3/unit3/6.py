# 3.6 Word Frequency Counter
import re

text = """
Python is an amazing programming language. Python is flexible, clean,
and python syntax is clean and readable.
"""

# Clean and tokenize words
words = re.findall(r'\b\w+\b', text.lower())

# Count frequency
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

# Sort by frequency (most common first)
sorted_freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)

print(f"{'Word':<15} | {'Frequency':<10}")
print("-" * 28)
for word, count in sorted_freq:
    print(f"{word:<15} | {count:<10}")