def a():
    from math import comb
    # comb is basically the choose function

    n = int(input())
    # Numbers come after letters in the alphabet here
    # Looked at solution because I was not doing well

    # Basically I needed to know that the choose function would be useful and the knowledge of the comb function in math

    # This stores the alphabet and numbers in the right order
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    def process(n,length,current = ""):
        # This is the terminating condition in our recursion
        if length == 0:
            return current
        # This gets the index of the first character that could be added to the string
        start = alpha.index(current[-1])+1 if current else 0
        # This tests all of the combos with each of the indexes
        for i in range(start,36):
            # combos is how many combos there are after this one, the options after
            combos = comb(36 - i - 1, length-1)
            # If this condition is satisfied then this value of i is the right character
            if combos >= n:
                return process(n,length-1, current + alpha[i])
            # Otherwise just reduce n by the combos, as we are discarding the other combos
            n -= combos

    # This little loop figures out the how many characters long the password is going to be using comb
    length = 1
    while comb(36,length) < n:
        n -= comb(36,length)
        length += 1

    # We then process the password with what we know is the right length
    print(process(n, 36))

a()

"""
Part b:
(first) 14, BIO, NTU, ABCDE, BIO14 (last)
"""

"""
Part c:
sum(comb(36,i) for i in range(1,37))
This gets all the of the combinations possible
68719476735
"""

"""
Part d:
As two adjacent passwords must either have the same length of the second one is one character longer than the first,
if the first password has less than 18 characters then the second password must have 19+ characters to include all 36,
however this wouldn't make them adjacent because there would be combinations inbetween, this means both passwords must
have 18 characters.

As the passwords are ordered the first password must contain A, due to this the first password has to be the last password
beginning with A, this leads to the passwords: ATUVWXYZ0123456789 and BCDEFGHIJKLMNOPQRS that work
"""