from functools import lru_cache

# This implementation in python is just slightly slower than the Cpp one, I think that the algorithm is the problem honestly

permutations = 0

@lru_cache(maxsize=None)
def generatePermutations(built, remaining, last2):
    global permutations
    if (len(remaining) == 0):
        permutations+=1
    for i in range(len(remaining)):
        if (chr(ord(last2[0]) + 1) != last2[1] and last2[1] != remaining[i]):
            generatePermutations(built + remaining[i], remaining[:i] + remaining[i+1:], last2[1]+remaining[i])

def solve():
    l, p = input().split()

    l = int(l)
    pCopy = p
    left = ""
    charsInP = set()
    for i in range(len(p)):
        charsInP.add(p[i])
    for i in range(l):
        if (chr(i + 65) not in charsInP):
            left += chr(i + 65)

    while len(p) < 2:
        p = " " + p
    generatePermutations(pCopy, left, p)
    
    print(permutations)

solve()