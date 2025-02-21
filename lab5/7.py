import re

def x(txt):
    words = txt.split('_')
    camel= words[0]
    for char in words[1:]:
        camel += char.capitalize()
    return camel

txt = input("Enter a string: ")
print(x(txt))