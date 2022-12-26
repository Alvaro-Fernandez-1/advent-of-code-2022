ls = None
with open("Day21-input.txt") as f:
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

monkeys = {}
for i in range(len(ls)):
    l = ls[i].split()
    if len(l) == 2:
        monkeys[l[0][:-1]] = int(l[1])
    else:
        monkeys[l[0][:-1]] = l[1:]

def calculate(monkey):
    global monkeys
    op = monkeys[monkey]
    if isinstance(op, int):
        return monkeys[monkey]
    if op[1] == "+":
        return calculate(op[0]) + calculate(op[2])
    if op[1] == "-":
        return calculate(op[0]) - calculate(op[2])
    if op[1] == "*":
        return calculate(op[0]) * calculate(op[2])
    if op[1] == "/":
        return calculate(op[0]) // calculate(op[2])

for monkey in monkeys:
    monkeys[monkey] = calculate(monkey)
    

print("Star 1:", monkeys["root"])

monkeys = {}
for i in range(len(ls)):
    l = ls[i].split()
    if len(l) == 2:
        monkeys[l[0][:-1]] = int(l[1])
    else:
        monkeys[l[0][:-1]] = l[1:]

path = ["humn"]
current = "humn"
while current != "root":
    for i in monkeys:
        if not isinstance(monkeys[i], int) and current in monkeys[i]:
            path.append(i)
            current = i

del path[-1]

current = path[-1]
prev = "root"
toGet = None
if monkeys["root"][0] == current:
    toGet = calculate(monkeys["root"][2])
else:
    toGet = calculate(monkeys["root"][0])

prev = current
del path[-1]

for i in path[::-1]:
    print(toGet, current)
    current = i
    op = monkeys[prev]
    print(op)
    if current == op[0]:
        if op[1] == "+":
            toGet = toGet - calculate(op[2])
        if op[1] == "-":
            toGet = toGet + calculate(op[2])
        if op[1] == "*":
            toGet = toGet // calculate(op[2])
        if op[1] == "/":
            toGet = toGet * calculate(op[2])
    if current == op[2]:
        if op[1] == "+":
            toGet = toGet - calculate(op[0])
        if op[1] == "-":
            toGet = calculate(op[0]) - toGet
        if op[1] == "*":
            toGet = toGet // calculate(op[0])
        if op[1] == "/":
            toGet = calculate(op[0]) // toGet
    
    
    print(toGet)
    print(" ")
    prev = current
    
    
print("star 2:", toGet)












