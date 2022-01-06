# Remember for question 2 to test many inputs and see if any of them result in errors
# Debugging is a key part of this question

n, w = input().split()
n = int(n)

# This creates the decode wheel from n
def decoder(n):
    second = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    out = []
    ptr = 0
    while len(second) > 0:
        ptr += n
        ptr %= len(second)
        out.append(second.pop(ptr))
    return out

wheel = decoder(n-1)

print("".join(wheel[0:6]))

# This encodes the text
out = ""
for i in range(len(w)):
    out += wheel[(i + ord(w[i])-65) % 26]

print(out)
