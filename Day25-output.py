import math
ls = None
with open("Day25-input.txt") as f:
    ls = list(map(lambda l:l.strip("\n"), f.readlines()))

def snafuToDecimal(num):
    result = 0
    conversion = {"0": 0, "1": 1, "2": 2, "-": -1, "=": -2}
    for i in num:
        result *= 5
        result += conversion[i]
        
    return result

def decimalToSnafu(num):
    digits = math.floor(math.log(num, 5)) + 2
    if num <= 5**(digits-1) // 2:
        digits -= 1
    
    snafu = ""
    for i in range(1, digits+1):
        minimum = {"q": 99**99, "digit": None}
        baseVal = 5**(digits-i)
        
        newNum = None
        if abs(num) < minimum["q"]:
            newNum = num
            minimum["q"] = abs(num)
            minimum["digit"] = "0"
        if abs(num - baseVal) < minimum["q"]:
            newNum = num - baseVal
            minimum["q"] = abs(num - baseVal)
            minimum["digit"] = "1"
        if abs(num - 2*baseVal) < minimum["q"]:
            newNum = num - 2*baseVal
            minimum["q"] = abs(num - 2*baseVal)
            minimum["digit"] = "2"
        if abs(num + baseVal) < minimum["q"]:
            newNum = num + baseVal
            minimum["q"] = abs(num + baseVal)
            minimum["digit"] = "-"
        if abs(num + 2*baseVal) < minimum["q"]:
            newNum = num + 2*baseVal
            minimum["q"] = abs(num + 2*baseVal)
            minimum["digit"] = "="
        
        snafu += minimum["digit"]
        num = newNum
    
    return snafu
    

total = 0
for i in range(len(ls)):
    total += snafuToDecimal(ls[i])

print("Star 1:", decimalToSnafu(total))

v = 0
for i in range(len(ls)):
    l = ls[i]

print("star 2:", v)