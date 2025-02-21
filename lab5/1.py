import re

txt = input("Enter a string: ")
x = re.search(r"^a.b*", txt)
if x:
    print("True")
else:
    print("False")