import re 

txt = input("Enter a string: ")
x = re.findall(r"[a-z]+_[a-z]+", txt)

print(x)