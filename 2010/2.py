def a():
    grid = [[1 for j in range(11)] for i in range(11)]

    # These loops set up the grid
    for i in range(3):
        row = [int(i) for i in input().split()]
        for j in range(3):
            grid[4+i][4+j] = row[j]

    # This function prints the 9 local squares next to the die
    def printLocal(y,x):
        for i in range(3):
            out = ""
            for j in range(3):
                if y-1+i < 0 or y-1+i >= 11 or x-1+j < 0 or x-1+j >= 11:
                    out += "X"
                else:
                    out += str(grid[y-1+i][x-1+j])
            print(out)

    # This object holds which numbers on the die are in which direction
    class Dice:
        # This just initiates the die to default orientation
        def __init__(self):
            self.top = 1
            self.bottom = 6
            self.right = 4
            self.left = 3
            self.upwards = 2
            self.downwards = 5
        # This method handles the rolling of the die
        def move(self,direction):
            # This means that the die has been rolled upwards
            up = self.top
            if direction == 0:
                self.top = self.downwards
                self.downwards = self.bottom
                self.bottom = self.upwards
                self.upwards = up
            # Die rolled to the right
            elif direction == 1:
                self.top = self.left
                self.left = self.bottom
                self.bottom = self.right
                self.right = up
            # Die rolled downwards
            elif direction == 2:
                self.top = self.upwards
                self.upwards = self.bottom
                self.bottom = self.downwards
                self.downwards = up
            # Die rolled to the left
            elif direction == 3:
                self.top = self.right
                self.right = self.bottom
                self.bottom = self.left
                self.left = up

    # For direction, 0 means up, 1 means right, 2 means down, 3 means left
    x = 5; y = 5; heading = 0
    die = Dice()
    # Movement vectors, y before x
    vectors = {0:[-1,0],1:[0,1],2:[1,0],3:[0,-1]}

    while 1:
        # All of this takes in an input and checks what action needs to be done
        n = input()
        try:
            n = int(n)
        except ValueError:
            continue
        if not n:
            break
        if n < 1 or n > 100:
            continue
        
        # This then moves the die
        for i in range(n):
            grid[y][x] += die.top
            if grid[y][x] > 6:
                grid[y][x] -= 6
            
            if grid[y][x] == 2:
                heading = (heading + 1) % 4
            if grid[y][x] == 3 or grid[y][x] == 4:
                heading = (heading + 2) % 4
            if grid[y][x] == 5:
                heading = heading-1 if heading else 3
            y += vectors[heading][0]
            x += vectors[heading][1]
            die.move(heading)
            if x < 0:
                x += 11
            if y < 0:
                y += 11
            if x >= 11:
                x -= 11
            if y >= 11:
                y -= 11

        print()
        printLocal(y,x)
        print()

a()

"""
Part b:
Has to start with 2 to turn the die in the right direction initally
boxes:
2, 3 or 4, 2 or 3, 5 or 6, 3 or 4, 2 or 3
top:
1, 3, 4, 1, 3, 4

There are 5 choices where I can make 2 options and it doesn't effect the outcome
Therefore, there are 16 different ways the boxes can be numbered
"""

"""
Part c:
There are 8 different ways to do it in 4 moves.
There are (idk) different ways to do it in 6 moves.

Unsure, I will come back to this later after doing question 3

Turns out there are 160 ways, I enumerated the 4 move ones on paper, but it would've
been way to much work to do it for 6 moves
"""

"""
Part d:
I don't think there is a way but, that is just a hunch

Turns out there actually isn't the current numbers on the grid and the die's
orientation and heading fully determine the state of simulation. There are only a finite
number of different states, since there are only a finite number of states we must, eventually,
encounter one for the second time, if we return to one of these states, then the sequence of moves
will repeat and the die will be stuck in a loop.
"""