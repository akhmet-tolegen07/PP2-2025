N = int(input())
G = (i**2 for i in range(N))
for i in range(N):
    print(next(G))