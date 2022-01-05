from typing import List


def a():
    fast1, fast2 = [int(i) for i in input().split()]

    hr1 = 0
    min1 = 0
    hr2 = 0
    min2 = 0

    while 1:
        min1 += fast1 + 60
        min2 += fast2 + 60
        hr1 += min1//60
        min1 %= 60
        hr2 += min2//60
        min2 %= 60
        hr1 %= 24
        hr2 %= 24
        if hr1 == hr2 and min1 == min2:
            break

    # Careful with formatting
    outh = str(hr1)
    outm = str(min1)
    if len(outh) == 1:
        outh = "0" + outh
    if len(outm) == 1:
        outm = "0" + outm
    print(outh + ":" + outm)

# a()

"""
Part b:
I am just going to check all the things, they have to not meet at 00:00
So:
0,8,9,16,18
"""

def b():
    for i in range(20):
        fast1 = 0
        fast2 = i

        hr1 = 0
        min1 = 0
        hr2 = 0
        min2 = 0

        while 1:
            min1 += fast1 + 60
            min2 += fast2 + 60
            hr1 += min1//60
            min1 %= 60
            hr2 += min2//60
            min2 %= 60
            hr1 %= 24
            hr2 %= 24
            if hr1 == hr2 and min1 == min2:
                break

        print(hr1,min1,i)

# b()

"""
Part c:
1440 hours
"""

def c():
    out = 0
    for fast1 in range(1440):
        if not fast1%50:
            print(fast1)
        for fast2 in range(fast1+1,1440):
            hr1 = 0
            min1 = 0
            hr2 = 0
            min2 = 0
            count = 0

            while 1:
                min1 += fast1 + 60
                min2 += fast2 + 60
                hr1 += min1//60
                min1 %= 60
                hr2 += min2//60
                min2 %= 60
                hr1 %= 24
                hr2 %= 24
                count += 1
                if hr1 == hr2 and min1 == min2:
                    break
            
            out = max(out,count)
    print(out)

c()