# Remember to remove debugging stuff when submitting

def a():
    n = int(input())

    # This function converts a number into a comparable form
    def convert(number):
        out = list(str(number))
        return sorted(out)

    works = []
    original = convert(n)

    for i in range(2,10):
        if convert(n*i) == original:
            works.append(i)

    if len(works):
        print(" ".join([str(i) for i in works]))
    else:
        print("NO")

a()

"""
Part b:
Just need to call part a with 85247910 and output all the number

28415970
17049582
14207985
"""

def b():
    n = 85247910

    # This function converts a number into a comparable form
    def convert(number):
        out = list(str(number))
        return sorted(out)

    original = convert(n)

    for i in range(2,10):
        if convert(n//i) == original:
            print(n//i)

# b()

"""
Part c:
146
"""

def c():
    count = 0
    def convert(number):
        out = list(str(number))
        return sorted(out) if len(out) == len(set(out)) else 0

    for n in range(100000,1000000):
        if n % 100000 == 0:
            print(n)
        original = convert(n)

        for i in range(2,10):
            value = convert(n*i)
            if not value:
                continue
            if value == original:
                count += 1
    print(count)

# c()