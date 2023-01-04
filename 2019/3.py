from copy import deepcopy
from functools import lru_cache
from time import time

l, p = input().split()
l = int(l)

# Only condition is that there can't be 3 characters in ascending alphabetical order
# Definitely combinatorics
# Need the number of possible blockchains that begin with p
# Currently just doing a really simple bfs, slow for big inputs
# Ideally I don't want to be storing the strings and improve the efficiency of the valid algorithm
# Thinking of switching to a dfs for ease of implementation
# Switched to a dfs as it is faster, still doesn't handle the biggest inputs well
# This solution gets like 18/24, I have looked online and haven't really found an algorithm that
# works a lot faster for bigger inputs, all of them time out for the largest test case

# better O(n) complexity
def valid(s,toAdd):
    smallest = s[0]
    for i in range(len(s)):
        if s[i] < smallest:
            smallest = s[i]
        elif smallest < s[i] and s[i] < toAdd:
            return 0
    
    if smallest < toAdd:
        for i in range(len(used)):
            if not used[i] and toAdd < chr(i+65):
                return 0
    return 1

# This sets up the used list and characters that are possible to use
letters = "ABCDEFGHIJKLMNOPQRS"
alpha = letters[:l]
used = [0 for i in alpha]
for i in p:
    used[ord(i)-65] = 1

@lru_cache(maxsize=None)
def dfs(current):
    if len(current) == l:
        return 1
    out = 0
    for i in alpha:
        if not used[ord(i)-65]:
            used[ord(i)-65] = 1
            if valid(current,i):
                out += dfs(current + i)
            used[ord(i)-65] = 0
    return out

print(dfs(p))
