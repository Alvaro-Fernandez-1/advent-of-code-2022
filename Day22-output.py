ls = None
with open("Day22-input.txt") as f:
    ls = list(map(lambda l:l.strip("\n"), f.readlines()))

class Nd(object):
    def __init__(self, data=None):
        self.data = data
        self.children = []

    def add(self, obj):
        self.children.append(obj)

jungle = ls[:-2]
pwd = ls[-1]
directions = []
while True:
    if pwd[0] == "R" or pwd[0] == "L":
        directions.append(pwd[0])
        pwd = pwd[1:]
    elif "R" in pwd and (not "L" in pwd or pwd.index("R") < pwd.index("L")):
        directions.append(int(pwd[:pwd.index("R")]))
        pwd = pwd[pwd.index("R"):]
    elif "L" in pwd and (not "R" in pwd or pwd.index("L") < pwd.index("R")):
        directions.append(int(pwd[:pwd.index("L")]))
        pwd = pwd[pwd.index("L"):]
    else:
        directions.append(int(pwd))
        break

#pad jungle
for i in range(len(jungle)):
    jungle[i] = jungle[i] + " " * 50

def move(num):
    global jungle
    global direction
    global pos
    posCopy = pos.copy()
    for i in range(num):
        if direction == "R":
            next_ = posCopy[1]
            if next_+1 >= len(jungle[posCopy[0]]) or jungle[posCopy[0]][next_+1] == " ":
                while next_ > 0 and jungle[posCopy[0]][next_-1] in ".#":
                    next_ -= 1
            else:
                next_ += 1
            
            if jungle[posCopy[0]][next_] == "#":
                break
            else:
                posCopy[1] = next_
        
        if direction == "L":
            next_ = posCopy[1]
            if next_-1 < 0 or jungle[posCopy[0]][next_-1] == " ":
                while next_ < len(jungle[posCopy[0]])-1 and jungle[posCopy[0]][next_+1] in ".#":
                    next_ += 1
            else:
                next_ -= 1
            
            if jungle[posCopy[0]][next_] == "#":
                break
            else:
                posCopy[1] = next_
        
        if direction == "U":
            next_ = posCopy[0]
            if next_-1 < 0 or jungle[next_-1][posCopy[1]] == " ":
                while next_ < len(jungle)-1 and jungle[next_+1][posCopy[1]] in ".#":
                    next_ += 1
            else:
                next_ -= 1
            
            if jungle[next_][posCopy[1]] == "#":
                break
            else:
                posCopy[0] = next_
                
        if direction == "D":
            next_ = posCopy[0]
            if next_+1 >= len(jungle) or jungle[next_+1][posCopy[1]] == " ":
                while next_ > 0 and jungle[next_-1][posCopy[1]] in ".#":
                    next_ -= 1
            else:
                next_ += 1
            
            if jungle[next_][posCopy[1]] == "#":
                break
            else:
                posCopy[0] = next_
    
    pos = posCopy
                
    

pos = [0, ls[0].index(".")]
direction = "R"
possible = ["R", "D", "L", "U"]
for i in directions:
    if isinstance(i, int):
        move(i)
    else:
        if i == "R":
            direction = possible[(possible.index(direction)+1)%4]
        else:
            direction = possible[(possible.index(direction)-1)%4]

print("Star 1:", (pos[0]+1)*1000 + (pos[1]+1)*4 + possible.index(direction))

def getDebugJungle(pos):
    global jungle
    global direction
    char = None
    if direction == "R":
        char = ">"
    if direction == "U":
        char = "^"
    if direction == "L":
        char = "<"
    if direction == "D":
        char = "V"
    debugJungle = []
    for i in jungle[:pos[0]]:
        debugJungle.append(i)
    debugJungle.append(jungle[pos[0]][:pos[1]] + char + jungle[pos[0]][pos[1]+1:])
    for i in jungle[pos[0]+1:]:
        debugJungle.append(i)
    
    with open("debug.txt", "w") as file:
        file.write("\n".join(debugJungle))
    

