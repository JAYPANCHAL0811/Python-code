# Vowel Counter & Character Frequency

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0

    for char in s:
    # for char in s(paramter: given input)
        if char in vowels:
        #  if char in vowels
            count += 1
            # make 0 += 1 increament by 1

    return count
    # return given count

# ------------------------- check occurrence of characters
def char_frequency(s):
    freq = {}
    # empty dictonary

    for char in s:
    # for char in s(paramter: given input)
        if char in freq:
        # if char in looped dictonary
            freq[char] += 1
            # If yes, increase its count by 1 
        else:
            freq[char] = 1
            # Add the character with an initial count of 1

    return freq


sentence = "momo"

print("Sentence:", sentence)
print("Total Vowels:", count_vowels(sentence))
print("Character Frequency:", char_frequency(sentence))