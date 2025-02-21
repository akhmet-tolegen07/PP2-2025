import re

txt = input("Enter a string: ")
x = re.sub(r"([A-Z])", r" \1", txt)
print(x)
