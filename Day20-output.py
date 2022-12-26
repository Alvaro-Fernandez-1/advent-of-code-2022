import copy

ls = None
with open("Day20-input.txt") as f:
    ls = list(map(lambda l:l.strip("\n"), f.readlines()))

def I(list_):
    for i in range(len(list_)):
        list_[i] = int(list_[i])
    return list_

def F(list_):
    for i in range(len(list_)):
        list_[i] = float(list_[i])
    return list_

def P(string, a, b):
    return [string[i] for i in range(a, len(string), b)]

class Nd(object):
    def __init__(self, data=None):
        self.data = data
        self.children = []

    def add(self, obj):
        self.children.append(obj)

I(ls)
for i in range(len(ls)):
    ls[i] = {"num": ls[i], "ind": i}

newArray = copy.deepcopy(ls)

for i in range(len(ls)):
    realInd = newArray.index(ls[i])
    temp = newArray[realInd]
    del newArray[realInd]
    newInd = realInd + temp["num"]
    newInd = newInd % (len(ls)-1)
    newInd = newInd % (len(ls))
    newArray.insert(newInd, temp)

for i in range(len(newArray)):
    newArray[i] = newArray[i]["num"]

zero = newArray.index(0)
value = newArray[(zero + 1000) % len(newArray)]
value += newArray[(zero + 2000) % len(newArray)]
value += newArray[(zero + 3000) % len(newArray)]

print("Star 1:", value)

ls = list(map(lambda x:{"num": x["num"] * 811589153, "ind": x["ind"]}, ls))
newArray = copy.deepcopy(ls)

for j in range(10):
    for i in range(len(ls)):
        realInd = newArray.index(ls[i])
        temp = newArray[realInd]
        del newArray[realInd]
        newInd = realInd + temp["num"]
        newInd = newInd % (len(ls)-1)
        newArray.insert(newInd, temp)

for i in range(len(newArray)):
    newArray[i] = newArray[i]["num"]

zero = newArray.index(0)
value = newArray[(zero + 1000) % len(newArray)]
value += newArray[(zero + 2000) % len(newArray)]
value += newArray[(zero + 3000) % len(newArray)]

print("star 2:", value)