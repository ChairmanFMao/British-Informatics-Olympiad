from copy import deepcopy

# Actually very happy with this solution, interesting problem

# Stores all of the information about a current board
class Board:
    def __init__(self,middle,edges):
        self.middle = middle
        self.edges = deepcopy(edges)
    def __str__(self):
        return str(self.middle) + "".join([str(a) for a in self.edges])

# This returns all possible moves for the player in a current state
def move(player,state):
    out = []
    # This move takes priority as it uses the first letter n the representation
    if state.middle == player:
        for i in range(8):
            if state.edges[i] == "E":
                next = Board(state.middle,state.edges)
                next.middle = "E"
                next.edges[i] = player
                out.append(next)

    # This takes care of the case where the middle is empty
    if state.middle == "E":
        for i in range(8):
            if state.edges[i] == player:
                if i == 0:
                    if state.edges[-1] != player or state.edges[1] != player:
                        next = Board(state.middle,state.edges)
                        next.middle = player
                        next.edges[0] = "E"
                        out.append(next)
                elif i == 7:
                    if state.edges[6] != player or state.edges[0] != player:
                        next = Board(state.middle,state.edges)
                        next.middle = player
                        next.edges[7] = "E"
                        out.append(next)
                else:
                    if state.edges[i-1] != player or state.edges[i+1] != player:
                        next = Board(state.middle,state.edges)
                        next.middle = player
                        next.edges[i] = "E"
                        out.append(next)
    # This takes care of when an outside spot is empty
    else:
        for i in range(8):
            if state.edges[i] == "E":
                if i > 0:
                    if state.edges[i-1] == player:
                        next = Board(state.middle,state.edges)
                        next.edges[i] = player
                        next.edges[i-1] = "E"
                        out.append(next)
                if i < 7:
                    if state.edges[i+1] == player:
                        next = Board(state.middle,state.edges)
                        next.edges[i] = player
                        next.edges[i+1] = "E"
                        out.append(next)
                if i == 0:
                    if state.edges[-1] == player:
                        next = Board(state.middle,state.edges)
                        next.edges[i] = player
                        next.edges[-1] = "E"
                        out.append(next)
                if i == 7:
                    if state.edges[0] == player:
                        next = Board(state.middle,state.edges)
                        next.edges[i] = player
                        next.edges[0] = "E"
                        out.append(next)
    
    return out

# This does a move for the current state according to the strategies
def process(player,current):
    moves = move(player,current)
    # This is if there are no valid moves
    if not len(moves):
        print(str(current))
        print("Player " + ("1" if player == "X" else "2") + " wins")
        return None
    
    # This checks if there are any winning moves
    for i in moves:
        if not len(move("O" if player == "X" else "X",i)):
            return i
    
    # Takes care of potentially losing moves
    bad = []
    for i in range(len(moves)):
        next = move("O" if player == "X" else "X",moves[i])
        for j in next:
            if not len(move(player,j)):
                bad.append(i)
    
    # This is if there is a move that prevents loss, do it
    if len(bad) != len(moves):
        for i in range(len(moves)):
            if i not in bad:
                return moves[i]
    
    # Otherwise, the leftmost move is returned
    return moves[0]

start = input()
start = Board(start[0],list(start[1:]))
turn = 0

# I am first going to make an algorithm that does parts 1 and 3, then add in part 2

while 1:
    inp = input()
    if inp == "n":
        start = process("X" if turn else "O",start)
        turn ^= 1
        if start == None:
            break
        print(str(start))
    if inp == "r":
        counter = 0
        # A game is deemed a draw after 1000 moves and no one has won
        while start != None and counter < 1000:
            start = process("X" if turn else "O",start)
            turn ^= 1
            counter += 1
        if counter == 1000:
            print("Draw")
            break
        if start == None:
            break

# Somehow getting moves that end up in the same state as the start
