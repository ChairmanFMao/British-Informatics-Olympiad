# Read the question carefully for what the output should be
def a():
    s = input()

    digits = ["ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]
    numbers = {"ONE":1,"TWO":2,"THREE":3,"FOUR":4,"FIVE":5,"SIX":6,"SEVEN":7,"EIGHT":8,"NINE":9}

    good = 0

    for i in digits:
        sptr = 0
        dptr = 0
        while sptr < len(s) and dptr < len(i):
            if s[sptr] == i[dptr]:
                dptr += 1
            sptr += 1
        if dptr == len(i):
            good = numbers[i]

    print(good if good else "NO")

a()

"""
Part b:
I enumerated all the possible ways on paper and I think that there are 10 ways
"""

"""
Part c:
For one to five, there would need to be 12 characters
For one to nine, there would need to be 16 characters
"""

def c():
    digits = ["ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]
    out = [0 for i in range(26)]
    for i in digits:
        current = [0 for k in range(26)]
        for j in i:
            current[ord(j)-65] += 1
        for j in range(26):
            out[j] = max(out[j],current[j])
    print(sum(out))

# c()
