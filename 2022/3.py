# Just taking the inputs
n, desired = input().split()
length = len(n)
desired = int(desired)

# Setting up the value and filled arrays
value = [ord(i)-97 for i in n]
filled = [0 for i in n]

# Deciding the order in which the letters will be processed
turns = {}
for i in range(length):
    turns[value[i]] = i

# Stores how many ways each choice can be made
ways = []
totalWays = 1
# Processing the possibilites
for i in range(length):
    current = turns[i]
    back = current-1
    while back >= 0 and filled[back]:
        back -= 1

    ways.append(current-back)
    totalWays *= (current-back)
    filled[turns[i]] = 1

# Gets the waysSum array
waysSum = [1 for i in range(length)]
for i in range(length):
    for j in range(i+1,length,1):
        waysSum[i] *= ways[j]

# We store the current which keep track of what choices we have made
current = 0
# This stores the output
out = [0 for i in range(length)]
# This loops through all of the letters in alphabetical order
for i in range(length):
    # This loops through the choices that could be made
    for j in range(ways[i]):
        # This evaluates if the current choice is the right one to make
        if current + (j+1) * waysSum[i] >= desired:
            out[i] = turns[i] - ways[i] + j + 1
            current += j*waysSum[i]
            break

# This just prints the output
print("".join([chr(i+65) for i in out]))

