def a():
    n = int(input())

    numbers = [i for i in range(1,10100,2)]

    # Need to be careful and fully look at the question before coding
    for i in range(1,len(numbers)):
        if i >= len(numbers):
            break
        if numbers[i] != 0:
            remove = []
            for j in range(numbers[i]-1,len(numbers),numbers[i]):
                remove.append(numbers[j])
            for j in remove:
                numbers.remove(j)

    left = n-1
    right = n+1
    while left not in numbers:
        left -= 1
    while right not in numbers:
        right += 1

    print(left, right)

a()

"""
Part b:
According to the function below there are 23 lucky numbers below 100
"""

def b(cap):
    numbers = [i for i in range(1,cap,2)]

    for i in range(1,len(numbers)):
        if i >= len(numbers):
            break
        if numbers[i] != 0:
            remove = []
            for j in range(numbers[i]-1,len(numbers),numbers[i]):
                remove.append(numbers[j])
            for j in remove:
                numbers.remove(j)
    
    print(len(numbers))

# b(100)

"""
Part c:
Obviously not possible to brute force. Not really sure how to go about this problem
Looked at a solution and they just probed the set to see answers and found a formula that worked
Used by own code to find the pattern, it is 2n - 2.

So for 1,000,000,000 th lucky number, there would be 1,999,999,998 pairs
"""

def c():
    for j in range(10,100,10):
        numbers = [i for i in range(1,j,2)]

        for i in range(1,len(numbers)):
            if i >= len(numbers):
                break
            if numbers[i] != 0:
                remove = []
                for j in range(numbers[i]-1,len(numbers),numbers[i]):
                    remove.append(numbers[j])
                for j in remove:
                    numbers.remove(j)
        
        number = numbers[len(numbers)-2]
        pairs = set()
        for i in range(2,number+1):
            left = i-1
            right = i+1
            while left not in numbers:
                left -= 1
            while right not in numbers:
                right += 1
            pairs.add((left,right))
        print(len(pairs), len(numbers)-1)

# c()