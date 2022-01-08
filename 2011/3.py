from math import ceil, perm
from itertools import permutations

def a():
    # Made a naive implementation first time iterating over all numbers
    # I could potentially just pregenerate all of the numbers and return the right one
    # However, I think that my code is too slow for that, it hangs with n = 10000
    # 10000th = 352951857, 100th = 9911

    n = int(input())
    bruteCopy = n

    # This function checks if a number is an upside down number
    def upsideDown(number):
        asString = str(number)
        for i in range(ceil(len(asString)/2)):
            if int(asString[i])+int(asString[-i-1])-10:
                return 0
        return 1

    # This function returns the number of combinations possible with length left characters
    def combos(length):
        return pow(9,length)

    # This is a simple brute force function I was using for debugging the main function
    def brute(n):
        count = 0
        current = 0
        while count < n:
            if upsideDown(current):
                count += 1
            current += 1
        return current-1

    # These are all the digit pairs that add up to 10
    pairs = [["1","9"],["2","8"],["3","7"],["4","6"],["5","5"],["6","4"],["7","3"],["8","2"],["9","1"]]

    count = 0
    current = 0
    length = 1
    # This loop finds the length of the number we want
    while 1:
        if combos(length >> 1) >= n:
            break
        n -= combos(length >> 1)
        length += 1

    left = ""
    # If the length is odd then the middle character has to be 5
    mid = "5" if length & 1 else ""
    right = ""
    # This loop then iterates over all the possilbe combinations and constructs the nth upside-down number
    while len(left+mid+right) < length:
        for i in range(9):
            # This checks if the current i is the right one, if so it adds it to the left and right strings
            if combos((length >> 1) - len(left) - 1) >= n:
                left += pairs[i][0]
                right = pairs[i][1] + right
                break
            # Otherwise, n is decremented by the number of combinations possible
            else:
                n -= combos((length >> 1) - len(left) - 1)

    print(left+mid+right)

# a()

"""
Part b:
384 upside down numbers for permutations of "123456789"
"""

def b():
    def upsideDown(number):
        asString = str(number)
        for i in range(ceil(len(asString)/2)):
            if int(asString[i])+int(asString[-i-1])-10:
                return 0
        return 1
    
    count = 0
    for i in permutations("123456789",9):
        if upsideDown("".join(i)):
            count += 1
    print(count)

# b()

"""
Part c:
38 digits long
"""

def c():
    def combos(length):
            return pow(9,length)

    length = 1
    n = 1000000000000000000
    while 1:
        if combos(length >> 1) >= n:
            break
        n -= combos(length >> 1)
        length += 1
    print(length)

# c()

"""
Part d:
There would be more 1001 digit upside-down numbers that contain 5 as if an upside-down number
contains an odd number of digits it must contain a 5 as the middle digit. Whereas for a upside-down
number that contains an even number of digits, the fives would only occur naturally. Leading the
1001 digit upside-down numbers to contain more fives than 1000 digit upside-down numbers.
"""