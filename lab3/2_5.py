def permute(s, l, r):
    if l == r:
        print("".join(s)) 
    else:
        for i in range(l, r+1):
            s[l], s[i] = s[i], s[l]
            permute(s, l+1, r) 
            s[l], s[i] = s[i], s[l] 

def print_permutations():
    word = input()
    s = list(word)
    permute(s, 0, len(s) - 1)

print_permutations()
