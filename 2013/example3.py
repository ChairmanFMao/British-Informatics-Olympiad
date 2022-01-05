
from collections import defaultdict
from copy import deepcopy
from string import ascii_letters
from itertools import combinations
alpha = ascii_letters
alphal = alpha[:len(alpha)//2]


class Board:

    # Just sets up the board from the input
    def __init__(self, start):
        self.board = [[0 for i in range(5)] for j in range(5)]
        self.done = defaultdict(int)
        for i in start:
            ind = alpha.index(i)
            got = 1
            if ind >= 26:
                ind -=26
                got = 2

            if ind!=25:
                y,x = divmod(ind, 5)
                self.board[y][x] = got

    # This function just prints the current board
    def pboard(self):
        for m in self.board:
            print(*m)
        print("-"*50)

    # This function turns letters into coordinates
    def convToCoords(self, letter):
        ind = alpha.index(letter)

        if ind >= 26:
            ind -= 26

        if ind != 25:
            y, x = divmod(ind, 5)
            #print(ind, letter, "HERE", "X", x, "Y", y)
            return (x, y)

    # This function just pushes the buttons, it has two modes
    # One where the real board is mutated, the other where a board passed
    # into the function is mutated
    def toggle(self, letter, board,isSelf=True):
        if isSelf:
            x,y = self.convToCoords(letter)
            self.board[y][x] += 1
            self.board[y][x] %= 3


            for dx, dy in [[0,1], [1,0], [-1,0], [0,-1]]:
                try:
                    nx, ny = dx+x, y+dy
                    if nx >= 0 and ny >= 0:
                        self.board[ny][nx] += 1
                        self.board[ny][nx] %= 3

                except:
                    pass
        else:
            x, y = self.convToCoords(letter)
            board[y][x] += 1
            board[y][x] %= 3

            for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                try:
                    nx, ny = dx + x, y + dy
                    if nx >= 0 and ny >= 0:
                        board[ny][nx] += 1
                        board[ny][nx] %= 3

                except:
                    pass
            return board

    # This is the main driver code for the whole board
    def reduce(self, board, dic,isSelf = True):
        # This mutates the actual board
        if isSelf:
            for letter in alphal[5:-1]:
                x,y = self.convToCoords(letter)
                while self.board[y-1][x] != 0:
                    self.toggle(letter, [])
                    #self.pboard()
                    self.done[letter] += 1
        # This just mutates the board parameter
        else:
            # This loops over every letter after e in the lower alphabet
            for letter in alphal[5:-1]:
                # This converts the letter into coordinates
                x,y = self.convToCoords(letter)
                #print(x,y, letter, self.board[y-1][x])
                # This turns the coordinate above it into 0, it has a max of two iterations
                while board[y-1][x] != 0:
                    #print("toggling", letter, self.convToCoords(letter), alphal.index(letter), "found invalid", y-1,x)
                    board = self.toggle(letter, board, isSelf = False)
                    #self.pboard()
                    dic[letter] += 1
                    dic[letter] %= 3
            return board,dic


    # This function gets the answers out of the boards
    def fin(self):
        got = []
        # This changes the length pos when it is generated
        for i in range(1, 6):
            # This generates all of the permutations of "abcde" with length of i
            # Overall there are 325 combinations of "abcde" with lengths ranging from 1 to 5
            for pos in combinations("abcde", i):
                # The board and done are copied
                done = deepcopy(self.done)
                cop = deepcopy(self.board)
                # All of the letters in pos are used on the copied boards
                for let in pos:
                    cop = self.toggle(let, cop, isSelf=False)
                    done[let] += 1

                # The copy is then reduced
                cop, newDone = self.reduce(cop, done, isSelf=False)

                # If the board is good then it is converted and appended to got
                if self.check(cop):
                    got.append(conv(done))
        return got


    # This function checks if the board is all off
    def check(self, board):
        return sum([sum(i) for i in board])==0



# This function converts the board from a grid into letters
def conv(dic):
    ans = ""
    for i in dic.keys():
        if dic[i]==2:
            ans += i.upper()
        elif dic[i]==1:
            ans += i
    return "".join(sorted(ans, key=lambda x: alphal.index(x.lower())))

# This sets up the board
solve = Board(input())

print(solve.board)
# This function call tests to see if it is possible using the given top row
solve.reduce([],{}, isSelf=True)
print(solve.board,solve.done)

# If the end board is solved then, print the board
if solve.check(solve.board):
    print(conv(solve.done))
answers = solve.fin()

# This prints the answers if there are any, else it prints impossible
if answers:
    print("\n".join(answers))
else:
    print("IMPOSSIBLE")
