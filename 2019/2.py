t, moves, m = input().split()
t = int(t); m = int(m)

# This function reduces the cooldown on all of the visited squares
def reduceCooldown():
    length = len(cooldown)
    for i in range(length):
        current = cooldown.pop(0)
        if current[0] == 1:
            continue
        cooldown.append([current[0]-1,current[1]])

# This function checks if the queue contains a certain coordinate
def contains(y,x):
    length = len(cooldown)
    for i in range(length):
        current = cooldown.pop(0)
        cooldown.append(current)
        if current[1][0] == y and current[1][1] == x:
            return 1
    return 0

# This function moves the explorer in a direction if possible
def forward():
    global y
    global x
    global direction
    global cooldown
    # This handles the explorer having blocked path or being unable to move
    rotates = 0
    while contains(y + vectors[direction][0], x + vectors[direction][1]) and rotates < 4:
        direction = (direction + 1) % 4
        rotates += 1
    if rotates == 4:
        return 0
    
    cooldown.append([t+1,[y,x]])
    y += vectors[direction][0]
    x += vectors[direction][1]
    return 1

cooldown = []
x = 0
y = 0
# 0 means up, 1 means right, 2 means down, 3 means left
direction = 0
# Dictionary for directions to movement vectors, y before x
vectors = {0:[1,0],1:[0,1],2:[-1,0],3:[0,-1]}

# This is the main driver code
for i in range(m):
    # This changes the direction of the explorer according to the instructions
    move = moves[i%len(moves)]
    if move == "R":
        direction = (direction + 1) % 4
    elif move == "L":
        direction = 3 if not direction else direction - 1
    # If forward returns false, the explorer is blocked in
    if not forward():
        break
    reduceCooldown()

print(x,y)
