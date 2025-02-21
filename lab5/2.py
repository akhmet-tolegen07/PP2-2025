import re

txt = input("Enter a string: ")
x = re.search(r"^ab{2,3}$", txt) 
if x:
    print("True")
else:
    print("False")
