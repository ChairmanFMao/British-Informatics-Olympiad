def a():
    # Pieces moved as far as possible

    p1 = [int(i) for i in input().split()]
    p2 = [int(i) for i in input().split()]

    # Positive numbers for white pieces and negative numbers for black pieces, neutron is 0
    grid = [["." for j in range(5)] for i in range(5)]
    grid[2][2] = 0
    for i in range(5):
        grid[0][i] = -(i+1)
        grid[4][i] = i+1

    ptr1 = 0; ptr2 = 0; turn = 1

    def printBoard():
        for i in grid:
            for j in i:
                print(j if type(j) == str else "F" if j > 0 else "S" if j < 0 else "*", end = "")
            print()
        print()

    # x then y
    vectors = [[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1]]

    # This function moves along a vector until it hits an edge or a piece
    def end(x,y,movement):
        while y + movement[1] >= 0 and y + movement[1] < 5 and x + movement[0] >= 0 and x + movement[0] < 5 and grid[y+movement[1]][x+movement[0]] == ".":
            x += movement[0]
            y += movement[1]
        return x,y

    # Checks if it will be possible for a piece at x,y will be able to move if fx,fy is filled in
    def possibleMoves(x,y,fx,fy,ox,oy):
        grid[fy][fx] = 0
        grid[oy][ox] = "."
        for i in range(8):
            endx, endy = end(x,y,vectors[i])
            if endx != x or endy != y:
                grid[fy][fx] = "."
                grid[oy][ox] = 0
                return 1
        grid[fy][fx] = "."
        grid[oy][ox] = 0
        return 0

    def move(piece):
        # Move neutron
        # Gets position of piece
        for i in range(5):
            for j in range(5):
                if grid[i][j] == piece:
                    px = j
                    py = i
        # Gets position of neutron
        for i in range(5):
            for j in range(5):
                if grid[i][j] == 0:
                    y = i
                    x = j
        # Checks if a winning move can be made
        moves = 0
        losing = 0
        for i in range(8):
            endx, endy = end(x,y,vectors[i])
            if (endy == 0 and piece < 0) or (endy == 4 and piece > 0):
                grid[endy][endx] = 0
                grid[y][x] = "."
                return 1
            if possibleMoves(px,py,endx,endy,x,y):
                if endx != x or endy != y:
                    moves += 1
                if (endy == 0 and piece > 0) or (endy == 4 and piece < 0):
                    losing += 1
        if moves == 0:
            return 1
        # Otherwise just does the first move that works and doesn't lose them the game and (doesn't block piece to move) - still to implement
        for i in range(8):
            endx, endy = end(x,y,vectors[i])
            if endx != x or endy != y:
                if possibleMoves(px,py,endx,endy,x,y):
                    if moves > losing:
                        if (endy == 0 and piece > 0) or (endy == 4 and piece < 0):
                            continue
                    grid[endy][endx] = 0
                    grid[y][x] = "."
                    # If a move that lost them the game was made just exit
                    if endy == 0 or endy == 4:
                        return 1
                    break
        
        # Move piece
        # Does the first move that works
        m = 1
        for i in range(8):
            endx, endy = end(px,py,vectors[i])
            if endx != px or endy != py:
                grid[endy][endx] = piece
                grid[py][px] = "."
                m = 0
                break
        if m:
            print("bad")
        return 0

    while 1:
        if turn & 1:
            if move(p1[ptr1%5]):
                break
            ptr1 += 1
            turn += 1
        else:
            if move(-p2[ptr2%5]):
                break
            ptr2 += 1
            turn += 1
        if turn == 2 or turn == 3:
            printBoard()
    printBoard()

# a()

"""
Part b:
I kinda have no ideas except like enumerating through all possibilities
Wrote some code that does it for me :)

Overall 65 combinations of moves
"""

def b():
    positions = 0
    grid = [[4,".",".",".",-4],
            [".",".",".",-2,5],
            [".",".",0,".",-3],
            [-1,".",".",-5,"."],
            [".",3,1,2,"."]]
    vectors = [[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1]]

    # Figures out where the counter will end up
    def end(x,y,movement):
        while y + movement[1] >= 0 and y + movement[1] < 5 and x + movement[0] >= 0 and x + movement[0] < 5 and grid[y+movement[1]][x+movement[0]] == ".":
            x += movement[0]
            y += movement[1]
        return x,y
    
    # Locates the neutron
    for i in range(5):
        for j in range(5):
            if grid[i][j] == 0:
                y = i
                x = j
    
    # Tries every single move for player 2
    def parse():
        pos = 0
        for i in range(5):
            for j in range(5):
                if type(grid[i][j]) == int and grid[i][j] < 0:
                    for k in range(8):
                        endx, endy = end(j,i,vectors[k])
                        if endx != j or endy != i:
                            pos += 1
        return pos
    
    # set neutron to position if it is valid
    for i in range(8):
        endx, endy = end(x,y,vectors[i])
        if endx != x or endy != y:
            if endy == 4 or endy == 0:
                positions += 1
                continue
            grid[endy][endx] = 0
            grid[y][x] = "."
            positions += parse()
            grid[endy][endx] = "."
            grid[y][x] = 0
    
    print(positions)

# b()

"""
Part c:
I think I can just manually count them, there aren't that many combos

There should be 21 but I can only see 18, and no one online has done this question before so...

black 1 - 4
white 5 - 4
black 3 - 4
white 3 - 4
white 2 - 1
black 2 - 1
"""