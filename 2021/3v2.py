from itertools import permutations
import heapq

# Just use a bfs
# can also use some dp kinda stuff
# there are only 8! ways

def minOps(s):
    INF = int(1e9)
    dist = dict()
    tmp = ""
    for i in range(len(s)):
        tmp += chr(i+65)
        for j in permutations(tmp):
            dist["".join(j)] = INF

    dist[""] = 0
    possible = [[0,""]]
    heapq.heapify(possible)
    while len(possible):
        current = heapq.heappop(possible)
        val = current[0]
        string = current[1]

        if string == s:
            return val

        if len(string) < len(s):
            tmp = string + chr(len(string)+65)
            if val+1 < dist[tmp]:
                heapq.heappush(possible,[val+1,tmp])
            dist[tmp] = min(dist[tmp],val+1)
        if len(string) >= 1:
            tmp = string[1:] + string[0]
            if val+1 < dist[tmp]:
                heapq.heappush(possible,[val+1,tmp])
            dist[tmp] = min(dist[tmp],val+1)
        if len(string) >= 2:
            tmp = string[1] + string[0] + string[2:]
            if val+1 < dist[tmp]:
                heapq.heappush(possible,[val+1,tmp])
            dist[tmp] = min(dist[tmp],val+1)

""" part a
#I sped this up using a heapq
s = input()
print(minOps(s))
#"""

""" part b
# there are 119, they are all of them except ABCDE
# Idk about the mark scheme here
#"""

""" part c
#this is not brute forcable I don't think
#I think I might be able to modify my original function to do this
minOps("HGFEDCBA")
# This is just adding extra stuff to the search
#"""

