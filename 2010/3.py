# Currently solution is quite inefficient and just dies with larger input
# I think this is due to the heavy use of the deepcopy and inefficient bfs
# I think that I also need to reconsider how the stuff is being stored, something for tomorrow
# Need to make algorithm as efficient as possible, not just to work for test case,
# I was lazy and chose not to implement Dijkstra's intially, which was a silly mistake

from copy import deepcopy

def a():
    INF = 1e9
    j, n = [int(i) for i in input().split()]
    maxJugs = [int(i) for i in input().split()]
    jugs = [0 for i in range(j)]

    dist = {}

    # This sets the initial distance to all states to INF(1e9)
    if j == 1:
        for i in range(maxJugs[0]+1):
            dist[i] = INF
    elif j == 2:
        for i in range(maxJugs[0]+1):
            for k in range(maxJugs[1]+1):
                dist[tuple([i,k])] = INF
    elif j == 3:
        for i in range(maxJugs[0]+1):
            for k in range(maxJugs[1]+1):
                for l in range(maxJugs[2]+1):
                    dist[tuple([i,k,l])] = INF

    queue = [[0,jugs]]
    dist[tuple(jugs)] = 0
    out = 0
    while len(queue):
        current = queue.pop(0)
        # Checks if any of the jugs contain n
        for i in range(j):
            if current[1][i] == n:
                print(current[0])
                out = 1
                break
        if out:
            break

        # Empties/fills jugs
        for i in range(j):
            normal = current[1][i]
            # Fills jugs
            current[1][i] = maxJugs[i]
            if normal < maxJugs[i] and dist[tuple(current[1])] > current[0]+1:
                copy = deepcopy(current[1])
                dist[tuple(current[1])] = current[0]+1
                queue.append([current[0]+1,copy])
            # Empties jugs
            current[1][i] = 0
            if normal > 0 and dist[tuple(current[1])] > current[0]+1:
                copy = deepcopy(current[1])
                dist[tuple(current[1])] = current[0]+1
                queue.append([current[0]+1,copy])
            current[1][i] = normal
        
        # Pours from one jug into another jug
        for i in range(j):
            for k in range(j):
                if i == k:
                    continue
                # Pouring from i to k
                if current[1][i] > 0 and current[1][k] < maxJugs[k]:
                    originali = current[1][i]
                    originalk = current[1][k]
                    current[1][i] -= min(maxJugs[k] - originalk, originali)
                    current[1][k] += min(maxJugs[k] - originalk, originali)
                    if dist[tuple(current[1])] > current[0]+1:
                        copy = deepcopy(current[1])
                        dist[tuple(current[1])] = current[0]+1
                        queue.append([current[0]+1,copy])
                    current[1][i] = originali
                    current[1][k] = originalk


a()

"""
Part b:
1. fill jug B to 8
jugs:
0 8

2. fill jug A using jug B
jugs:
3 5

3. empty jug A
jugs:
0 5

4. fill jug A using jug B
jugs:
3 2

Then you have 2 oz in jug B in only 4 steps
"""

"""
Part c:
Not sure about this one, need to note that jugs are all of different size.

Potentially, just write some code to brute force it.
"""

"""
Part d:
No, this is not possible, due to the fact that you can only fully fill
and fully empty jugs, except when pouring from one jug into another, if
you don't have a jug of size 1, then you are always left with one jug that
will contain zero when all of the others contain 1 in the best situation.
"""