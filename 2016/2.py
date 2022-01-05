# Very happy with my solution for a, it works very quickly now after reseting check on each step

def a():
    p, s, n = [int(i) for i in input().split()]
    sq = [int(i) for i in input().split()]
    ptr = 0
    p -= 1

    people = dict()
    for i in range(n):
        check = []
        check.append([p//5,p%5])
        if people.get((p//5,p%5)) == None:
            people[(p//5,p%5)] = 0
        people[(p//5,p%5)] += 1
        while 1:
            start = len(check)
            for j in range(len(check)):
                if people[(check[j][0],check[j][1])] >= 4:
                    if people.get((check[j][0]-1,check[j][1])) == None:
                        people[(check[j][0]-1,check[j][1])] = 0
                    if people.get((check[j][0]+1,check[j][1])) == None:
                        people[(check[j][0]+1,check[j][1])] = 0
                    if people.get((check[j][0],check[j][1]-1)) == None:
                        people[(check[j][0],check[j][1]-1)] = 0
                    if people.get((check[j][0],check[j][1]+1)) == None:
                        people[(check[j][0],check[j][1]+1)] = 0
                    people[(check[j][0]-1,check[j][1])] += 1
                    people[(check[j][0]+1,check[j][1])] += 1
                    people[(check[j][0],check[j][1]-1)] += 1
                    people[(check[j][0],check[j][1]+1)] += 1
                    check.append((check[j][0]-1,check[j][1]))
                    check.append((check[j][0]+1,check[j][1]))
                    check.append((check[j][0],check[j][1]-1))
                    check.append((check[j][0],check[j][1]+1))
                    people[(check[j][0],check[j][1])] -= 4
            if start == len(check):
                break
        p = (p + sq[ptr%len(sq)]) % 25
        ptr += 1

    for i in range(5):
        for j in range(5):
            if people.get((i,j)) == None:
                print("0", end = " ")
            else:
                print(people[(i,j)], end = " ")
        print("\n",end="")

a()

"""
Part b:
The smallest number of people to be added is 16 all on one square in a corner or side square as this would
lead to there being 4 people migrating out onto the same square and then out of these 4, one person will
move back into the square again due to overcrowding.
"""

"""
Part c:
Considering brute force here, complexity would roughly be, 24^3 * 25 * normal runtime
According to other solution it seems like brute force is the way to go for these
Remember that partial answers get partial marks sometimes
One example for this would be:
8 3 8
3 5 2
"""

"""
Part d:
No, due to migrations it would be impossible to know which squares have had migrations and which didn't
leading to the problem that it would be impossible to backtrack these migrations making it impossible for
you to determine the original landscape. Some combinations of starting landscape and position lead to the
same final landscape. If migrations have occurred and at least one person remains on the given position,
it is also possible that no migrations occured and a person was placed in that position.
"""