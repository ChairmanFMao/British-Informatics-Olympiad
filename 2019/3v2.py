l, p = input().split(); l = int(l)

# No 3 from left to right in ascending alphabetical order
# Just extending the current p to length l
# we use every letter once and get length l
# need to be to check if adding a character will change the length
# This code currently works but it is not very efficient
# need to do some kind of storing and effiencies
# if all of the prior used ones were greater then we can just
# kinda do it recursively
# we can use catalan numbers
# I think this now works
# It works for all except one case
# My code works but it is just too slow
# The catalan numbers bit provides a good speedup

from math import factorial as f

catalan = [(f(i+i)//(f(i)*f(i)))//(i+1) for i in range(21)]

def dfs(current, remaining):
    if not len(remaining):
        return 1

    left = len(remaining); val = 0
    while val in remaining:
        val += 1

    if val == left:
        return catalan[val]

    ret = 0
    for k in range(l):
        if not k in remaining:
            continue
        good = 1
        for i in range(len(current)):
            for j in range(i+1,len(current)):
                if current[i] < current[j] and current[j] < k:
                    good = 0
                    break
            if not good:
                break

        if good:
            current.append(k)
            remaining.remove(k)
            ret += dfs(current,remaining)
            remaining.add(k)
            current.pop()
    return ret

start = [ord(i)-65 for i in list(p)]; other = set()
for i in range(l):
    if i not in start:
        other.add(i)

print(dfs(start,other))

""" part b
BOI, IBO, IOB, OBI, OIB
"""

""" part c
first half -> MLKJIHGFEDCBA
second half -> ZYXWVUTSRQPON
Every character in the first half will be lower
than every character in the second half, so to make it such
that the combination is valid both need to be in decreasing order
"""

""" part d
first - ASRQPONMLKJIHGFEDCB
can use code from part A to get solutions for the second one
"""
