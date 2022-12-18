ls = None
with open("Day14-input.txt") as f:
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

pos = {}
lowestRock = 0
for i in range(len(ls)):
    l = ls[i]
    l = l.split(" -> ")
    l = list(map(lambda x:I(x.split(",")), l))
    
    prev = None
    for nextPos in l:
        if nextPos[1] > lowestRock:
            lowestRock = nextPos[1]
            
        if prev == None:
            pos[(nextPos[0], nextPos[1])] = "#"
            prev = nextPos
            continue
        
        if nextPos[0] > prev[0]:
            for j in range(prev[0], nextPos[0]+1):
                pos[(j, nextPos[1])] = "#"
                
        elif nextPos[0] < prev[0]:
            for j in range(prev[0], nextPos[0]-1, -1):
                pos[(j, nextPos[1])] = "#"
                
        elif nextPos[1] > prev[1]:
            for j in range(prev[1], nextPos[1]+1):
                pos[(nextPos[0], j)] = "#"
                
        elif nextPos[1] < prev[1]:
            for j in range(prev[1], nextPos[1]-1, -1):
                pos[(nextPos[0], j)] = "#"
        prev = nextPos
    
total = 0;  
end = False          
while True:
    sand = (500,0)
    while True:
        if not (sand[0], sand[1]+1) in pos:
            sand = (sand[0], sand[1]+1)
        elif not (sand[0]-1, sand[1]+1) in pos:
            sand = (sand[0]-1, sand[1]+1)
        elif not (sand[0]+1, sand[1]+1) in pos:
            sand = (sand[0]+1, sand[1]+1)
        else:
            pos[sand] = "o"
            break
        if sand[1] > lowestRock:
            end = True
            break
    
    if end:
        break
    
    total +=1

print("Star 1:", total)

#reset sand in dictionary
pos_ = {}
for i in pos:
    if pos[i] == "#":
        pos_[i] = pos[i]
pos = pos_

total = 0;  
end = False          
while True:
    sand = (500,0)
    while True:
        if not (sand[0], sand[1]+1) in pos and sand[1]+1 != lowestRock+2:
            sand = (sand[0], sand[1]+1)
        elif not (sand[0]-1, sand[1]+1) in pos and sand[1]+1 != lowestRock+2:
            sand = (sand[0]-1, sand[1]+1)
        elif not (sand[0]+1, sand[1]+1) in pos and sand[1]+1 != lowestRock+2:
            sand = (sand[0]+1, sand[1]+1)
        else:
            pos[sand] = "o"
            if ((500,0) in pos):
                end = True
                break
            break
    
    total +=1
    
    if end:
        break
    
    

print("star 2:", total)