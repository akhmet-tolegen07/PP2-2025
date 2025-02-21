import re

txt = input("Enter a string: ")
x = re.sub(r"[,.]|\s", ":", txt)
print(x)
