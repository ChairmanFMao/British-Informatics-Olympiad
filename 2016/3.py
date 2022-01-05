from math import ceil
from collections import deque
l, p, q = [int(i) for i in input().split()]
# Start is p, end is q
# I think that this is just a bfs
# Currently works but is just very slow, maybe I should implement dijkstra's logic
# This program works but, it takes just a little too long with larger inputs
# So, I rewrote the whole thing in cpp in "3.cpp" and it runs even the bigger inputs in about a second

# This checked dictionary caches the output for numbers that were already run through checkPrime
checked = dict()
def checkPrime(number):
    if number == 2:
        return 1
    if not (number & 1):
        return 0
    if checked.get(number) != None:
        return checked[number]
    for i in range(3, ceil(pow(number,0.5)) + 1, 2):
        if not (number % i):
            checked[number] = 0
            return 0
    checked[number] = 1
    return 1

shortest = [int(1e9) for i in range(l+1)]
powers = [pow(2,i) for i in range(24)]
queue = deque([[p,1]])
while len(queue) > 0:
    current = queue.popleft()
    if current[0] == q:
        print(current[1])
        break
    for i in powers:
        if current[0] - i > 0:
            if current[1] + 1 < shortest[current[0]-i]:
                if checkPrime(current[0]-i):
                    queue.append([current[0]-i,current[1]+1])
                    shortest[current[0]-i] = current[1]+1
        if current[0] + i <= l:
            if current[1] + 1 < shortest[current[0]+i]:
                if checkPrime(current[0]+i):
                    queue.append([current[0]+i,current[1]+1])
                    shortest[current[0]+i] = current[1] + 1
