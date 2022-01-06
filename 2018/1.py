from math import ceil

# Just have to read the question carefully make sure you round at the right points

i, r = [int(i) for i in input().split()]
debt = 10000
out = 0

while debt > 0:
    debt += ceil((i/100)*debt)
    takeaway = max(5000, ceil(debt * (r/100)))
    out += takeaway
    debt -= takeaway

out += debt
round(out)
print(out/100)