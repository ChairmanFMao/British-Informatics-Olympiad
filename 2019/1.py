# We increment n by one so that if it is a palindrome we don't find it
n = str(int(input()) + 1)

# This mirrors the first half of the string onto the second half
# If the string is an odd length we retain the middle character
out = list(n[:len(n)//2] + (n[len(n)//2] if len(n) & 1 else "") + n[:len(n)//2][::-1])

# If the palindrome out is less than n, we must make it bigger
if int("".join(out)) < int(n):
    # This increments the middle ascii value of out
    out[len(n)//2] = chr(ord(out[len(n)//2])+1)
    # If the length of out is even, then we must increment the two middle values
    if not len(n) & 1:
        out[len(n)//2-1] = chr(ord(out[len(n)//2-1])+1)

# If after the increment, there is a ":" in the output, this means that we have turned
# a 9 into a ":", the solution to this is to increment the first half of the n that we are
# mirroring, then mirror it again. If the lengths of the initial string and the incremented
# one are equal this means that the middle character has been turned into a zero from a 9
# and we have to put the zero there, otherwise the extra character is accounted for.
if ":" in out:
    start = str(int(n[:len(n)//2]) + 1)
    out = list(start + ("0" if len(start) == len(n[:len(n)//2]) else "") + start[::-1])

print("".join(out))

# Note:
# Sorry if this code is hard to understand, I used some complicated string manipulation.
# However, I took a shot at trying to explain all of it
