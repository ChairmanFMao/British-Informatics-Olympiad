from functools import lru_cache

# Tried a brute force implementation but it quickly timed out
# So, the key for this problem, that I realised after looking at a solution is that
# you don't need to actually store the strings, you just pass around the length, last
# character and streak. This saves lots of memory and makes the program way more efficient
# This is kinda classic combinatorics with a little twist

p, q, r = [int(i) for i in input().split()]
n = int(input())

# This function processes the number of permutations for a given prefix
@lru_cache(maxsize=None)
def perm(length,streak,alpha,q,r,last):
    # If the streak is longer than what is permitted, this string isn't valid
    if streak > q:
        return 0
    # If the length of the string is equal to the desired length and it is valid
    # it is one valid combination
    if length == r:
        return 1
    
    total = 0
    # We iterate over all of the characters in alpha and try adding them to the end
    # of our string, but we do this by just manipulating length, streak and last(i)
    for i in alpha:
        total += perm(length+1,streak + 1 if i == last else 1,alpha,q,r,i)
    return total

# This gets the characters that are valid to use in the string
letters = "ABCDEFGHIJKL"
alpha = letters[:p]

# This is just setting up some variables for later
out = ""
streak = 1
currentStreak = 1
last = None
# This is then the main driver code for the program
while len(out) < r:
    # We iterate over alpha to check what would happen if each letter was added to the string
    for i in alpha:
        # We need to have this temporary variable currentStreak so we don't override streak
        # for cases that don't work
        currentStreak = streak + 1 if i == last else 1
        # This finds how many combinations there are with the prefix with i appended
        current = perm(len(out)+1,currentStreak,alpha,q,r,i)
        # If the number of combinations is greater than n, the current letter(i) must be the
        # right one to append to the output string
        if current >= n:
            out += i
            last = i
            streak = currentStreak
            break
        # Otherwise we can just decrement n by current as we are discarding all of the combinations
        # that don't work
        n -= current

print(out)
