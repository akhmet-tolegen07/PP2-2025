def palindrome(s):
    s = s.replace(" ", "")
    s = s.lower()
    if  s == s[::-1]:
        return True
    else:
        return False


print(palindrome("madam"))
print(palindrome("apple"))
