from itertools import permutations
from queue import PriorityQueue
def a():
    n = input()

    # I think that this is just a dijkstra's problem

    # This sets up the distances to all of the permutations
    INF = 1e9
    dist = {}
    for i in permutations("1234567"):
        dist["".join(i)] = INF

    # This sets up the priority queue
    queue = PriorityQueue()
    queue.put([0,n])

    # This just runs through the queue until it finds the answer
    while not queue.empty():
        current = queue.get()
        if current[1] == "1234567":
            print(current[0])
            break

        # This generates all of the possible moves
        left = current[1][1:4] + current[1][0] + current[1][4:]
        right = current[1][0:3] + current[1][-1] + current[1][3:6]
        midl = current[1][3] + current[1][:3] + current[1][4:]
        midr = current[1][:3] + current[1][4:] + current[1][3]
        moves = [left,right,midl,midr]
        for i in moves:
            if dist[i] > current[0] + 1:
                dist[i] = current[0] + 1
                queue.put([current[0]+1,i])

# a()

"""
Part b:
There are 10 different orderings that take 2 operations.
There are 334 different orderings that take 6 operations.
"""

def b():
    out = {}
    for i in range(15):
        out[i] = 0
    count = 0
    fourteen = []
    for j in permutations("1234567"):
        count += 1
        if not count % 100:
            print(count)
        n = "".join(j)
        INF = 1e9
        dist = {}
        for i in permutations("1234567"):
            dist["".join(i)] = INF

        # This sets up the priority queue
        queue = PriorityQueue()
        queue.put([0,n])

        # This just runs through the queue until it finds the answer
        while not queue.empty():
            current = queue.get()
            if current[1] == "1234567":
                out[current[0]] += 1
                if current[0] == 14:
                    fourteen.append(n)
                break

            # This generates all of the possible moves
            left = current[1][1:4] + current[1][0] + current[1][4:]
            right = current[1][0:3] + current[1][-1] + current[1][3:6]
            midl = current[1][3] + current[1][:3] + current[1][4:]
            midr = current[1][:3] + current[1][4:] + current[1][3]
            moves = [left,right,midl,midr]
            for i in moves:
                if dist[i] > current[0] + 1:
                    dist[i] = current[0] + 1
                    queue.put([current[0]+1,i])
    print(out)
    print(fourteen)

# b()

"""
Part c:
5674321 and 7654123 both take 14 operations to get to the final ending
"""

"""
Part d:
The maximum spanning distance of a graph can be determined from the furthest point
from any point, and then the furthest point from that point. I am going to do this
using code, if the maximum distance is 14, then it is not possible to select orders
that make more operations required than the hardest case.

With a brute force search from both 5674321 and 7654123, still the longest number
of operations required was 14, therefore there is no possible way to select the
orders to get more operations required than the hardest case when the starting
position is chosen(14).
"""

def d():
    count = 0
    longest = 0
    for j in ["5674321","7654123"]:
        for k in permutations("1234567"):
            count += 1
            if not count % 100:
                print(count)
            n = "".join(k)
            INF = 1e9
            dist = {}
            for i in permutations("1234567"):
                dist["".join(i)] = INF

            # This sets up the priority queue
            queue = PriorityQueue()
            queue.put([0,n])

            # This just runs through the queue until it finds the answer
            while not queue.empty():
                current = queue.get()
                if current[1] == j:
                    longest = max(longest, current[0])
                    break

                # This generates all of the possible moves
                left = current[1][1:4] + current[1][0] + current[1][4:]
                right = current[1][0:3] + current[1][-1] + current[1][3:6]
                midl = current[1][3] + current[1][:3] + current[1][4:]
                midr = current[1][:3] + current[1][4:] + current[1][3]
                moves = [left,right,midl,midr]
                for i in moves:
                    if dist[i] > current[0] + 1:
                        dist[i] = current[0] + 1
                        queue.put([current[0]+1,i])
    print(longest)

# d()
