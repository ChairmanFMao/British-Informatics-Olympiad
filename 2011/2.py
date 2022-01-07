from copy import deepcopy

seed = [int(i) for i in input().split()]

cards = []
# This generates all of the cards an appends them to the cards list in order
for i in ["C","H","S","D"]:
    for j in ["A","2","3","4","5","6","7","8","9","T","J","Q","K"]:
        cards.append([j + i,1])

# This function shuffles the cards and returns them according to the seed
def shuffle(seed,cards):
    ptr = 0
    shuffled = []
    sptr = 0
    while cards:
        for i in range(seed[sptr]-1):
            ptr = (ptr + 1) % len(cards)
        ptr %= len(cards)
        shuffled.append(cards.pop(ptr))
        sptr = (sptr + 1) % len(seed)

    print(shuffled[0][0],shuffled[-1][0])
    return shuffled

# This function completes the strategy 1
def strat1(cards):
    moving = 1
    while moving:
        moving = 0
        # This loops through the cards from right to left
        for i in range(len(cards)-1,0,-1):
            # This checks the adjacent card
            if cards[i-1][0][0] == cards[i][0][0] or cards[i-1][0][1] == cards[i][0][1]:
                cards[i-1][1] += cards[i][1]
                cards[i-1][0] = cards[i][0]
                cards.pop(i)
                moving = 1
                break
            # This checks the card 3 away
            if i >= 3:
                if cards[i-3][0][0] == cards[i][0][0] or cards[i-3][0][1] == cards[i][0][1]:
                    cards[i-3][1] += cards[i][1]
                    cards[i-3][0] = cards[i][0]
                    cards.pop(i)
                    moving = 1
                    break

    return [len(cards),cards[0][0]]

# This function completes the strategy 2
def strat2(cards):
    moving = 1
    while moving:
        moving = 0
        possible = 1
        # First element is the one being moved, second is the one it is being moved onto
        move = []
        # This loops through all the possible moves
        for i in range(len(cards)-1,0,-1):
            # This checks the adjacent card
            if cards[i-1][0][0] == cards[i][0][0] or cards[i-1][0][1] == cards[i][0][1]:
                if cards[i-1][1] + cards[i][1] > possible:
                    possible = cards[i-1][1] + cards[i][1]
                    move = [i,i-1]
                    moving = 1
            # This checks the card 3 away
            if i >= 3:
                if cards[i-3][0][0] == cards[i][0][0] or cards[i-3][0][1] == cards[i][0][1]:
                    if cards[i-3][1] + cards[i][1] > possible:
                        possible = cards[i-3][1] + cards[i][1]
                        move = [i,i-3]
                        moving = 1
        
        if len(move) > 0:
            cards[move[1]][1] += cards[move[0]][1]
            cards[move[1]][0] = cards[move[0]][0]
            cards.pop(move[0])
    
    return [len(cards),cards[0][0]]

# This function returns the number of valid moves for a given card state
def validMoves(cards):
    out = 0
    for i in range(len(cards)-1,0,-1):
        # This checks the card 1 away
        if cards[i-1][0][0] == cards[i][0][0] or cards[i-1][0][1] == cards[i][0][1]:
            out += 1
        # This checks the card 3 away
        if i >= 3:
            if cards[i-3][0][0] == cards[i][0][0] or cards[i-3][0][1] == cards[i][0][1]:
                out += 1
    return out

# This function completes the strategy 3
def strat3(cards):
    moving = 1
    while moving:
        moving = 0
        nextPossible = -1
        move = []
        for i in range(len(cards)-1,0,-1):
            # This checks the card 1 away
            if cards[i-1][0][0] == cards[i][0][0] or cards[i-1][0][1] == cards[i][0][1]:
                temp = deepcopy(cards)
                temp[i-1][1] += temp[i][1]
                temp[i-1][0] = temp[i][0]
                temp.pop(i)
                if validMoves(temp) > nextPossible:
                    move = [i,i-1]
                    nextPossible = validMoves(temp)
                    moving = 1
            # This checks the card 3 away
            if i >= 3:
                if cards[i-3][0][0] == cards[i][0][0] or cards[i-3][0][1] == cards[i][0][1]:
                    temp = deepcopy(cards)
                    temp[i-3][1] += temp[i][1]
                    temp[i-3][0] = temp[i][0]
                    temp.pop(i)
                    if validMoves(temp) > nextPossible:
                        move = [i,i-3]
                        nextPossible = validMoves(temp)
                        moving = 1
        
        if len(move) > 0:
            cards[move[1]][1] += cards[move[0]][1]
            cards[move[1]][0] = cards[move[0]][0]
            cards.pop(move[0])
    
    return [len(cards),cards[0][0]]

cards = shuffle(seed,cards)
print(" ".join([str(i) for i in strat1(deepcopy(cards))]))
print(" ".join([str(i) for i in strat2(deepcopy(cards))]))
print(" ".join([str(i) for i in strat3(deepcopy(cards))]))
