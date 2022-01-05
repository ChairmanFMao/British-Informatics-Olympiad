pos1, mod1, pos2, mod2, turns = [int(i) for i in input().split()]
# X for player 1 and O for player2
# This is for our modulo 36 system to work
pos1 -= 1; pos2 -= 1

class Node:
    # Stores the states of the sides
    right = 0
    left = 0
    up = 0
    down = 0
    unused = 1
    def __init__(self):
        self.unused = 1

# Initalises the grid
grid = []
for i in range(6):
    current = []
    for j in range(6):
        current.append(Node())
    grid.append(current)

# This is the actual output that will go out later
out = []
for i in range(5):
    moment = []
    for j in range(5):
        moment.append("*")
    out.append(moment)

# This checks for boxes and fills them in
def check(turn):
    changed = 0
    character = "X" if turn == 1 else "O"
    for i in range(5):
        for j in range(5):
            if grid[i][j].right and grid[i][j].down and grid[i+1][j+1].up and grid[i+1][j+1].left and grid[i][j].unused:
                out[i][j] = character
                changed = 1
                grid[i][j].unused = 0
    return changed


# This is the main driver code for the game
p1turn = 1
for i in range(turns):
    moved = 0
    if p1turn:
        pos1 = (pos1 + mod1)%36 - 1
        while moved == 0:
            pos1 = (pos1+1)%36
            if grid[pos1//6][pos1%6].up == 0 and pos1//6 != 0:
                grid[pos1//6][pos1%6].up = 1
                grid[pos1//6-1][pos1%6].down = 1
                moved = 1
            elif grid[pos1//6][pos1%6].right == 0 and pos1%6 != 5:
                grid[pos1//6][pos1%6].right = 1
                grid[pos1//6][pos1%6+1].left = 1
                moved = 1
            elif grid[pos1//6][pos1%6].down == 0 and pos1//6 != 5:
                grid[pos1//6][pos1%6].down = 1
                grid[pos1//6+1][pos1%6].up = 1
                moved = 1
            elif grid[pos1//6][pos1%6].left == 0 and pos1%6 != 0:
                grid[pos1//6][pos1%6].left = 1
                grid[pos1//6][pos1%6-1].right = 1
                moved = 1
        if check(1):
            p1turn = 1
        else:
            p1turn = 0
    else:
        pos2 = (pos2 + mod2)%36 - 1
        while moved == 0:
            pos2 = (pos2+1)%36
            if grid[pos2//6][pos2%6].up == 0 and pos2//6 != 0:
                grid[pos2//6][pos2%6].up = 1
                grid[pos2//6-1][pos2%6].down = 1
                moved = 1
            elif grid[pos2//6][pos2%6].left == 0 and pos2%6 != 0:
                grid[pos2//6][pos2%6].left = 1
                grid[pos2//6][pos2%6-1].right = 1
                moved = 1
            elif grid[pos2//6][pos2%6].down == 0 and pos2//6 != 5:
                grid[pos2//6][pos2%6].down = 1
                grid[pos2//6+1][pos2%6].up = 1
                moved = 1
            elif grid[pos2//6][pos2%6].right == 0 and pos2%6 != 5:
                grid[pos2//6][pos2%6].right = 1
                grid[pos2//6][pos2%6+1].left = 1
                moved = 1
        if check(2):
            p1turn = 0
        else:
            p1turn = 1

# Just formats the output nicely
p1Count = 0; p2Count = 0
for i in range(5):
    for j in range(5):
        if out[i][j] == "X":
            p1Count += 1
        if out[i][j] == "O":
            p2Count += 1
        print(out[i][j], end = " ")
    print("\n",end="")
print("\n" + str(p1Count), p2Count)


"""
Part B:
23 squares for player 1

"""

"""
Part D:
This last completion would have to be on a side of the square
as if it was in the middle then it would have to complete two boxes.
It being on the side is the only way that it only completes one box as
that side will only matter in one box's completion.

"""