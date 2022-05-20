s = input()

out = "";
for i in range(len(s)-1,0,-1):
    current = ord(s[i]) - ord(s[i-1])
    if current <= 0:
        current += 26
    out += chr(current+64)

out += s[0]
out = out[::-1]
print(out)
