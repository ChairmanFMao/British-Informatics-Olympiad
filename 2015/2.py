def a():
    a, c, m = [int(i) for i in input().split()]
    r = 0

    grid = [[0 for i in range(10)] for j in range(10)]
    ships = [4,3,3,2,2,2,1,1,1,1]
    shipPtr = 0

    def checkValid(x, y, length, direction):
        # When direction is one, we place vertically
        startx, starty = [x,y]
        for i in range(length):
            # Initially had a small bug here that I didn't account, think of all the possible things that could go wrong
            if x > 9 or y > 9:
                return 0
            for j in range(3):
                for k in range(3):
                    try:
                        if grid[x-1+j][y-1+k]:
                            return 0
                    except IndexError:
                        continue
            if direction:
                y += 1
            else:
                x += 1
        
        # We will now actually fill in this new ship
        for i in range(length):
            grid[startx][starty] = 1
            if direction:
                starty += 1
            else:
                startx += 1
        return 1

    while shipPtr < len(ships):
        r = (a * r + c) % m
        x = r % 10
        y = int((r % 100) / 10)
        r = (a * r + c) % m
        if checkValid(x,y,ships[shipPtr], r & 1):
            shipPtr += 1
            print(x, y, ("V" if r & 1 else "H"))

a()

"""
Part b:
Just called the function a and made it log the values of r that it created.
The coordinate pairs are:
x: 4, y: 0
x: 8, y: 0
x: 7, y: 0
x: 3, y: 0
"""

"""
Part c:
After reading question properly, we just need to count the number of squares touched
by two or more ships as they will guaranteed to be empty.
There are 18 of these such squares.
"""

"""
Part d:
Unsure of how to start this, because it is only a 5x5 board it shouldn't be too difficult
Idk how to get the answer, brute force doesn't seem like a good option.
"""