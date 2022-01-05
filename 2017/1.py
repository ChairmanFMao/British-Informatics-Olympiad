# Part a
def a():
    start = list(input())

    while len(start) > 1:
        end = []
        for i in range(len(start)-1):
            if (start[i] == start[i+1]):
                end.append(start[i])
                continue
            valid = ["R","G","B"]
            valid.remove(start[i])
            valid.remove(start[i+1])
            end.append(valid[0])
        start = end

    print(start[0])

possible = []
length = 0
def generatePossible(current):
    if len(current) == length:
        possible.append(current)
        return
    generatePossible(current + "R")
    generatePossible(current + "G")
    generatePossible(current + "B")

a()
# Part b
# RRRBBGGRG
# GBGGRRBBB
# BGBRGBRGR
# Made my own permutation function when I got annoyed with itertools
def b():
    global possible
    global length
    length = 9
    generatePossible("")
    starting = 0
    for start in possible:
        end = ""
        for i in range(len(start)-1):
            if (start[i] == start[i+1]):
                end += start[i]
                continue
            valid = ["R","G","B"]
            valid.remove(start[i])
            valid.remove(start[i+1])
            end += valid[0]
        
        if end == "RRGBRGBB":
            print("".join(start))
            starting += 1
    
    print(starting)

# Part c
# Unsure of how to do this, it is a justify question
# Answer is actually just one as the smallest row is completely known
# and by induction you can complete all of the higher rows

# Part d
# I am just going to test part a with different sized things
# Actually I am going to take a break and resume this tomorrow,
# I wanna finish this question as well as the aoc tomorrow.
# For now I just wanna relax, it's christmas eve after all.
# I think that the answer for this is 10, be careful