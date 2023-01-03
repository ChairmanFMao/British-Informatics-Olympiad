# you need to generate the graph as well as the algorithm that
# will traverse through the graph
# We need to output the graph and the spy's positions at P and Q

plan, p, q = input().split(); p = int(p); q = int(q)
plan = [ord(i)-65 for i in plan]
n = len(plan)+2

adj = [[] for i in range(n)]
chosen = [0 for i in range(n)]
# This does the majority of the graph generation
while len(plan):
    val = -1
    for i in range(n):
        if not chosen[i] and i not in plan:
            val = i
            break

    chosen[val] = 1
    adj[val].append([plan[0],0])
    adj[plan[0]].append([val,0])
    plan.pop(0)

# This caters for the last 2 unchosen ones
unChosen = []
for i in range(n):
    if not chosen[i]:
        unChosen.append(i)
adj[unChosen[0]].append([unChosen[1],0])
adj[unChosen[1]].append([unChosen[0],0])

# This prints the graph
for i in range(n):
    adj[i].sort()
    print("".join([chr(j[0]+65) for j in adj[i]]))

# Need to store how many times a room has been seen and how many
# times each of the edges in the graph have been used
seen = [0 for i in range(n)]
seen[0] = 1

moves = 0; out = ""; current = 0
while moves <= max(p,q):
    if moves == p or moves == q:
        out += chr(current+65)

    val = -1
    if seen[current]&1:
        val = 0
    else:
        for i in range(len(adj[current])):
            if adj[current][i][1]&1:
                val = min(i+1,len(adj[current])-1)
                break

    seen[adj[current][val][0]] += 1
    adj[current][val][1] += 1
    current = adj[current][val][0]
    moves += 1


print(out)

""" part b
for 3 rooms: A
for 6 rooms: AAAA
"""

""" part c
They can count the number of times that they have exited through
all of the connections, if this number is odd then they have
visited the room an even number of times and if this number is
even then they have visited the room and odd number of times.
This information would be sufficient to determine how many times
that they have visited the rooms and continue the exploration.
As when a spy leaves a room it increases the number of exits used
by 1, when a spy has never been in a room before it will have 0
exits used which is why an even number leads to an odd amount of
entries
"""

""" part d
This would be possible with brute force
I think that there are only 8**6 ways to choose things
and this would be computationally possible

intial code got me 46 which is wrong
I brute force all of the combinations and test them
I don't know why I don't get the right answer
I now get 54, which is the correct answer
The mark scheme is wrong here I think
"""

def process(plan):
    chosen = [0 for i in range(8)]
    edges = []
    while len(edges) < 4:
        val = -1
        # Should be 8 not n here
        for i in range(8):
            if not chosen[i] and i not in plan:
                val = i
                break

        chosen[val] = 1
        edges.append("".join(map(str,sorted([plan[0],val]))))
        plan.pop(0)

    edges.sort()
    return edges == ["04","15","26","37"]

def dfs(plan):
    if len(plan) == 6:
        return process(__import__("copy").deepcopy(plan))
    
    current = 0
    for i in range(8):
        plan.append(i)
        current += dfs(plan)
        plan.pop()
    return current

print(dfs([]))

