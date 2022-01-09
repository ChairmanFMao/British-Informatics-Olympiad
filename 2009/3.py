# Read question fully, blocks only from 1 to 9, misinterpreted problem in a bad way
# My current code works if all values of blocks are allowed, changed code to work properly

def a():
    s, n = [int(i) for i in input().split()]

    # I think that you can use dynamic programming here
    # This generates the number of combinations to generate a total using dp
    dp = [0 for i in range(s+1)]
    dp[0] = 1
    for i in range(1,s+1):
        for j in range(1,10):
            if i >= j:
                dp[i] += dp[i-j]
    
    out = []
    # This keeps the loop going until the total is reached
    while sum(out) < s:
        # This loops through all of the possible ancestors
        for i in range(1,s-sum(out)+1):
            # If the number of solutions is less than n, it isn't right so we decrement n
            if n > dp[s-i-sum(out)]:
                n -= dp[s-i-sum(out)]
            # Otherwise, the number is right, we append it to out and continue further
            else:
                out.append(i)
                break
    
    print(" ".join([str(i) for i in out]))

a()

"""
Part b:
one blocks - 32
two blocks - 16
three blocks - 10
four blocks - 8
five blocks - 6
seven blocks - 4
eight blocks - 4
nine blocks - 3

The sum of all these is:
88 blocks
"""

"""
Part c:
The last number in the dictionary contains one, the first number in the dictionary
number of times, the first number in the dictionary will always be the target sum
of the list, this is because that number will have the smallest number of digits,
therefore it is the smallest number and will be first in the list. The last number
in the list has the most number of digits out of all the of the numbers as it leads
to creating the largest number so, to get the largest number of digits, we represent
the number as all ones, leading to one repeated the first number of times.
"""

"""
Part d:
It will be possible to brute force the sum to 8, but I will need to make an observation
of a pattern to do the sum to 50.

With the sum to 4, there are 4 palindromic arrangements.
With the sum to 8, there are 16 palindromic arrangements.
Honestly, it seems quite random, and I am not sure about the answer for the sum to 50
"""

def d():
    def palindrome(number):
        for i in range(len(number)//2):
            if number[i] != number[-i-1]:
                return 0
        return 1

    palindromes = 0
    s = 8
    for n in range(1,pow(2,s-1)+1):
        power = s-2
        current = 0
        out = []
        # This makes the loop continue until finished
        while sum(out) < s:
            count = 0
            # Loops over the powers of 2 from big to small
            for i in range(power,-2,-1):
                # Prevents pow(2,-1)
                if i == -1:
                    i = 0
                count += 1
                # Checks if the current one is right
                if current + pow(2,i) > n:
                    out.append(count)
                    power -= count
                    break
                current += pow(2,i)
        palindromes += palindrome("".join([str(i) for i in out]))
    
    print(palindromes)

# d()
