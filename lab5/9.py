import re

txt = input("Enter a string: ")
x = re.sub(r"([A-Z])([A-Z])", r" \1 \2", txt)
print(x)
