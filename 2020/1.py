roman, n = input().split()

def toRoman(number):
    out = ""
    values = [[1000,"M"],[900,"CM"],[500,"D"],[400,"CD"],[100,"C"],[90,"XC"],[50,"L"],[40,"XL"],[10,"X"],[9,"IX"],[5,"V"],[4,"IV"],[1,"I"]]
    while number > 0:
        for i in values:
            if number >= i[0]:
                out += i[1]
                number -= i[0]
                break
    return out

def lookAndSay(s):
    out = ""
    current = s[0]
    run = 0
    for i in range(len(s)):
        if s[i] == current:
            run += 1
        else:
            out += toRoman(run) + current
            current = s[i]
            run = 1
    out += toRoman(run) + current
    return out

for i in range(int(n)):
    roman = lookAndSay(roman)

print(sum([1 for i in roman if i == "I"]),sum([1 for i in roman if i == "V"]))
