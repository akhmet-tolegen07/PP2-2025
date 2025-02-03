def palindrome(s):
    s = s.replace(" ", "").lower()
    if  s == s[::-1]:
        return True
    else:
        return False


print(palindrome("madam"))
print(palindrome("apple"))
