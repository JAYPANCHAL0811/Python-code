# 3.9 Anagram Checker
# contains exact same words(chars)
# apple
# a p p l e

# pappl
# p a p p l
def is_anagram(s1, s2):
    # Convert both strings to lowercase and remove spaces
    str1 = s1.lower().replace(" ", "")
    str2 = s2.lower().replace(" ", "")
    
    # Sort the characters of both strings and compare them
    return sorted(str1) == sorted(str2)

pairs = [
    ("listen", "silent"),
    ("triangle", "integral"),
    ("apple", "pappl"),
    ("hello", "world")
]
"""
Index 0 → ("listen", "silent")
Index 1 → ("triangle", "integral")
Index 2 → ("apple", "pappl")
Index 3 → ("hello", "world")
"""

for s1, s2 in pairs:
# Python goes through each tuple one by one.
    result = "Anagrams" if is_anagram(s1, s2) else "Not Anagrams"
    """
    same as:
    if is_anagram(s1, s2):
        result = "Anagrams"
    else:
        result = "Not Anagrams"
    """
    print(f"'{s1:<9}' and '{s2:<9}' -> {result}")
