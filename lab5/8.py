import re

txt = input("Enter a string: ")
x = re.split(r"[A-Z]", txt)
print(x)
