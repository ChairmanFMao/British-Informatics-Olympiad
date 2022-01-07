first, second, n = input().split()
first = ord(first)-64; second = ord(second)-64; n = int(n)

# We do it n-2 times as the first and second elements in the sequence are given to us
for i in range(n-2):
    third = first + second
    if third > 26:
        third -= 26
    first = second
    second = third

print(chr(second+64))