ls = None
with open("Day9-input.txt") as f:
    ls = list(map(lambda l:l.strip("\n"), f.readlines()))

def I(list_):
    for i in range(len(list_)):
        list_[i] = int(list_[i])
    return list_


hPos = (0,0)
tPos = (0,0)

def mvHead(d):
    global hPos
    if d=="R":
        hPos = (hPos[0]+1, hPos[1])
    elif d=="U":
        hPos = (hPos[0], hPos[1]+1)
    elif d=="L":
        hPos = (hPos[0]-1, hPos[1])
    elif d=="D":
        hPos = (hPos[0], hPos[1]-1)

def mvTail(hPos, tPos):
    if hPos[0] == tPos[0] and abs(tPos[1] - hPos[1]) == 2:
        tPos = (tPos[0], tPos[1] + (hPos[1] - tPos[1])/2)
    elif hPos[1] == tPos[1] and abs(tPos[0] - hPos[0]) == 2:
        tPos = (tPos[0] + (hPos[0] - tPos[0])/2, tPos[1])
    elif abs(tPos[1] - hPos[1]) == 2 or abs(tPos[0] - hPos[0]) == 2:
        tPos = (tPos[0] + abs(tPos[0] - hPos[0])/(hPos[0] - tPos[0]), tPos[1] + abs(tPos[1] - hPos[1])/(hPos[1] - tPos[1]))
    tPos = (int(tPos[0]), int(tPos[1]))
    return tPos


vis = {(0,0)}
for i in range(len(ls)):
    d,n = ls[i].split()
    n = int(n)
    for i in range(n):
        mvHead(d)
        tPos = mvTail(hPos, tPos)
        vis.add(tPos)
        
print("Star 1:", len(vis))


hPos = (0,0)
tPos = [(0,0)]*9
vis = {(0,0)}
for i in range(len(ls)):
    d,n = ls[i].split()
    n = int(n)
    for j in range(n):
        mvHead(d)
        tPos[0] = mvTail(hPos, tPos[0])
        for k in range(1, len(tPos)):    
            tPos[k] = mvTail(tPos[k-1], tPos[k])
        vis.add(tPos[8])
        
        

print("star 2:", len(vis))













