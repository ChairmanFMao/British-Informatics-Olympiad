s1, s2 = input().split()

def pat(s):
    if len(s) == 1:
        return "YES"

    # Read the question carefully and try to understand what is being asked
    # I thought that it was recursive but, I was making it more difficult than it was
    for i in range(len(s)-1):
        if min([ord(j) for j in s[0:i+1]]) > max([ord(j) for j in s[i+1:]]):
            return "YES"
    return "NO"

print(pat(s1))
print(pat(s2))
print(pat(s1+s2))