def a():
    s, n = [int(i) for i in input().split()]

    # I think that you can use dynamic programming here
    # The number of ways to make the arrangments just goes up in powers of 2
    # I think that you could find the number of numbers using pascal's triangle

    # This code finds the number of numbers that make up the combination

    n -= 1
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
ten blocks - 3
eleven blocks - 2
twelve blocks - 2
thirteen blocks - 2
fourteen blocks - 2
fifteen blocks - 2
sixteen blocks - 2
seventeen blocks - 1
eightteen blocks - 1
nineteen blocks - 1
twenty blocks - 1
and 12 more blocks

The sum of all these is:
114 blocks
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
