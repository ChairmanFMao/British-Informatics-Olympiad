n = input()

original = int(n)

# They both now cater for all of the edge cases
# I had it such that one edge case didn't work because I forgot
# to reverse one bit, need to debug more throughly

l = len(n)//2
if len(n)&1:
    n = n[0:l] + n[l] + n[0:l][::-1]
    if int(n) <= original:
        if n[l] != "9":
            n = n[0:l] + str(int(n[l])+1) + n[0:l][::-1]
        else:
            n = str(int(n[0:l+1])+1) + str(int(n[0:l+1])+1)[::-1][1:]
else:
    n = n[0:l] + n[0:l][::-1]
    if int(n) <= original:
        if len(str(int(n[0:l])+1)) > len(n[0:l]):
            n = str(int(n[0:l])+1)[0:l] + str(int(n[0:l])+1)[::-1]
        else:
            n = str(int(n[0:l])+1) + str(int(n[0:l])+1)[::-1]

print(n)

""" part b
I think that you need to do this analytically
99999999988000000000, 9 9s 2 8s 9 0s
this answer is not correct
we should go from a palindrome to another palindrome
11000000000, is the correct answer
"""

""" part c
this could be done with dynamic programming
def palindrome(n):
    s = str(n)
    return s[0:len(s)//2] == s[len(s)//2:][::-1] if len(s)%2 == 0 else s[0:len(s)//2] == s[len(s)//2+1:][::-1]

dp = [[0,0,0] for i in range(100000)]
dp[0][0] = 1

palindromes = []
for i in range(100000):
    if palindrome(i):
        palindromes.append(i)

for i in range(100000):
    for j in range(2):
        if not dp[i][j]:
            continue
        for k in palindromes:
            if i+k >= 100000:
                break
            else:
                dp[i+k][j+1] |= dp[i][j]

out = 0
for i in range(1,100000):
    out += 0 if dp[i][2] else 1

print(out)

8203, this is apparently wrong
I now get 9030 which is correct because I forgot another reverse
"""

