# This takes like 2 seconds ish for the biggest input, it is almost instant

from queue import PriorityQueue
from itertools import permutations

b = input()

dist = {}
for i in range(9):
    for p in permutations("ABCDEFGH",i):
        dist["".join(p)] = 1e9

queue = PriorityQueue()
queue.put((0,""))
while not queue.empty():
    current = queue.get()
    s = current[1]
    if s == b:
        print(current[0])
        break
    if len(s) < len(b):
        if current[0]+1 < dist[s+chr(65+len(s))]:
            queue.put((current[0]+1,s+chr(65+len(s))))
            dist[s+chr(65+len(s))] = current[0]+1
    if len(s) > 1:
        if current[0] + 1 < dist[s[1]+s[0]+s[2:]]:
            queue.put((current[0]+1,s[1]+s[0]+s[2:]))
            dist[s[1]+s[0]+s[2:]] = current[0]+1
        if current[0] + 1 < dist[s[1:]+s[0]]:
            queue.put((current[0]+1,s[1:]+s[0]))
            dist[s[1:]+s[0]] = current[0]
