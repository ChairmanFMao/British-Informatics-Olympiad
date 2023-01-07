# decrypting the string rather than encrypting it

def decrypt(s):
    out = [0 for i in range(len(s))]
    out[0] = ord(s[0])-64

    for i in range(len(s)-1,0,-1):
        tmp = (ord(s[i])-64) - (ord(s[i-1])-64)
        while tmp < 1:
            tmp += 26
        while tmp > 26:
            tmp -= 26

        out[i] = tmp

    return "".join([chr(i+64) for i in out])

def encrypt(s):
    out = [ord(s[0])-64]
    for i in range(1,len(s)):
        tmp = ord(s[i])-64 + out[-1]
        while tmp < 1:
            tmp += 26
        while tmp > 26:
            tmp -= 26

        out.append(tmp)

    return "".join([chr(i+64) for i in out])

#""" part a
s = input()
print(decrypt(s))
#"""

""" part b
ZZZZZ
"""

""" part c
out = 1
s = encrypt("OLYMPIAD")
while s != "OLYMPIAD":
    s = encrypt(s)
    out += 1

print(out)

104 times
#"""

""" part d
just find the periodicity of each 3 letter string
then check if 1e12-1 is a multiple

val = int(1e12)-1

def period(s):
    original = s
    out = 1
    s = encrypt(s)
    while s != original:
        s = encrypt(s)
        out += 1
    return out

out = 0

def dfs(current):
    if len(current) >= 3:
        global val, out
        out += 0 if val%period(current) else 1
        return

    for i in range(26):
        dfs(current+chr(i+65))

dfs("")
print(out)

4394
#"""

