# Takes like exactly a second on the biggest of test cases, very epic
# It also works perfectly

n, p, q = input().split()
plan = [ord(i)-65 for i in n]; p = int(p); q = int(q)

# This is an object to store all of the room data
class Room:
    def __init__(self,value):
        self.value = value
        self.visits = 0
        self.connections = []
        self.exits = []
    def addConnection(self,connection):
        self.connections.append(connection)
        self.exits.append(0)

rooms = [Room(i) for i in range(len(plan)+2)]

# This function creates all of the connections between the rooms according to the plan
def createConnections():
    used = [0 for i in range(len(plan)+2)]

    while len(plan) > 0:
        for j in range(len(used)):
            if not used[j] and j not in plan:
                used[j] = 1
                rooms[j].addConnection(plan[0])
                rooms[plan[0]].addConnection(j)
                plan.pop(0)
                break

    for i in range(len(used)):
        if not used[i]:
            for j in range(i+1,len(used)):
                if not used[j]:
                    rooms[i].addConnection(j)
                    rooms[j].addConnection(i)
                    used[i] = 1
                    used[j] = 1
                    break
    
    for i in range(len(rooms)):
        rooms[i].connections.sort()

createConnections()

# This outputs all of the connections for each of the rooms
for i in rooms:
    for j in i.connections:
        print(chr(j+65),end="")
    print()

current = 0

# This is the main driver code that controls the movement of the spy
for i in range(q):
    if i == p:
        print(chr(current+65),end="")
    
    rooms[current].visits += 1
    # This deals with the case that the visits to the room are odd
    if rooms[current].visits & 1:
        rooms[current].exits[0] ^= 1
        current = rooms[current].connections[0]
    # This deals with the case that the visits to the room are even
    else:
        for i in range(len(rooms[current].exits)):
            if rooms[current].exits[i] & 1:
                if i == len(rooms[current].exits)-1:
                    rooms[current].exits[i] ^= 1
                    current = rooms[current].connections[i]
                else:
                    rooms[current].exits[i+1] ^= 1
                    current = rooms[current].connections[i+1]
                break

print(chr(current+65))
