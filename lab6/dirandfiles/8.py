import os
p=(r"C:\Users\Asus\Desktop\PP2-2025\lab6\dirandfiles\delete.txt")
if os.path.exists(p):
    os.remove(p)
else:
    print("this file does not exist")