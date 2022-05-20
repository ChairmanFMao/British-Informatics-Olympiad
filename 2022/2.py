# Just taking the inputs for the problem
r, b = [int(i) for i in input().split()]
s, f = [int(i) for i in input().split()]

# Unsure if to use hexagons as a class because it might become very ugly
# I would need to sync the edges so that it works well
# 0 is for empty, 1 is for red, 2 is for blue
# This now works for all of the test cases

class Bee:
    # Sets up all of the attributes for the Bee
    def __init__(self, colour, moveDist):
        # This is for if the Bee is red
        if colour == 1:
            self.x = 0
            self.y = 0
            self.direction = 0
        # This if for if the Bee is blue
        else:
            self.x = 4
            self.y = 4
            self.direction = 5
        self.colour = colour
        self.moveDist = moveDist

    # Function to move the Bee along the hive
    def move(self):
        self.x += self.moveDist
        # If there is row overflow
        self.y += self.x//5
        self.x %= 5
        # If there is grid overflow
        self.y %= 5

# Just a class to store all the sides of the hexagons
class Hexagon:
    def __init__(self):
        self.sides = [0,0,0,0,0,0]

# Opposite edges
opposite = {0:3, 1:4, 2:5, 3:0, 4:1, 5:2}

# Fills one edge on all corresponding hexagons
# A little hard coding was needed but, it works perfectly
def fill(x, y, edge, colour):
    grid[y][x].sides[edge] = colour

    if edge == 0:
        if not (y == 0 or (x == 4 and y == 1) or (x == 4 and y == 3)):
            grid[y-1][x+(y&1)].sides[opposite[edge]] = colour

    if edge == 1:
        if not x == 4:
            grid[y][x+1].sides[opposite[edge]] = colour

    if edge == 2:
        if not (y == 4 or (x == 4 and y == 1) or (x == 4 and y == 3)):
            grid[y+1][x+(y&1)].sides[opposite[edge]] = colour

    if edge == 3:
        if not (y == 4 or (x == 0 and y == 0) or (x == 0 and y == 2)):
            grid[y+1][x-1+(y&1)].sides[opposite[edge]] = colour

    if edge == 4:
        if not x == 0:
            grid[y][x-1].sides[opposite[edge]] = colour

    if edge == 5:
        if not (y == 0 or (x == 0 and y == 2) or (x == 0 and y == 4)):
            grid[y-1][x-1+(y&1)].sides[opposite[edge]] = colour

# Determines who owns which squares with the current grid
def gridState():
    rout = 0; bout = 0
    for i in grid:
       for j in i:
           rc = 0; bc = 0
           for k in j.sides:
               if k == 1:
                   rc += 1
               if k == 2:
                   bc += 1

           if rc > bc:
               rout += 1
           if bc > rc:
               bout += 1

    return rout, bout

# We are just going to test all the edges and check which one gives the best increase
def feud(colour):
    bestr, bestb = gridState(); bestx = -1; besty = -1; bestd = -1
    # This makes sure that an edge is laid if possible even if it doesn't
    # lead to an increase in the colour or a decrease in the other colour
    if colour == 1:
        bestr -= 1
    else:
        bestb -= 1
    start = 0 if colour == 1 else 4; start2 = 0 if colour == 1 else 5
    end = 5 if colour == 1 else -1; end2 = 6 if colour == 1 else -1
    step = 1 if colour == 1 else -1
    # This is our y co-ordinate
    for j in range(start, end, step):
        # This is our x co-ordinate
        for i in range(start, end, step):
            # This is our edge
            for k in range(start2, end2, step):
                # This only triggers if the edge is empty
                # Basically just tests if it leads to better new state
                if grid[j][i].sides[k] == 0:
                    fill(i,j,k,colour)
                    newr, newb = gridState()
                    if colour == 1:
                        if newr > bestr or (newr == bestr and newb < bestb):
                            bestr = newr
                            bestb = newb
                            bestx = i
                            besty = j
                            bestd = k
                    else:
                        if newb > bestb or (newb == bestb and newr < bestr):
                            bestb = newb
                            bestr = newr
                            bestx = i
                            besty = j
                            bestd = k
                    fill(i,j,k,0)
    
    # This just checks if there are any valid edges left to fill
    if not bestd == -1:
        fill(bestx, besty, bestd, colour)

# Creates the grid of hexagons
grid = [[Hexagon() for i in range(5)] for j in range(5)]

# Instantiates the bee objects
red = Bee(1,r)
blue = Bee(2,b)

# Skirmishes
for i in range(s):
    fill(red.x,red.y,red.direction,red.colour)
    red.direction = (red.direction+1)%6
    red.move()
    
    fill(blue.x,blue.y,blue.direction,blue.colour)
    blue.direction = (blue.direction+5)%6
    blue.move()

# Feuds
for i in range(f):
    feud(red.colour)
    feud(blue.colour)

redOut, blueOut = gridState()
print(str(redOut) + "\n" + str(blueOut))

