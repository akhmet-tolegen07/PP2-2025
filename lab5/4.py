import re 

txt = input("Enter a string: ")
x = re.findall(r"[A-Z]+[a-z]+", txt)

print(x)