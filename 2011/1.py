def a():
    first, second, n = input().split()
    first = ord(first)-64; second = ord(second)-64; n = int(n)
    og = first

    # We do it n-2 times as the first and second elements in the sequence are given to us
    for i in range(n-2):
        third = first + second
        if third > 26:
            third -= 26
        first = second
        second = third

    print(chr(second+64))

a()

"""
Part b:
F is 6th letter of the alphabet
X is the 24th letter of the alphabet
The letter that would link them would be "R"

Q is the 17th letter of the alphabet
H is the 8th letter of the alphabet
The letter would link them would be "Q"
"""

"""
Part c:
I think there is a recurring sequence, we just need to find how often it repeats.
sequence:
27,11,15,3,10,15,2,1
The sum of the terms is 84 so we can do 1,000,000,000,000,000,000 mod 84 = 64
so we can just get the 64th term of the sequence.
This happens to be 11, which relates to the letter "K"
"""