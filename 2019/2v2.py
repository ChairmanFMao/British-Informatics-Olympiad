from collections import deque

t, instructions, m = input().split(); t = int(t); m = int(m)

# attempts to move after every instruction
# I managed to code this so much nicer than last time

# NESW
dy = (1,0,-1,0)
dx = (0,1,0,-1)

pos = [0,0]; d = 0

seen = dict()
q = deque()

for i in range(m):
    current = instructions[i%len(instructions)]
    if current == "R":
        d = (d+1)%4
    if current == "L":
        d = (d-1+4)%4

    q.append(tuple(pos))
    seen[tuple(pos)] = 1

    turns = 0
    while turns < 4:
        if seen.get((pos[0]+dy[d],pos[1]+dx[d])) == 1:
            turns += 1
            d = (d+1)%4
            continue
        else:
            pos[0] += dy[d]
            pos[1] += dx[d]
            break

    if turns >= 4:
        break

    while len(q) > t:
        del seen[q.popleft()]

#""" part a
print("("+str(pos[1])+","+str(pos[0])+")")
#"""

""" part b
grid = [[0 for i in range(10)] for j in range(10)]

for i in q:
    grid[i[0]+5][i[1]+5] = 1

for i in range(9,-1,-1):
    print(grid[i])

this can just be done by printing out the trail
I actually needed to go one move further to get the right grid
also I had to flip the grid
[0, 0, 0, 0, 0, 1, 1, 1, 0, 0]
[0, 0, 0, 0, 1, 1, 0, 1, 0, 0]
[0, 0, 0, 0, 1, 0, 0, 1, 0, 0]
"""

""" part c
This should be 440 the explorer would just go in a circle
"""

""" part d
just set a limit for infinity at like 1e5 and could even binary
search the answer
function is actually not monotonic so, a binary search doesn't
work

instructions = "LLRFFF"
for j in range(1,10000):
    good = 1
    dy = (1,0,-1,0)
    dx = (0,1,0,-1)

    pos = [0,0]; d = 0

    seen = dict()
    q = deque()

    for i in range(int(1e5)):
        current = instructions[i%len(instructions)]
        if current == "R":
            d = (d+1)%4
        if current == "L":
            d = (d-1+4)%4

        q.append(tuple(pos))
        seen[tuple(pos)] = 1

        turns = 0
        while turns < 4:
            if seen.get((pos[0]+dy[d],pos[1]+dx[d])) == 1:
                turns += 1
                d = (d+1)%4
                continue
            else:
                pos[0] += dy[d]
                pos[1] += dx[d]
                break

        if turns >= 4:
            good = 0
            break

        while len(q) > j:
            del seen[q.popleft()]

    if good:
        print(j)

1561 is what I got initially with a binary search
but this is wrong because a binary search doesn't work
I tried it again with a linear search but I got values higher
than it
"""

