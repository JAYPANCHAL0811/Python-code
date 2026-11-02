# 2.5 String Reverse & Palindrome
def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    cleaned_s = s.lower().replace(" ", "")
    return cleaned_s == reverse_string(cleaned_s)

test_strings = ["madam", "racecar", "Aarav", "Ahmedabad"]

for text in test_strings:
    rev = reverse_string(text)
    palindrome_flag = "Yes" if is_palindrome(text) else "No"
    print(f"String: '{text}' | Reversed: '{rev}' | Palindrome: {palindrome_flag}")