# Decided to look at some solutions for ideas as I was stumped
# The solution itself is very simple, just need to fully understand problem
# I have been having trouble with the 1 problems, they aren't that difficult it's just that I don't think in the right way

from functools import lru_cache

def a():
    s = input()

    @lru_cache(maxsize=None)
    def countWays(testing):
        out = 0
        for i in range(1,len(testing)//2+1):
            if testing[:i] == testing[-i:]:
                out += 1 + countWays(testing[i:-i])
        return out

    print(countWays(s))

"""
Part b:
A ABCBA A
AA BCB AA
AAB C BAA
A A BCB A A
A A B C B A A
"""

"""
Part c:
The block palindrome needs to just be a word repeated twice as this is the only way to get an even
number of blocks, therefore it needs to have an even number of characters, as 2 times any number is
even. There can also only be one possible way of grouping the characters as if there is more than
one possible grouping, at least one grouping contains more than two blocks. A grouping containing
more than 2 blocks can be changed into a grouping containing the first block, last block and all
the middle blocks joined together, this leads to 3 blocks and contradicts the requirement that all
of the groupings of the block must contain an even number of blocks.
"""