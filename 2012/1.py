def a():
    n = int(input())

    out = 1
    for i in range(2,n+1):
        if not n % i:
            out *= i
            while not n % i:
                n /= i

    print(out)

a()

"""
Part b:
10 20 40 50 80 100 160 200 250 320
"""

def b():
    valid = []
    for n in range(1000000):
        initial = n
        if len(valid) == 10:
            break
        out = 1
        for i in range(2,n+1):
            if not n % i:
                out *= i
                while not n % i:
                    n /= i

        if out == 10:
            valid.append(initial)
    
    for i in valid:
        print(i)

# b()

"""
Part c:
This function that I wrote is very inefficient, got about half way through in like an hour
"""

def c():
    end = set()
    occurs = dict()
    occurs[1] = 1
    for n in range(1,1000001):
        if n % 10000 == 0:
            print(n)
        initial = n
        out = 1
        i = 2
        while i <= n and n != 1:
            if not n % i:
                out *= i
                while not n % i:
                    n /= i
            i += 1

        end.add(initial)
        if occurs.get(initial) == None:
            occurs[initial] = 0
        occurs[initial] += 1
    print(max(occurs[i] for i in end))

# c()