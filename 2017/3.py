p, h, n, w = [int(i) for i in input().split(" ")]
# p is the number of parcels
# i is the weight of the items
# n is the total number of items
# w is the weight of each parcel
# I think that you can just do it with dynamic programming
# I think that you can but I just don't know how to
# I will do this by making a list of sets of sorted tuples
# Current solution gets 19/25 marks because it is very inefficient
# Looked at a solution where it used recursion

totals = [set() for i in range(w+1)]

totals[0].add(tuple())

for i in range(1,w+1):
    for j in range(1,h+1):
        if j <= i:
            for k in totals[i-j]:
                if len(k) + 1 <= n:
                    totals[i].add(tuple(sorted(k+(j,))))

# I think that I need to loop over totals[w] and search for valid pairs
# At the moment p dictates the number of nested for loops
current = list(totals[w])
good = 0
if p == 1:
    for i in range(len(current)):
        if len(current[i]) == n:
            good += 1
elif p == 2:
    for i in range(len(current)):
        for j in range(len(current)):
            if len(current[i]) + len(current[j]) == n:
                good += 1
elif p == 3:
    for i in range(len(current)):
        for j in range(len(current)):
            for k in range(len(current)):
                if len(current[i]) + len(current[j]) + len(current[k]) == n:
                    good += 1
elif p == 4:
    for i in range(len(current)):
        for j in range(len(current)):
            for k in range(len(current)):
                for l in range(len(current)):
                    if len(current[i]) + len(current[j]) + len(current[k]) + len(current[l]) == n:
                        good += 1
elif p == 5:
    for i in range(len(current)):
        for j in range(len(current)):
            for k in range(len(current)):
                for l in range(len(current)):
                    for a in range(len(current)):
                        if len(current[i]) + len(current[j]) + len(current[k]) + len(current[l]) + len(current[a]) == n:
                            good += 1
print(good)