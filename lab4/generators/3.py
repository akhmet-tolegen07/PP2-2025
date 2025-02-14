def filtered(n):
    f = []
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0:
            f.append(i)
    return f

n = int(input())
mylist = filtered(n)

print(mylist)