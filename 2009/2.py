from copy import deepcopy

def a():
    grid = [list(input()) for i in range(4)]
    copy = deepcopy(grid)
    score = 0

    # Prints out the grid formatted nicely
    def printGrid():
        for i in range(4):
            for j in range(4):
                print(grid[i][j],end="")
            print()
        print()

    # This list holds the next element to fall into the simulation for each column
    nextPtr = [3,3,3,3]

    playing = 1

    # This keeps the game going indefinitely
    while playing:
        n = input()
        # This handles the input
        try:
            n = int(n)
        except ValueError:
            continue
        if not n:
            break
        if n < 1 or n > 100:
            continue

        print()
        # This removes and replaces the pieces
        for i in range(n):
            used = [[0 for k in range(4)] for j in range(4)]
            blocks = 1
            queue = []
            # This iterates through all of the squares, we do a bfs to find the blocks
            kill = []
            for j in range(4):
                for k in range(4):
                    if used[j][k]:
                        continue
                    size = 0
                    letter = grid[j][k]
                    working = []
                    queue.append([j,k])
                    while len(queue):
                        y, x = queue.pop(0)
                        used[y][x] = 1
                        size += 1
                        working.append([y,x])
                        if y > 0:
                            if grid[y-1][x] == letter and not used[y-1][x]:
                                queue.append([y-1,x])
                        if y < 3:
                            if grid[y+1][x] == letter and not used[y+1][x]:
                                queue.append([y+1,x])
                        if x > 0:
                            if grid[y][x-1] == letter and not used[y][x-1]:
                                queue.append([y,x-1])
                        if x < 3:
                            if grid[y][x+1] == letter and not used[y][x+1]:
                                queue.append([y,x+1])

                    if size > 1:
                        blocks *= size
                        for l in working:
                            kill.append(l)
            
            # This checks if there were no blocks
            if blocks == 1:
                print("GAME OVER")
                print(score)
                playing = 0
                break
            score += blocks
            # This removes all of the blocks from the grid
            for j in kill:
                grid[j[0]][j[1]] = " "

            # This moves squares down the grid
            moving = 1
            while moving:
                moving = 0
                for j in range(3):
                    for k in range(4):
                        if grid[j][k] != " " and grid[j+1][k] == " ":
                            grid[j+1][k] = grid[j][k]
                            grid[j][k] = " "
                            moving = 1

            # This moves new squares into the grid from bottom to top, j is y, k is x
            for j in range(3,-1,-1):
                for k in range(4):
                    if grid[j][k] == " ":
                        grid[j][k] = copy[nextPtr[k]][k]
                        nextPtr[k] = nextPtr[k] - 1 if nextPtr[k] else 3
        
        # This will output the grid and score if the game is still going
        if playing:
            printGrid()
            print(score)
            print()

a()
# Can't think of any bugs at the moment, I think it works well

"""
Part b:
105 -> 3 * 5 * 7
grid:
RRRB
BBBB
GGGG
GGGR
"""

"""
Part c:
3 * 3 * 3 * 3 * 4 -> 324
"""

def c():
    out = 0
    for i in range(5):
        for j in range(5):
            for k in range(5):
                for l in range(5):
                    for m in range(5):
                        if sum([i,j,k,l,m]) == 16:
                            out = max(out, i*j*k*l*m)
    print(out)

# c()

"""
Part d:
No, it will not, imagine a point in the grid where four different blocks meet
e.g.
DAAA
DBCC
DBDC
DDDC
Where A, B, C, D all represent blocks

This would be impossible to place using the pieces, take for example the B in
the top left of the grid, it is touching 3 other blocks. This means that there
need to be four different block types otherwise you can't pick a colour for B.
All of the other blocks also touch, so you can't get out of the situation.
Every single block touches all of the other blocks, you need four different block
colours to allow this to be legal.
"""
