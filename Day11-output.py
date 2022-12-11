ls = None
with open("Day11-input.txt") as f:
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


monkeys = [];
monkeysNumInspect = []
monkeysNum = (len(ls) + 1)//7
for i in range(monkeysNum):
    monkeys.append({"items": [], "operation": None, "test": None, "true": None, "false": None})
    monkeysNumInspect.append(0)

for i in range(monkeysNum):
    l = ls[i*7 + 1].split()[2:]
    l = list(map(lambda x: x.strip(","), l))
    I(l)
    monkeys[i]["items"] = l
    monkeys[i]["operation"] = ls[i*7 + 2].split()[3:]
    monkeys[i]["test"] = int(ls[i*7 + 3].split()[3])
    monkeys[i]["true"] = int(ls[i*7 + 4].split()[5])
    monkeys[i]["false"] = int(ls[i*7 + 5].split()[5])

def getNum(string, old):
    if string[0] in "0123456789":
        return int(string)
    return old

def operate(monkey, old):
    op = monkeys[monkey]["operation"]
    if op[1] == "+":
        return getNum(op[0], old) + getNum(op[2], old)
    else:
        return getNum(op[0], old) * getNum(op[2], old)


for i in range(20):
    for j in range(monkeysNum):
        monkey = monkeys[j]
        monkeysNumInspect[j] += len(monkey["items"])
        for i in range(len(monkey["items"])):
            item = operate(j, monkey["items"][0])//3
            if item % monkey["test"] == 0:
                monkeys[monkey["true"]]["items"].append(item)
                del monkey["items"][0]
            else:
                monkeys[monkey["false"]]["items"].append(item)
                del monkey["items"][0]
            

monkeysNumInspect.sort()
print("Star 1:", monkeysNumInspect[-1] * monkeysNumInspect[-2])

#initialize everything again
monkeys = [];
monkeysNumInspect = []
monkeysNum = (len(ls) + 1)//7
for i in range(monkeysNum):
    monkeys.append({"items": [], "operation": None, "test": None, "true": None, "false": None})
    monkeysNumInspect.append(0)

for i in range(monkeysNum):
    l = ls[i*7 + 1].split()[2:]
    l = list(map(lambda x: x.strip(","), l))
    I(l)
    monkeys[i]["items"] = l
    monkeys[i]["operation"] = ls[i*7 + 2].split()[3:]
    monkeys[i]["test"] = int(ls[i*7 + 3].split()[3])
    monkeys[i]["true"] = int(ls[i*7 + 4].split()[5])
    monkeys[i]["false"] = int(ls[i*7 + 5].split()[5])

#numbers get really high, use modulo of product of all tests
#to keep the important info
modulo = 1
for monkey in monkeys:
    modulo *= monkey["test"]

for i in range(10000):
    for j in range(monkeysNum):
        monkey = monkeys[j]
        monkeysNumInspect[j] += len(monkey["items"])
        for i in range(len(monkey["items"])):
            item = operate(j, monkey["items"][0]) % modulo
            if item % monkey["test"] == 0:
                monkeys[monkey["true"]]["items"].append(item)
                del monkey["items"][0]
            else:
                monkeys[monkey["false"]]["items"].append(item)
                del monkey["items"][0]
            

monkeysNumInspect.sort()
print("star 2:", monkeysNumInspect[-1] * monkeysNumInspect[-2])
















