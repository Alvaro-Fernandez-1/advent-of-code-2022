ls = None
with open("Day24-input.txt") as f:
    ls = list(map(lambda l:l.strip("\n"), f.readlines()))

valley = []
possible = []
for i in range(len(ls)):
    valley.append([0] * (len(ls[0])-2))
    possible.append([0] * (len(ls[0])-2))

possible[0][0] = 1

for i in range(1, len(ls)):
    l = ls[i][1:-1]
    
    for j in range(len(l)):
        valley[i][j] = {}
        if l[j] == ".":
            valley[i][j]["q"] = 0
        else:
            valley[i][j]["q"] = 1
        
        valley[i][j]["d"] = []
        if l[j] != ".":
            valley[i][j]["d"].append(l[j])

def moveSquare(i, j, newValley):
    global valley
    square = valley[i][j]
    for k in range(square["q"]):
        d = square["d"][k]
        if d == "<":
            if j > 0:
                newValley[i][j-1]["q"] += 1
                newValley[i][j-1]["d"].append(d)
            else:
                newValley[i][-1]["q"] += 1
                newValley[i][-1]["d"].append(d)
        
        if d == ">":
            if j < len(valley[0])-1:
                newValley[i][j+1]["q"] += 1
                newValley[i][j+1]["d"].append(d)
            else:
                newValley[i][0]["q"] += 1
                newValley[i][0]["d"].append(d)
        
        if d == "v":
            if i < len(valley)-2:
                newValley[i+1][j]["q"] += 1
                newValley[i+1][j]["d"].append(d)
            else:
                newValley[1][j]["q"] += 1
                newValley[1][j]["d"].append(d)
        
        if d == "^":
            if i > 1:
                newValley[i-1][j]["q"] += 1
                newValley[i-1][j]["d"].append(d)
            else:
                newValley[-2][j]["q"] += 1
                newValley[-2][j]["d"].append(d)
        
        
def moveValley():
    global valley
    newValley = []
    for i in range(len(valley)):
        newValley.append(valley[i].copy())
        for j in range(len(valley[0])):
            newValley[i][j] = {"q": 0, "d": []}
    
    for i in range(1, len(valley)-1):
        row = valley[i]
        for j in range(len(row)):
            moveSquare(i, j, newValley)
    valley = newValley

def updatePossible():
    global possible
    global valley
    newPossible = []
    for i in range(len(possible)):
        newPossible.append(possible[i].copy())

    for i in range(len(possible)):
        for j in range(len(possible[0])):
            if possible[i][j] == 0:
                continue
            if i >= 2 or (i == 1 and j == 0):
                newPossible[i-1][j] = 1
            if i < len(possible)-2 or (j == len(possible[0])-1 and i < len(possible)-1):
                newPossible[i+1][j] = 1
            if j != len(possible[0])-1 and i != 0:
                newPossible[i][j+1] = 1
            if j != 0 and i != len(possible)-1:
                newPossible[i][j-1] = 1
    
    for i in range(len(possible)):
        for j in range(len(possible[0])):
            if valley[i][j]["q"] != 0:
                newPossible[i][j] = 0
    
    possible = newPossible
            
counter = 0
while True:
    counter += 1
    moveValley()
    updatePossible()
    if possible[-1][-1] == 1:
        break

print("Star 1:", counter)

valley = []
possible = []
for i in range(len(ls)):
    valley.append([0] * (len(ls[0])-2))
    possible.append([0] * (len(ls[0])-2))

possible[0][0] = 1

for i in range(1, len(ls)):
    l = ls[i][1:-1]
    
    for j in range(len(l)):
        valley[i][j] = {}
        if l[j] == ".":
            valley[i][j]["q"] = 0
        else:
            valley[i][j]["q"] = 1
        
        valley[i][j]["d"] = []
        if l[j] != ".":
            valley[i][j]["d"].append(l[j])

now = 0
counter = 0
while True:
    counter += 1
    moveValley()
    updatePossible()
    if now == 0 and possible[-1][-1] == 1:
        now = 1
        possible = []
        for i in range(len(ls)):
            possible.append([0] * (len(ls[0])-2))
        possible[-1][-1] = 1
    
    if now == 1 and possible[0][0] == 1:
        now = 2
        possible = []
        for i in range(len(ls)):
            possible.append([0] * (len(ls[0])-2))
        possible[0][0] = 1
    
    if now == 2 and possible[-1][-1] == 1:
        break

print("star 2:", counter)