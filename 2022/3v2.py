n, p = input().split(); p = int(p)-1

n = [ord(i)-97 for i in n]

spaces = [0 for i in range(len(n))]
taken = [0 for i in range(len(n))]

# labelled in order of arrival
# gets the number of collisions possible for each
for i in range(len(n)):
    counter = 1
    while (i-counter >= 0 and n[i-counter] < n[i]):
        counter += 1

    taken[n[i]] = counter

# gets the product of later taken values
vals = [1 for i in range(len(n))]
for i in range(len(n)-2,-1,-1):
    vals[i] = vals[i+1] * taken[i+1]

# finds how many steps back each of them should take
current = []
for i in range(len(n)):
    # I had a bug here were I was starting with tmp low and then
    # incrementing it rather than making it go down
    # this led to the same answer for the sample tho
    tmp = taken[i]-1
    while vals[i] <= p:
        p -= vals[i]
        tmp -= 1

    current.append(tmp)

out = [0 for i in range(len(n))]
for i in range(len(n)):
    out[n[i]] = chr(i-current[n[i]]+65)

print("".join(out))

# My first code was initially wrong
# But I managed to amend it relatively quickly

""" part b
GHCDABEFIJ
Just done manually
"""

""" part c
it must be like
1 0 1 1 1 1 1 1 1 1 1...
and all of the other ones have to take their place in reverse
order?
15 ways by changing which one appears first

0 1 0 1 1 1 1 1 1 1 1...
this would also work for 14 more ways
0 0 1 0 1 1 1 1 1 1 1...
this would work for 13 more ways

15th triangle number
15*16/2 = 120

My first answer for this was wrong
I got this right the second try
"""

""" part d
a has to be in their preferred position
some kinda simulation might be able to do this
"""

