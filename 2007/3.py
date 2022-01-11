# This would be impossible to brute force

t = input()
s, p = [int(i) for i in input().split()]

# Unsure of what strategy to use

out = [0,0,0,0,0]

def move(current):
    return [current[1],current[0]+current[1],current[2]+current[3],current[2]+current[3],current[4]+current[4]]

current = [0,0,0,0,0]
for i in t:
    current[ord(i)-65] += 1


