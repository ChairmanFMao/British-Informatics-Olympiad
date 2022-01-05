from math import factorial
from functools import lru_cache
a, b, c, d, n = [int(i) for i in input().split()]
# 1 <= n <= 2^34, this means that I can't manualy generate all the combos as it will just be too big
# Roughly like 16 billion combinations max
# Was kinda stuck so, I read through a guide for the thought process
# This is just a constructive algorithm to make the string
# You cna determine how many combinations a choice will give you down the line with the permutations lambda
# Relied on help to solve this problem, need to solve more combinatorics I think

# This gets the total number of permutations possible,
# This is very clever and it was the main thing that I was missing in my thought process 
permutations = lambda a, b, c, d: int(factorial(a+b+c+d)/(factorial(a)*factorial(b)*factorial(c)*factorial(d)))

@lru_cache(maxsize=None)
def solve(a, b, c, d, k):
    total = 0
    if a > 0:
        total += permutations(a-1,b,c,d)
        if k <= total:
            return "A" + solve(a-1,b,c,d,k-total+permutations(a-1,b,c,d))
    if b > 0:
        total += permutations(a,b-1,c,d)
        if k <= total:
            return "B" + solve(a,b-1,c,d,k-total+permutations(a,b-1,c,d))
    if c > 0:
        total += permutations(a,b,c-1,d)
        if k <= total:
            return "C" + solve(a,b,c-1,d,k-total+permutations(a,b,c-1,d))
    if d > 0:
        total += permutations(a,b,c,d-1)
        if k <= total:
            return "D" + solve(a,b,c,d-1,k-total+permutations(a,b,c,d-1))
    return ""

print(solve(a,b,c,d,n))