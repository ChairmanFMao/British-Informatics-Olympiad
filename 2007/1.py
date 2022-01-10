from copy import deepcopy

def a():
    numbers = [int(i) for i in input().split()]
    score = 0

    used = []

    # This is function that generates permutations
    def permutations(current,left):
        if sum([numbers[i] for i in current]) == 15 and sorted(current) not in used:
            used.append(sorted(current))
            return 1
        
        out = 0
        for i in range(5):
            if i in left:
                copy = deepcopy(current)
                copy.append(i)
                leftcopy = deepcopy(left)
                leftcopy.remove(i)
                out += permutations(copy,leftcopy)
        return out

    # This creates a dictionary of how often each number occurs
    occurs = {}
    for i in numbers:
        if occurs.get(i) == None:
            occurs[i] = 0
        occurs[i] += 1

    # This adds to the score for pairs
    triangle = [0,0,1,3,6,10]
    for i in occurs.values():
        score += triangle[i]

    # This adds the sums to 15, we store the indexes of the numbers for ease
    score += permutations([],[i for i in range(5)])
    print(score)

a()

"""
Part b:
1 2 8 9 10
"""

"""
Part c:
There are 28 ways, read the question properly.
"""

def c():
    out = 0
    used = []
    for i in range(1,11):
        for j in range(1,11):
            for k in range(1,11):
                for l in range(1,11):
                    for m in range(1,11):
                        if sum([i,j,k,l,m]) == 15 and sorted([i,j,k,l,m]) not in used and len(set([i,j,k,l,m])) > 1:
                            used.append(sorted([i,j,k,l,m]))
                            out += 1
    print(out)

# c()
