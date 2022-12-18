ls = None
with open("Day17-input.txt") as f:
    ls = list(map(lambda l:l.strip("\n"), f.readlines()))


def isStopped(piece, pos, board):
    for i in range(len(piece)):
        row = piece[i]
        for j in range(len(row)):
            block = row[j]
            if pos[1]-i == 0 or (block == "#" and board[pos[1] - i - 1][pos[0] + j] == "#"):
                return True
    return False

def move(mv, piece, pos, board):
    if pos[0] == 0 and mv == "<":
        return
    if pos[0] + len(piece[0]) == 7 and mv == ">":
        return
    
    if mv == "<":
        for i in range(len(piece)):
            row = piece[i]
            for j in range(len(row)):
                block = row[j]
                if pos[0]==0 or (block == "#" and board[pos[1] - i][pos[0] + j - 1] == "#"):
                    return
        
        pos[0] -= 1
        return
    
    if mv == ">":
        for i in range(len(piece)):
            row = piece[i]
            for j in range(len(row)):
                block = row[j]
                if pos[0]+j == 6 or (block == "#" and board[pos[1] - i][pos[0] + j + 1] == "#"):
                    return
        
        pos[0] += 1
        return




l = ls[0]
rocks = [["####"],
[".#.",
"###",
".#."],
["..#",
"..#",
"###"],
["#",
"#",
"#",
"#"],
["##",
"##"]]

board = []
for i in range(50000):
    board.append([".", ".", ".", ".", ".", ".", "."])
highestPoint = -1
rInd = -1
moveNum = 0

for i in range(2022):
    rInd = (rInd+1) % len(rocks)
    rock = rocks[rInd]
    pos = [2, highestPoint + 3 + len(rock)]
    
    move(l[moveNum], rock, pos, board)
    moveNum = (moveNum+1) % len(l)
    while (not isStopped(rock, pos, board)):
        pos[1] -= 1
        move(l[moveNum], rock, pos, board)
        moveNum = (moveNum+1) % len(l)
    
    for i in range(len(rock)):
        row = rock[i]
        for j in range(len(row)):
            block = row[j]
            if block == ".":
                continue
            board[pos[1] - i][pos[0] + j] = block
        
    highestPoint = max(highestPoint, pos[1])

print("Star 1:", highestPoint+1)

board = []
for i in range(500000):
    board.append([".", ".", ".", ".", ".", ".", "."])
highestPoint = -1
rInd = -1
moveNum = 0
repeated = set()
onlyOne = None
rep1 = None
rep2 = None
lastRows = None

for i in range(100000):
    if rInd == 0: #important for part 2
        if onlyOne == moveNum:
            t = tuple(map(lambda x:"".join(x), board[highestPoint-15: highestPoint+5]))
            if t in repeated:
                rep2 = (i, highestPoint+1)
                break
            repeated.add(t)
        
        if moveNum in repeated and onlyOne == None:
            rep1 = (i, highestPoint+1)
            onlyOne = moveNum
            lastRows = board[highestPoint-15: highestPoint+5]
            
        repeated.add(moveNum)
        


    rInd = (rInd+1) % len(rocks)
    rock = rocks[rInd]
    pos = [2, highestPoint + 3 + len(rock)]
    
    move(l[moveNum], rock, pos, board)
    moveNum = (moveNum+1) % len(l)
    while (not isStopped(rock, pos, board)):
        pos[1] -= 1
        move(l[moveNum], rock, pos, board)
        moveNum = (moveNum+1) % len(l)
    
    for i in range(len(rock)):
        row = rock[i]
        for j in range(len(row)):
            block = row[j]
            if block == ".":
                continue
            board[pos[1] - i][pos[0] + j] = block
        
    highestPoint = max(highestPoint, pos[1])

endPeriodPos = (1000000000000 - rep1[0]) % (rep2[0] - rep1[0])
afterAllPeriods = rep1[1] + (rep2[1] - rep1[1]) * (1000000000000-rep1[0]-endPeriodPos) // (rep2[0] - rep1[0])

#simulate again
board = [['.', '#', '#', '#', '#', '.', '.']]
for i in range(10000):
    board.append([".", ".", ".", ".", ".", ".", "."])
highestPoint = 0
rInd = 0
moveNum = onlyOne
for i in range(endPeriodPos):
    rInd = (rInd+1) % len(rocks)
    rock = rocks[rInd]
    pos = [2, highestPoint + 3 + len(rock)]
    
    move(l[moveNum], rock, pos, board)
    moveNum = (moveNum+1) % len(l)
    while (not isStopped(rock, pos, board)):
        pos[1] -= 1
        move(l[moveNum], rock, pos, board)
        moveNum = (moveNum+1) % len(l)
    
    for i in range(len(rock)):
        row = rock[i]
        for j in range(len(row)):
            block = row[j]
            if block == ".":
                continue
            board[pos[1] - i][pos[0] + j] = block
        
    highestPoint = max(highestPoint, pos[1])

print("star 2:", afterAllPeriods + highestPoint)