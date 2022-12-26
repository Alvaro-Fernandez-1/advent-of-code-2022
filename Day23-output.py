ls = None
with open("Day23-input.txt") as f:
    ls = list(map(lambda l:l.strip("\n"), f.readlines()))

def checkMove(elf, move):
    global elves
    global potentialMoves
    if not (elf[0]-1, elf[1]-1) in elves and \
       not (elf[0]-1, elf[1]) in elves and \
       not (elf[0]-1, elf[1]+1) in elves and \
       not (elf[0], elf[1]+1) in elves and \
       not (elf[0]+1, elf[1]+1) in elves and \
       not (elf[0]+1, elf[1]) in elves and \
       not (elf[0]+1, elf[1]-1) in elves and \
       not (elf[0], elf[1]-1) in elves:
           return True
    
    if move == "U":
        if not (elf[0]-1, elf[1]-1) in elves and \
           not (elf[0]-1, elf[1]) in elves and \
           not (elf[0]-1, elf[1]+1) in elves:
            if (elf[0]-1, elf[1]) in potentialMoves:
                potentialMoves[elf[0]-1, elf[1]] = None
            else:
                potentialMoves[elf[0]-1, elf[1]] = elf
            return True
    
    if move == "D":
        if not (elf[0]+1, elf[1]-1) in elves and \
           not (elf[0]+1, elf[1]) in elves and \
           not (elf[0]+1, elf[1]+1) in elves:
            if (elf[0]+1, elf[1]) in potentialMoves:
                potentialMoves[elf[0]+1, elf[1]] = None
            else:
                potentialMoves[elf[0]+1, elf[1]] = elf
            return True
    
    if move == "R":
        if not (elf[0]-1, elf[1]+1) in elves and \
           not (elf[0],   elf[1]+1) in elves and \
           not (elf[0]+1, elf[1]+1) in elves:
            if (elf[0], elf[1]+1) in potentialMoves:
                potentialMoves[elf[0], elf[1]+1] = None
            else:
                potentialMoves[elf[0], elf[1]+1] = elf
            return True
    
    if move == "L":
        if not (elf[0]-1, elf[1]-1) in elves and \
           not (elf[0],   elf[1]-1) in elves and \
           not (elf[0]+1, elf[1]-1) in elves:
            if (elf[0], elf[1]-1) in potentialMoves:
                potentialMoves[elf[0], elf[1]-1] = None
            else:
                potentialMoves[elf[0], elf[1]-1] = elf
            return True
    
    
    return False

def getMove(elf, moves):
    for move in moves:
        if checkMove(elf, move):
            break

elves = set()
potentialMoves = {}

for i in range(len(ls)):
    for j in range(len(ls[i])):
        if ls[i][j] == "#":
            elves.add((i,j))

moves = ["U", "D", "L", "R"]
for i in range(10):
    for elf in elves:
        getMove(elf, moves)
    
    for i in potentialMoves:
        if potentialMoves[i] != None:
            elves.remove(potentialMoves[i])
            elves.add(i)
    
    potentialMoves = {}
    
    moves.append(moves[0])
    del moves[0]

minX = 99**99
maxX = -99**99
minY = 99**99
maxY = -99**99
for elf in elves:
    if elf[0] < minY:
        minY = elf[0]
    if elf[1] < minX:
        minX = elf[1]
    if elf[0] > maxY:
        maxY = elf[0]
    if elf[1] > maxX:
        maxX = elf[1]

empty = (maxY - minY + 1) * (maxX - minX + 1) - len(elves)
print("Star 1:", empty)


elves = set()
potentialMoves = {}

for i in range(len(ls)):
    for j in range(len(ls[i])):
        if ls[i][j] == "#":
            elves.add((i,j))

moves = ["U", "D", "L", "R"]
prevPotentialMoves = 1
counter = 0
while prevPotentialMoves > 0:
    for elf in elves:
        getMove(elf, moves)
    
    for i in potentialMoves:
        if potentialMoves[i] != None:
            elves.remove(potentialMoves[i])
            elves.add(i)
    
    prevPotentialMoves = len(potentialMoves)
    counter += 1
    potentialMoves = {}
    
    moves.append(moves[0])
    del moves[0]

print("star 2:", counter)