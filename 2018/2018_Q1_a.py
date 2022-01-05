# going to try to start to do things in python from now on as it is just much eaiser to write and debug
# Got this to work, the main problem was that I wasn't ceiling the subtotals for the interest and repayment
# I modified it into a function to do part c, should've really just created a new document
# Need to brush up on understanding question properly and truly understanding what is being asked of me

from math import ceil

def calculate(interest, repayment):
    debt = 10000
    #interest, repayment = [int(a) for a in input().split()]
    repayment /= 100
    interest /= 100
    total = 0
    while debt > 0:
        interestMonth = ceil((interest) * debt)
        debt += interestMonth
        repaid = ceil((repayment) * debt)
        repaid = min(max(5000, repaid), debt)
        total += repaid
        debt -= repaid
        if (debt > 10000):
            return 0

    return total

biggest = 0
bi = 0
bj = 0
for i in range (101):
    for j in range (101):
        if calculate(i,j) > biggest:
            biggest = calculate(i,j)
            bi = i
            bj = j

print(bi, bj)