def wrapRight(next_):
    global maybeDirection
    if next_[0] < 50:
        maybeDirection = "L"
        return [149-next_[0], 99]
    
    if next_[0] < 100:
        maybeDirection = "U"
        return [49, next_[0]+50]
    
    if next_[0] < 150:
        maybeDirection = "L"
        return [149-next_[0], 149]
    
    maybeDirection = "U"
    return [149, next_[0]-100]

def wrapLeft(next_):
    global maybeDirection
    if next_[0] < 50:
        maybeDirection = "R"
        return [149-next_[0], 0]
    
    if next_[0] < 100:
        maybeDirection = "D"
        return [100, next_[0]-50]
    
    if next_[0] < 150:
        maybeDirection = "R"
        return [149-next_[0], 50]
    
    maybeDirection = "D"
    return [0, next_[0]-100]

def wrapUp(next_):
    global maybeDirection
    if next_[1] < 50:
        maybeDirection = "R"
        return [next_[1]+50, 50]
    
    if next_[1] < 100:
        maybeDirection = "R"
        return [next_[1]+100, 0]
    
    maybeDirection = "U"
    return [199, next_[1]-100]

def wrapDown(next_):
    global maybeDirection
    if next_[1] < 50:
        maybeDirection = "D"
        return [0, next_[1]+100]
    
    if next_[1] < 100:
        maybeDirection = "L"
        return [next_[1]+100, 49]
    
    maybeDirection = "L"
    return [next_[1]-50, 99]

a = None
def moveCube(num):
    global a
    global jungle
    global direction
    global pos
    global maybeDirection
    posCopy = pos.copy()
    for i in range(num):
        getDebugJungle(posCopy)
        if direction == "R":
            next_ = posCopy.copy()
            if next_[1]+1 >= len(jungle[next_[0]]) or jungle[next_[0]][next_[1]+1] == " ":
                next_ = wrapRight(next_)
            else:
                next_[1] += 1
                maybeDirection = None
                
            if jungle[next_[0]][next_[1]] == "#":
                break
            else:
                posCopy = next_
                if maybeDirection != None:
                    direction = maybeDirection
        
        elif direction == "L":
            next_ = posCopy.copy()
            if next_[1]-1 < 0 or jungle[next_[0]][next_[1]-1] == " ":
                next_ = wrapLeft(next_)
                print(next_)
            else:
                next_[1] -= 1
                maybeDirection = None
            
            if jungle[next_[0]][next_[1]] == "#":
                break
            else:
                posCopy = next_
                if maybeDirection != None:
                    direction = maybeDirection
        
        elif direction == "U":
            next_ = posCopy.copy()
            if next_[0]-1 < 0 or jungle[next_[0]-1][next_[1]] == " ":
                next_ = wrapUp(next_)
            else:
                next_[0] -= 1
                maybeDirection = None
            
            if jungle[next_[0]][next_[1]] == "#":
                break
            else:
                posCopy = next_
                if maybeDirection != None:
                    direction = maybeDirection
        
        elif direction == "D":
            next_ = posCopy.copy()
            if next_[0]+1 >= len(jungle) or jungle[next_[0]+1][next_[1]] == " ":
                next_ = wrapDown(next_)
            else:
                next_[0] += 1
                maybeDirection = None
            
            if jungle[next_[0]][next_[1]] == "#":
                break
            else:
                posCopy = next_
                if maybeDirection != None:
                    direction = maybeDirection
                
    pos = posCopy

pos = [0, ls[0].index(".")]
direction = "R"
maybeDirection = None
possible = ["R", "D", "L", "U"]
for i in directions:
    if isinstance(i, int):
        temp = direction
        temp2 = pos
        moveCube(i)
        if direction != temp:
            print(temp, temp2)
            print(direction, pos)
            print(" ")
    else:
        if i == "R":
            direction = possible[(possible.index(direction)+1)%4]
        else:
            direction = possible[(possible.index(direction)-1)%4]


print("star 2:", (pos[0]+1)*1000 + (pos[1]+1)*4 + possible.index(direction))