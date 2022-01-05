# I spent some time optmising the code and I managed to get it to be
# really efficient, the thing that was holding me back was that I kept
# searching for the top left filled triangle rather than just keeping
# it cached.

# Player positions always stored in the empty triangle for the edge
class Player:
    side = 1
    x = 249
    y = 249
    id = 0
    score = 0
    trav = 0
    def __init__(self,id,trav):
        self.id = id
        self.trav = trav

# Initialises the grid
grid = [[0 for j in range(500)] for i in range(500)]

# 249, 250 will be the starting upwards facing triangle
grid[249][250] = 9

# This just takes the inputs and formats them a bit
p, m = [int(i) for i in input().split()]
maxTrav = [int(i) for i in input().split()]
players = [Player(i+1,maxTrav[i]) for i in range(p)]

# This function checks if this triangle will score a player a point
def check(y,x,id):
    out = 0
    if (y+x) & 1:
        if grid[y+1][x+1] == id and grid[y+1][x-1] == id:
            out += 1
        if grid[y][x+2] == id and grid[y-1][x+1] == id:
            out += 1
        if grid[y][x-2] == id and grid[y-1][x-1] == id:
            out += 1
    else:
        if grid[y-1][x-1] == id and grid[y-1][x+1] == id:
            out += 1
        if grid[y][x-2] == id and grid[y+1][x-1] == id:
            out += 1
        if grid[y][x+2] == id and grid[y+1][x+1] == id:
            out += 1

    return out

# This function moves a player to the next spot clockwise
def traverse(y,x,s):
    if (y+x) & 1:
            if s == 1:
                if grid[y][x-1]:
                    s = 3
                elif grid[y-1][x-1]:
                    x -= 1
                    s = 0
                elif grid[y-1][x]:
                    y -= 1
                    x -= 1
                    s = 1
                elif grid[y-1][x+1]:
                    y -= 1
                    s = 1
                else:
                    y -= 1
                    x += 1
                    s = 2
            elif s == 2:
                if grid[y][x+1]:
                    s = 1
                elif grid[y][x+2]:
                    x += 1
                    s = 1
                elif grid[y+1][x+2]:
                    x += 2
                    s = 2
                elif grid[y+1][x+1]:
                    x += 2
                    y += 1
                    s = 3
                else:
                    x += 1
                    y += 1
                    s = 3
            elif s == 3:
                if grid[y+1][x]:
                    s = 2
                elif grid[y+1][x-1]:
                    y += 1
                    s = 3
                elif grid[y+1][x-2]:
                    y += 1
                    x -= 1
                    s = 3
                elif grid[y][x-2]:
                    y += 1
                    x -= 2
                    s = 0
                else:
                    x -= 2
                    s = 1
    else:
        if s == 0:
            if grid[y][x-1]:
                s = 3
            elif grid[y][x-2]:
                x -= 1
                s = 3
            elif grid[y-1][x-2]:
                x -= 2
                s = 0
            elif grid[y-1][x-1]:
                x -= 2
                y -= 1
                s = 1
            else:
                y -= 1
                x -= 1
                s = 1
        elif s == 1:
            if grid[y-1][x]:
                s = 0
            elif grid[y-1][x+1]:
                y -= 1
                s = 1
            elif grid[y-1][x+2]:
                y -= 1
                x += 1
                s = 1
            elif grid[y][x+2]:
                y -= 1
                x += 2
                s = 2
            else:
                x += 2
                s = 3
        elif s == 3:
            if grid[y][x+1]:
                s = 1
            elif grid[y+1][x+1]:
                x += 1
                s = 2
            elif grid[y+1][x]:
                y += 1
                x += 1
                s = 3
            elif grid[y+1][x-1]:
                y += 1
                s = 3
            else:
                y += 1
                x -= 1
                s = 0
    return [y,x,s]

# This function will move a player around the outside of the grid
def move(playerIndex):
    y = players[playerIndex].y
    x = players[playerIndex].x
    s = players[playerIndex].side
    # This goes through all the traversals that the player can
    for i in range(players[playerIndex].trav):
        y, x, s = traverse(y,x,s)
        # If the current triangle has potential to score the player a point
        # on the next turn then the player stops
        if check(y,x,players[playerIndex].id):
            break
    players[playerIndex].y = y
    players[playerIndex].x = x
    players[playerIndex].side = s

# This finds the perimeter of the leftover shape
def perimeter():
    starty, startx = top
    starts = 1
    y = starty
    x = startx
    s = starts
    moves = 0
    while y != starty or x != startx or s != starts or moves == 0:
        y, x, s = traverse(y,x,s)
        moves += 1

    print(moves)

# Will store the top left co ordinate
top = [249,249]

# This function goes through all of the moves in the game
for i in range(m):
    # This if statement handles the situation where the triangle the the current player
    # is in, is currently occupied, it will replace them at the top left to the shape
    startx = players[i%p].x
    starty = players[i%p].y
    move(i%p)
    players[i%p].score += check(starty,startx,players[i%p].id)
    grid[starty][startx] = players[i%p].id
    if starty < top[0] or (starty == top[0] and startx <= top[1]):
        top = [starty,startx-1]
    for j in range(p):
        if grid[players[j].y][players[j].x]:
            players[j].y, players[j].x = top
            players[j].side = 1

# This outputs all of the players scores
for i in players:
    print(i.score)

perimeter()
