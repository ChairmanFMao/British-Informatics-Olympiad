from itertools import permutations
from collections import deque

def a():
    d = int(input())
    s = input()

    # This is the driver code that will run the bfs
    # Currently this works however it takes like nearly 2 seconds for the longest test case
    # Probably just due to my laptop's slow processor honestly
    longest = 0
    seen = set()
    queue = []
    queue.append([0,s])
    # This keeps the loop running while there are still permutations to be explored
    while len(queue) > 0:
        longest = queue[0][0]
        current = queue.pop(0)
        seen.add(current[1])

        change = current[1]
        ints = [int(i) for i in change]

        # This caters for the edge cases of the start and end
        if len(change) > 2:
            big = max(ints[0], ints[1])
            small = min(ints[0], ints[1])
            if ints[2] < big and ints[2] > small:
                if (change[1] + change[0] + change[2:]) not in seen:
                    queue.append([current[0]+1,change[1] + change[0] + change[2:]])
            
            length = len(ints)
            big = max(ints[length-1],ints[length-2])
            small = min(ints[length-1],ints[length-2])
            if ints[length-3] < big and ints[length-3] > small:
                if (change[:length-2] + change[length-1] + change[length-2]) not in seen:
                    queue.append([current[0]+1,change[:length-2] + change[length-1] + change[length-2]]) 
        # This loop goes over all of the middle numbers
        for i in range(1,len(change)-2):
            # This checks if the number before is in the range of the two current numbers
            big = max(ints[i],ints[i+1])
            small = min(ints[i],ints[i+1])
            if (ints[i-1] < big and ints[i-1] > small) or (ints[i+2] < big and ints[i+2] > small):
                if (change[:i] + change[i+1] + change[i] + change[i+2:]) not in seen:
                    queue.append([current[0]+1, change[:i] + change[i+1] + change[i] + change[i+2:]])

    print(longest)

"""
Part b:
To find this distance we will find the furthest node from the start,
then we will find the furthest node from this furthest node and that is the longest
distance within the graph. Simply, finding the diameter of the graph.

326451 : 7
183654792 : 16
"""

def b(s):
    longest = 0
    out = s
    seen = set()
    queue = []
    queue.append([0,s])
    while len(queue) > 0:
        longest = queue[0][0]
        out = queue[0][1]
        current = queue.pop(0)
        seen.add(current[1])

        change = current[1]
        ints = [int(i) for i in change]

        if len(change) > 2:
            big = max(ints[0], ints[1])
            small = min(ints[0], ints[1])
            if ints[2] < big and ints[2] > small:
                if (change[1] + change[0] + change[2:]) not in seen:
                    queue.append([current[0]+1,change[1] + change[0] + change[2:]])
            
            length = len(ints)
            big = max(ints[length-1],ints[length-2])
            small = min(ints[length-1],ints[length-2])
            if ints[length-3] < big and ints[length-3] > small:
                if (change[:length-2] + change[length-1] + change[length-2]) not in seen:
                    queue.append([current[0]+1,change[:length-2] + change[length-1] + change[length-2]]) 
        for i in range(1,len(change)-2):
            big = max(ints[i],ints[i+1])
            small = min(ints[i],ints[i+1])
            if (ints[i-1] < big and ints[i-1] > small) or (ints[i+2] < big and ints[i+2] > small):
                if (change[:i] + change[i+1] + change[i] + change[i+2:]) not in seen:
                    queue.append([current[0]+1, change[:i] + change[i+1] + change[i] + change[i+2:]])

    return [longest,out]

# These are the lines of code that produce the diameter of the graphs created
# print(b(b("326451")[1])[0])
# print(b(b("183654792")[1])[0])

"""
Part c:
I think that I should just generate all permuatations of 1-9 and if they are
equivalent to any other number, get the all the elements in the set and add then to used
then return 1 for the element that represents that set, and 0 if the element is already used in a set.
We are basically counting the number of strongly connected components in the graph. The graph is also
undirected.

Thinking of using Kosaraju's algorithm to try to indentify the strongly connected components.
Actually, this is not needed as the graph is undirected, the code below should work but, it is 
quite inefficient. Better idea is to remove all of the seen elements from the tuple that we are
searching as it should remove the need for the big set and make it so that less elements need to
be processed.

12345 : 26
123456789 : 2620
The second one is still quite slow but it only took like 10 mins which is fine honestly
"""

def c(s):
    seen = set()
    queue = deque([])
    queue.append((0,s))
    while len(queue) > 0:
        current = queue.popleft()
        seen.add(current[1])

        change = current[1]
        ints = [int(i) for i in change]

        if len(change) > 2:
            big = max(ints[0], ints[1])
            small = min(ints[0], ints[1])
            if ints[2] < big and ints[2] > small:
                if (change[1] + change[0] + change[2:]) not in seen:
                    queue.append((current[0]+1,change[1] + change[0] + change[2:]))
            
            length = len(ints)
            big = max(ints[length-1],ints[length-2])
            small = min(ints[length-1],ints[length-2])
            if ints[length-3] < big and ints[length-3] > small:
                if (change[:length-2] + change[length-1] + change[length-2]) not in seen:
                    queue.append((current[0]+1,change[:length-2] + change[length-1] + change[length-2])) 
        for i in range(1,len(change)-2):
            big = max(ints[i],ints[i+1])
            small = min(ints[i],ints[i+1])
            if (ints[i-1] < big and ints[i-1] > small) or (ints[i+2] < big and ints[i+2] > small):
                if (change[:i] + change[i+1] + change[i] + change[i+2:]) not in seen:
                    queue.append((current[0]+1, change[:i] + change[i+1] + change[i] + change[i+2:]))

    return seen

def c_1(number):
    things = set("".join(i) for i in permutations(number))
    count = 0
    while things:
        things -= c(things.pop())
        count += 1
        print(len(things))

    print(count)

# c_1("12345")
# c_1("123456789")