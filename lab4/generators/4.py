def square(a,b):
    f = []
    for i in range(a, b):
        f.append(i**2)
    return f
a = int(input())
b = int(input())
print(square(a,b))