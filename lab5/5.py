import re

txt = input("Enter a string: ")
x = re.search("^a.*b$", txt)
if x:
    print("True")
else:
    print("False")
