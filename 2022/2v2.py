# This is just an implementation fest
# I actually managed to implement this correctly and efficiently
# first try
GRIDSIZE = 25

# This will store all of the hexagons and their edges
class Grid:
    def __init__(self):
        self.grid = [[0 for i in range(6)] for j in range(GRIDSIZE)]

    def fill(self,pos,direction,colour):
        # fills one of the edges
        self.grid[pos][direction] = colour

        direction2 = (direction+3)%6
        # fills the related edge if it exists
        # we need to do the rows as well
        if direction == 0 and pos not in [0,1,2,3,4,9,19]:
            if (pos//5)&1:
                self.grid[pos-4][direction2] = colour
            else:
                self.grid[pos-5][direction2] = colour
        if direction == 1 and pos not in [4,9,14,19,24]:
            self.grid[pos+1][direction2] = colour
        if direction == 2 and pos not in [9,19,20,21,22,23,24]:
            if (pos//5)&1:
                self.grid[pos+6][direction2] = colour
            else:
                self.grid[pos+5][direction2] = colour
        if direction == 3 and pos not in [0,10,20,21,22,23,24]:
            if (pos//5)&1:
                self.grid[pos+5][direction2] = colour
            else:
                self.grid[pos+4][direction2] = colour
        if direction == 4 and pos not in [0,5,10,15,20]:
            self.grid[pos-1][direction2] = colour
        if direction == 5 and pos not in [0,1,2,3,4,10,20]:
            if (pos//5)&1:
                self.grid[pos-5][direction2] = colour
            else:
                self.grid[pos-6][direction2] = colour

    def own(self):
        red = blue = 0
        for i in self.grid:
            rc = bc = 0
            for j in i:
                if j == 1:
                    rc += 1
                elif j == 2:
                    bc += 1
            
            if rc > bc:
                red += 1
            elif bc > rc:
                blue += 1
        return (red,blue)

        
# This makes the drones easier to manage
class Drone:
    def __init__(self,colour,pos,direction,speed):
        self.colour = colour
        self.pos = pos
        self.direction = direction
        self.speed = speed

    # Simulates skirmishes
    def skirmish(self,grid):
        # Gets the value of that edge before colouring
        original = grid.grid[self.pos][self.direction]
        grid.fill(self.pos,self.direction,self.colour)
        
        # Moves the drone
        self.pos = (self.pos + self.speed)%GRIDSIZE
        self.direction = (self.direction + (1 if self.colour == 1 else -1) + 6)%6
        return original

    # Simulates a red feud
    def feudr(self,grid):
        # We want to ensure that best is overrode
        best = [-1,-1]; operation = [-1,-1]
        for i in range(25):
            for j in range(6):
                if not grid.grid[i][j]:
                    grid.fill(i,j,self.colour)
                    tmp = grid.own()
                    grid.fill(i,j,0)
                    if tmp[0] > best[0] or (tmp[0] == best[0] and tmp[1] < best[1]):
                        best = tmp
                        operation = [i,j]

        grid.fill(operation[0],operation[1],self.colour)

    # Simulates a blue feud
    def feudb(self,grid):
        # We want to ensure that best is overrode
        best = [-1,-1]; operation = [-1,-1]
        for i in range(24,-1,-1):
            for j in range(5,-1,-1):
                if not grid.grid[i][j]:
                    grid.fill(i,j,self.colour)
                    tmp = grid.own()
                    grid.fill(i,j,0)
                    if tmp[1] > best[1] or (tmp[1] == best[1] and tmp[0] < best[0]):
                        best = tmp
                        operation = [i,j]

        grid.fill(operation[0],operation[1],self.colour)

    # Determines the right type of feud
    def feud(self,grid):
        if self.colour == 1:
            self.feudr(grid)
        else:
            self.feudb(grid)

#""" part a
r, b = list(map(int,input().split()))
s, f = list(map(int,input().split()))
# Sets up a grid object
grid = Grid()
# 1 for red, 2 for blue
red = Drone(1,0,0,r)
blue = Drone(2,24,5,b)

# Does all of the skirmishes
for i in range(s):
    red.skirmish(grid)
    blue.skirmish(grid)

# Does all of the feuds
for i in range(f):
    red.feud(grid)
    blue.feud(grid)

print("\n".join(list(map(str,grid.own()))))
#"""

""" part b
Drawn on paper, hard to show
I got it wrong initally
"""

""" part c
we can just make a brute force simulation and add a move cap
at like 1000 or smth

largest = -1; smallest = 1000
# value for r
for i in range(1,26):
    # value for b
    for j in range(1,26):
        grid = Grid()
        red = Drone(1,0,0,i)
        blue = Drone(2,24,5,j)
        counter = 0
        while counter < 1000:
            if red.skirmish(grid) == 2:
                break
            if blue.skirmish(grid) == 1:
                break
            counter += 1

        if counter != 1000:
            largest = max(largest,counter)
            smallest = min(smallest,counter)

print(smallest,largest)

smallest is 1
largest is 28
got the value for the largest wrong initally as 20
It changes ownership not just overridden, misread and it led to
me getting wa
"""

