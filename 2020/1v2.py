# Need to practice doing the follow ups as well

def toRoman(a:int):
    out = ""
    vals = [[1000,"M"],[900,"CM"],[500,"D"],[400,"CD"],[100,"C"],
            [90,"XC"],[50,"L"],[40,"XL"],[10,"X"],[9,"IX"],
            [5,"V"],[4,"IV"],[1,"I"]]
    while a:
        for i in vals:
            if a >= i[0]:
                a -= i[0]
                out += i[1]
                break

    return out

def lookAndSay(current, n):
    for i in range(n):
        nextVal = ""

        ptr = 0; character = current[0]; streak = 0
        while ptr < len(current):
            if current[ptr] == character:
                streak += 1
            else:
                nextVal += toRoman(streak) + character
                character = current[ptr]
                streak = 1
            ptr += 1

        nextVal += toRoman(streak) + character

        current = nextVal

    #""" part a
    print(current.count("I"),current.count("V"))
    #"""

    """ part c
    return current
    #"""

#""" part a
start, num = input().split()
num = int(num)
lookAndSay(start,num)
#"""

""" part b - just did these all manually
I -> II
II -> III
V -> IV
X -> IX
should state that there are 4
"""

""" part c - 3759
I got 3919(correct answer) after debugging my toRoman code
the bug didn't effect part a
seen = set()
for i in range(1,4000):
    seen.add(lookAndSay(toRoman(i),1))

print(len(seen))

#answer I got for this was wrong initally
#"""

