def a():
    n = int(input())

    def prime(number):
        if number == 2:
            return 1
        if not number & 1:
            return 0
        for i in range(3,number//2,2):
            if not number % i:
                return 0
        return 1

    out = 0
    for i in range(2,n//2 + 1):
        if prime(n-i) and prime(i):
            out += 1

    print(out)

a()

"""
Part b:
43 3
41 5
29 17
23 23
"""

def b():
    n = 46

    def prime(number):
        if number == 2:
            return 1
        if not number & 1:
            return 0
        for i in range(3,number//2,2):
            if not number % i:
                return 0
        return 1

    out = 0
    for i in range(2,n//2 + 1):
        if prime(n-i) and prime(i):
            print(n-i,i)
            out += 1

    print(out)

# b()

"""
Part c:
9 numbers
"""

def c():
    def prime(number):
        if number == 2:
            return 1
        if not number & 1:
            return 0
        for i in range(3,number//2,2):
            if not number % i:
                return 0
        return 1
    
    count = 0
    for i in range(5,51,2):
        out = 0
        for j in range(2,i//2 + 1):
            if prime(i-j) and prime(j):
                out = 1
        if not out:
            count += 1

    print(count)

# c()
