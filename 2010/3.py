# Currently solution is quite inefficient and just dies with larger input

from copy import deepcopy

def a():
    j, n = [int(i) for i in input().split()]
    # The first number in the list is the capacity, the second is how much it is filled
    jugs = [[int(i),0] for i in input().split()]

    # I think the strategy is to just do a bfs, there are only like 3 operations possible at each stage
    # I don't think that Dijkstra's is applicable as the states are too varied, not sure how well this
    # is going to do with bigger test cases

    # This stores all of the information about a current state
    class State:
        def __init__(self, jugs, moves):
            self.jugs = deepcopy(jugs)
            self.moves = moves

    finished = 0
    queue = [State(jugs,0)]
    while len(queue) > 0:
        current = queue.pop(0)
        # This checks if any the current jugs have n oz in them
        for i in range(j):
            if current.jugs[i][1] == n:
                print(current.moves)
                finished = 1
                break
        if finished:
            break
        
        # This fills jugs from other jugs
        for i in range(j):
            for k in range(j):
                if i == k:
                    continue
                if current.jugs[i][0] > current.jugs[i][1] and current.jugs[k][1] > 0:
                    copy = State(current.jugs,current.moves+1)
                    copy.jugs[i][1] += min(current.jugs[i][0] - current.jugs[i][1], current.jugs[k][1])
                    copy.jugs[k][1] -= min(current.jugs[i][0] - current.jugs[i][1], current.jugs[k][1])
                    queue.append(copy)

        # This fills and empties jugs
        for i in range(j):
            # This fills up the jug if possible
            if current.jugs[i][0] > current.jugs[i][1]:
                copy = State(current.jugs,current.moves+1)
                copy.jugs[i][1] = copy.jugs[i][0]
                queue.append(copy)
            # This empties a jug if possible
            if current.jugs[i][1] > 0:
                copy = State(current.jugs,current.moves+1)
                copy.jugs[i][1] = 0
                queue.append(copy)

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
Not sure about this one
"""

"""
Part d:
No, this is not possible, due to the fact that you can only fully fill
and fully empty jugs, except when pouring from one jug into another, if
you don't have a jug of size 1, then you are always left with one jug that
will contain zero when all of the others contain 1 in the best situation.
"""