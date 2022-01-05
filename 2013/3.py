from copy import deepcopy
from itertools import permutations
from sys import exit

s = input()

# 0 for off, 1 for dim, 2 for bright
grid = [[0 for j in range(5)] for i in range(5)]
# Keeps track of how many times buttons have been pressed
presses = [[0 for j in i] for i in grid]

# Updates the grid according to s
for i in range(len(s)):
    grid[(ord(s[i].upper())-65)//5][(ord(s[i].upper())-65)%5] = 2 if s[i].isupper() else 1

# Function to press a button at co ordinates x,y and all of the buttons next to it
def press(y,x,g,p):
    p[y][x] += 1
    g[y][x] = (g[y][x] + 1) % 3
    if y > 0:
        g[y-1][x] = (g[y-1][x] + 1) % 3
    if y < 4:
        g[y+1][x] = (g[y+1][x] + 1) % 3
    if x > 0:
        g[y][x-1] = (g[y][x-1] + 1) % 3
    if x < 4:
        g[y][x+1] = (g[y][x+1] + 1) % 3
    return [g, p]

# Checks if the system is unlocked and if so, it will ouput the string needed to unlock it
def done(grid, presses):
    if sum(sum([j for j in i]) for i in grid) == 0:
        out = ""
        for i in range(5):
            for j in range(5):
                if presses[i][j] == 1:
                    out += chr(65 + i*5 + j).lower()
                if presses[i][j] == 2:
                    out += chr(65 + i*5 + j)
        print(out)
        exit(0)

def finish(board, used):
    for i in range(5,25):
        y = i // 5
        x = i % 5
        while board[y-1][x] != 0:
            board, used = press(y,x,board,used)
    return board, used

# Debugging function
def printGrid():
    for i in grid:
        for j in i:
            print(j,end='')
        print()
    print()

# This uses the observation that there is always at least one solution where the top row characters
# are pressed no more than once.
for i in range(6):
    for start in permutations("abcde",i):
        used = deepcopy(presses)
        board = deepcopy(grid)
        for letter in start:
            board, used = press(0, ord(letter)-97, board, used)
        board, used = finish(board,used)
        done(board, used)

print("IMPOSSIBLE")

# Ideas:
# Just the top row is what matters
# All of the other rows can be made to fit in with it
# Then if the bottom row is all zero, the top row works and we are epicly winning
# Strategy:
# Change the top row to every combination possible
# There is always at least one solution where the "abcde" are all lowercase
# You can fix the row above using the row beneath always
# Test every single top row combination and if the bottom row combination
# ends up working out, that is a solution

"""
Part b:
1 1 1 1 0
0 1 1 1 2
0 0 0 2 1
0 0 0 0 1
0 0 0 0 0
"""