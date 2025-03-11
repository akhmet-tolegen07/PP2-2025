def count_case(s):
    upper_count = 0
    lower_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
    for char in s:
        if char.islower():
            lower_count += 1
    return upper_count, lower_count

text = input()
upper, lower = count_case(text)
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
