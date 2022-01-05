def a():
    # Code now works perfectly after debugging, there was one wrong connection ;-;

    f = input()
    xy = input()
    n = int(input())

    # Just need to build a network, I think this can be done with pointers

    class Point:
        lazy = 1
        pointingLeft = 1
        def __init__(self, straight, left, right, value):
            self.straight = straight
            self.left = left
            self.right = right
            self.value = value

    # The pointers will just be pointing the location of that junction in the points list
    points = []
    def initialisePoints():
        points.append(Point(3,4,5,0))
        points.append(Point(2,6,7,1))
        points.append(Point(1,8,9,2))
        points.append(Point(0,10,11,3))
        points.append(Point(0,12,13,4))
        points.append(Point(0,13,14,5))
        points.append(Point(1,14,15,6))
        points.append(Point(1,15,16,7))
        points.append(Point(2,16,17,8))
        points.append(Point(2,17,18,9))
        points.append(Point(3,18,19,10))
        points.append(Point(3,19,12,11))
        points.append(Point(20,11,4,12))
        points.append(Point(20,4,5,13))
        points.append(Point(21,5,6,14))
        points.append(Point(21,6,7,15))
        points.append(Point(22,7,8,16))
        points.append(Point(22,8,9,17))
        points.append(Point(23,9,10,18))
        points.append(Point(23,10,11,19))
        points.append(Point(21,12,13,20))
        points.append(Point(20,14,15,21))
        points.append(Point(23,16,17,22))
        points.append(Point(22,18,19,23))

    initialisePoints()

    # Initialises all of the flip-flop points
    for i in f:
        points[ord(i)-65].lazy = 0

    prev = ord(xy[0])-65
    current = ord(xy[1])-65

    # Code that moves the location of the train
    for i in range(n):
        # This means the train entered at the straight bit
        if points[prev].value == points[current].straight:
            next = points[current].left if points[current].pointingLeft else points[current].right
        # This means the train entered at a curved bit
        else:
            # This alternates the track for the lazy points
            if points[current].lazy:
                points[current].pointingLeft = points[prev].value == points[current].left
            
            next = points[current].straight
        # This flips the direction for flip flop points
        if points[prev].value == points[current].straight and not points[current].lazy:
            points[current].pointingLeft = not points[current].pointingLeft
        
        prev = current
        current = next

    print(chr(prev+65)+chr(current+65))

a()

"""
Part b:
VUMLDAEMUP
"""

def b():
    xy = "PV"
    class Point:
        lazy = 1
        pointingLeft = 1
        def __init__(self, straight, left, right, value):
            self.straight = straight
            self.left = left
            self.right = right
            self.value = value
    points = []
    def initialisePoints():
        points.append(Point(3,4,5,0))
        points.append(Point(2,6,7,1))
        points.append(Point(1,8,9,2))
        points.append(Point(0,10,11,3))
        points.append(Point(0,12,13,4))
        points.append(Point(0,13,14,5))
        points.append(Point(1,14,15,6))
        points.append(Point(1,15,16,7))
        points.append(Point(2,16,17,8))
        points.append(Point(2,17,18,9))
        points.append(Point(3,18,19,10))
        points.append(Point(3,19,12,11))
        points.append(Point(20,11,4,12))
        points.append(Point(20,4,5,13))
        points.append(Point(21,5,6,14))
        points.append(Point(21,6,7,15))
        points.append(Point(22,7,8,16))
        points.append(Point(22,8,9,17))
        points.append(Point(23,9,10,18))
        points.append(Point(23,10,11,19))
        points.append(Point(21,12,13,20))
        points.append(Point(20,14,15,21))
        points.append(Point(23,16,17,22))
        points.append(Point(22,18,19,23))
    initialisePoints()

    prev = ord(xy[0])-65
    current = ord(xy[1])-65

    # Code that moves the location of the train
    while current != 15:
        print(chr(current+65),end="")
        # This means the train entered at the straight bit
        if points[prev].value == points[current].straight:
            next = points[current].left if points[current].pointingLeft else points[current].right
        # This means the train entered at a curved bit
        else:
            # This alternates the track for the lazy points
            if points[current].lazy:
                points[current].pointingLeft = points[prev].value == points[current].left
            
            next = points[current].straight
        # This flips the direction for flip flop points
        if points[prev].value == points[current].straight and not points[current].lazy:
            points[current].pointingLeft = not points[current].pointingLeft
        
        prev = current
        current = next
    print("P")

# b()

"""
Part c:
I honestly had no idea, just looked at the mark scheme.

Train starts between M-T and U-X
The train is going towards the U-X point

There is a position cycle:
M-T -> U-X
U-X -> U-X
U-X -> M-T
M-T -> E-L
E-L -> A-D
A-D -> A-D
A-D -> E-L
E-L -> M-T

This cycle has 8 terms
As 1,000,000,000,000,000,000 is divisible by 8,
The train will end up M-T -> U-X, it will finish
in the start portion of the cycle.
"""

"""
Part d:
I didn't really know how to approach this problem,
Looked at the mark scheme but, its just the number with no context,
I also can't find an online answer to this part.
"""