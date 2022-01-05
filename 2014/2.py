def a():
    # Solution currently fully works! 25/25 marks

    n = int(input())

    # This sets up the grid with the numbers
    tiles = [[int(i) for i in input().split()] for j in range(n)]

    # v for vertical, h for horizontal, rest are diagonal, t for top, b for bottom, r for right, l for left
    red = {1:"v",2:"h",3:"tl",4:"tr",5:"br",6:"bl"}
    green = {1:"h",2:"v",3:"br",4:"bl",5:"tl",6:"tr"}

    # This dictionary relates the type of tile to the movements that are possible on it
    movement = {"v":["u","d"], "h":["r","l"], "tl":["u","l"], "tr":["u","r"], "bl":["l","d"], "br":["r","d"]}

    # This is a dictionary for movement vectors, y before x
    vector = {"r":[0,1], "l":[0,-1], "u":[-1,0], "d":[1,0]}

    # This is a dictionary of valid tiles to move to from a move
    valid = {"r":["h","tl","bl"], "l":["h","br","tr"], "u":["v","bl","br"], "d":["v","tl","tr"]}

    # These are the grids for red and green
    rgrid = [[red[j] for j in i] for i in tiles]
    ggrid = [[green[j] for j in i] for i in tiles]

    # This searches a whole grid and ouputs the score of that grid
    def solve(grid):
        # A score is kept track of as well as a set used which contains the tuple coordinates that have been visited
        score = 0
        used = set()
        for i in range(n):
            for j in range(n):
                if (i,j) in used:
                    continue
                seen = set()
                seen.add((i,j))
                y = i
                x = j
                # We do a move in one direction from the start as if we went in both it would be more difficult
                start = movement[grid[y][x]][0]
                y += vector[start][0]
                x += vector[start][1]
                if x < 0 or y < 0 or x >= n or y >= n or not grid[y][x] in valid[start]:
                    used = set.union(used,seen)
                    continue
                seen.add((y,x))
                # We then carry on going from that one we moved to around until we meet a dead end
                a = 1
                while a:
                    start = movement[grid[y][x]]
                    # We try every movement for the possible square, max two movements
                    for k in start:
                        y += vector[k][0]
                        x += vector[k][1]
                        # A valid loop needs to contain at least 4 sites in the grid
                        if (y,x) == (i,j) and len(seen) > 3:
                            score += len(seen)
                            a = 0
                            break
                        # This handles the case of the tile that we just left
                        if (y,x) in seen:
                            y -= vector[k][0]
                            x -= vector[k][1]
                            continue
                        # This handles the case where the coordinates aren't on the grid or the tiles don't fit together
                        if x < 0 or y < 0 or x >= n or y >= n or not grid[y][x] in valid[k]:
                            a = 0
                            break
                        seen.add((y,x))
                        # It took me quite a while to figure out that I was missing this break, as if it works you just
                        # need to move onto the next square instead of continuing processing
                        break
                used = set.union(used, seen)

        return score

    print(solve(rgrid),solve(ggrid))

a()

"""
Part b:
7, this is to disrupt the red loop or to make a bigger green loop
Think about it, for each one being a different tile you get another combo
The real answer is 31 as each of the 6 red tiles in the loop can be switched
for any other 5 of the tiles and the one tile can be switched to 6 to make a
bigger green loop
"""

"""
Part c:
I am just attempting to create all of the possibilities in my head
4 size 4 -> 1
2 size 4, 1 size 8 -> 4
1 size 4, 1 size 12 -> 5
2 size 8 -> 4
1 size 16 -> 4

Overall 18 possibilites
"""

"""
Part d:
No, as every loop has to contain an even number of squares, it would be impossible
for red to have one more point than green as one player would need to get an odd score
and this is impossible due to loops only containing an even number of squares. The difference
in the players scores must be even as both of their scores have to be even.
"""