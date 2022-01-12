s, n = [int(i) for i in input().split()]

# I think that this is dynamic programming

# The index relates to how many drats have been thrown
dp = [[0,0,0,0,0,0,0,0,0] for i in range(201)]
# Does the first turn, for doubles
for i in range(2,41,2):
    dp[i][1] += 1

# Does all of the other turns
for i in range(1,s+1):
    for j in range(1,21):
        if i >= j:
            for k in range(8):
                dp[i][k+1] += dp[i-j][k]

print(dp[s][n])
