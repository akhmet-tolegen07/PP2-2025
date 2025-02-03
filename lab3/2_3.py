def solve(numheads, numlegs):
    c = (numlegs - numheads * 2) // 2
    r = numheads - c
    return c, r

c, r = solve(35, 94)

print(c, "chickens and", r, "rabbits")