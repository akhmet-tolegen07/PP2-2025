def is_palindrome(s):
    return s == s[::-1]

word = input()
print(f"Is '{word}' a palindrome?", is_palindrome(word))
