def checkPat(current):
    if len(current) <= 1:
        return 1

    # get the minimum in the left and maximum in the right
    for i in range(1,len(current)):
        left = 1000; right = 0;
        for j in range(i):
            left = min(left,ord(current[j]))
        for j in range(i,len(current)):
            right = max(right,ord(current[j]))

        #print(current,current[0:i], current[i:])
        if left > right and checkPat(current[0:i][::-1]) and checkPat(current[i:][::-1]):
            return 1

    return 0

def convert(val):
    return "YES" if val else "NO"

""" part a
# I'm not sure if I've done this correctly
# I did manage to do this correctly, I identified the bug before
# testing it
s, t = input().split()
print(convert(checkPat(s)))
print(convert(checkPat(t)))
print(convert(checkPat(s+t)))
#"""

""" part b
from itertools import permutations
out = 0
for i in permutations("ABCD"):
    out += checkPat("".join(i))
    if checkPat("".join(i)):
        print("".join(i))

print(out)

# 5 are pats
# Needed to state them:
# BDCA CBDA CDAB DACB DBAC
#"""

""" part c
B has to be at the start
I think this only works when A is at the end
# I didn't manage to get the answer before checking
"""

