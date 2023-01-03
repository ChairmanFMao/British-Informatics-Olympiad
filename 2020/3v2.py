from functools import lru_cache

p, q, r = list(map(int,input().split()))
n = int(input()); n -= 1

# p letters of the alphabet
# streaks <= q
# length of r
# nth permutation
# print out the nth possible plan

# need to work out how many possibilities each of the
# letters you can choose at each stage has
# could probably do this with some kind of dp
# there is max value of r <= 12
# I kinda rushed it and it fails half the tests
# I just missed one else statement ;-;
# Solution still fails for some
# I was just missing another else statement I had used prior

@lru_cache(maxsize=None)
def dfs(left, streak):
    if streak > q:
        return 0
    if left <= 0:
        return 1
    return dfs(left-1,streak+1) + (p-1)*dfs(left-1,1)


out = ""; streak = 1; current = -1
for i in range(r):
    pos = 0
    for j in range(p):
        if n - dfs(r-i-1,streak+1 if j==current else 1) >= 0:
            n -= dfs(r-i-1,streak+1 if j==current else 1)
            pos += 1
        else:
            break

    out += chr(pos+65)
    if current == pos:
        streak += 1
    # This was my bug for a while ;-;
    else:
        streak = 1
    current = pos

#""" part a
print(out)
#"""

""" part b
Just write a brute force piece of code just like 4**8 or smth
then sort all of the possible ones
for CCA it is 39th
for CCABABCC it is 29947th

number = 1; length = 8; maxChar = 4; desired = "CCABABCC"; maxStreak = 2
def recur(current,streak):
    global length, number
    if len(current) >= length:
        if "".join([chr(i+65) for i in current]) == desired:
            print(number)
        number += 1
        return
    
    for i in range(maxChar):
        if streak < maxStreak and len(current) and i == current[-1]:
            current.append(i)
            recur(current,streak+1)
            current.pop()

        if not len(current) or (len(current) and i != current[-1]):
            current.append(i)
            recur(current,1)
            current.pop()

recur([],0)

"""

""" part c
If it is the same position in reverse order, it must be at the
middle of the order and there must be an odd number of plans.
This means that p must be odd

With help:
also, r <= q
these are the only conditions that lead to an odd number of plans
"""

