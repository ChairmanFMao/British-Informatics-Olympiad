# Problem was actualy much simpler than I made it, this function below was taken from someone else's solution and it works perfectly
# def fraction(promenade):
#     l, m = 1, 0
#     r, s = 0, 1

#     for i in range(len(promenade)):
#         if promenade[i]=="L":
#             l, m = l+r, s+m
#         else:
#             r, s = l+r, s+m

#     print(f"{l+r}/{m+s}")

def a():
    promenade = input()
    # (l+r) / (m+s), if r = 0, l = 1, m = 0, if l = 0, r= 0, s=1
    def calculate(l,r,m,s):
        top = l + r
        bottom = m + s
        for i in range(2,50):
            while top % i == 0 and bottom % i == 0:
                top /= i
                bottom /= i
        return [int(top),int(bottom)]

    prevl = [1,1]; prevr = [1,1]; current = []
    left = 0; right = 0
    for i in range(len(promenade)):
        if promenade[i] == "L":
            left = 1
            if len(current) > 0:
                prevr = current
            if not right:
                current = calculate(1,prevr[0],0,prevr[1])
            else:
                current = calculate(prevl[0],prevr[0],prevl[1],prevr[1])
        else:
            right = 1
            if len(current) > 0:
                prevl = current
            if not left:
                current = calculate(prevl[0],0,prevl[1],1)
            else:
                current = calculate(prevl[0],prevr[0],prevl[1],prevr[1])
    
    print(str(current[1]) + " / " + str(current[0]))

a()

"""
Part b:
I am just going to brute force combinations for lengths up to 10
Turns out that it didn't work well. Not sure what to do. Turns out my a program had a bug
I fixed a, so I will try again.

LRRR is the answer, careful to use the right values not wrong ones for follow ups
"""

def b():
    def check(promenade):
        def calculate(l,r,m,s):
            top = l + r
            bottom = m + s
            for i in range(2,50):
                while top % i == 0 and bottom % i == 0:
                    top /= i
                    bottom /= i
            return [int(top),int(bottom)]

        prevl = [1,1]; prevr = [1,1]; current = []
        left = 0; right = 0
        for i in range(len(promenade)):
            if promenade[i] == "L":
                left = 1
                if len(current) > 0:
                    prevr = current
                if not right:
                    current = calculate(1,prevr[0],0,prevr[1])
                else:
                    current = calculate(prevl[0],prevr[0],prevl[1],prevr[1])
            else:
                right = 1
                if len(current) > 0:
                    prevl = current
                if not left:
                    current = calculate(prevl[0],0,prevl[1],1)
                else:
                    current = calculate(prevl[0],prevr[0],prevl[1],prevr[1])
        
        return [current[1],current[0]]
    combos = []
    def generate(current):
        if len(current) <= 10:
            combos.append(current+"R")
            combos.append(current+"L")
            generate(current+"R")
            generate(current+"L")
        else:
            return
    
    generate("")
    for i in combos:
        if [4,5] == check(i):
            print(i)
            return

# b()

"""
Part c:
It is just 999999 L in a row with no R
"""

"""
Part d:
No, it isn't possilbe to get a promenade representing a negative fraction or number.
The process of generating a fraction from a promenade is additive so, it would be impossible
for a fraction that is generated by a promenade to be negative as the starting value for the
promenade is 1 from the fraction 1/1 numbers can only be added to either the top, bottom or 
both, therefore having the minimum number that you are able to create by asyptotic to 0.
However, the fraction will never become zero, and never be negative. Negative fraction must
have a negative numerator or denominator. Two non-negative numbers added together always has
to result in a non-negative number, there is no way a negative number can be formed during
the processing of a promenade.
"""