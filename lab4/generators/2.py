def evens(n):
    f = []
    for i in range(n):
        if i % 2 == 0:
            f.append(i)
    return f

n = int(input())
mylist = evens(n)

print(mylist)