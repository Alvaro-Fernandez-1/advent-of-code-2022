import queue

ls = None
with open("Day18-input.txt") as f:
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

cubes = []
for i in range(25):
    y = []
    for j in range(25):
        z = [False]*25
        y.append(z)
    cubes.append(y)

counter = 0    
for i in range(len(ls)):
    l = I(ls[i].split(","))
    cubes[l[0]][l[1]][l[2]] = True
    counter += 1

sides = counter*6
for i in range(25):
    for j in range(25):
        for k in range(25):
            if cubes[i][j][k] and cubes[i+1][j][k]:
                sides -= 2
            if cubes[i][j][k] and cubes[i][j+1][k]:
                sides -= 2
            if cubes[i][j][k] and cubes[i][j][k+1]:
                sides -= 2


print("Star 1:", sides)

q = queue.Queue()
q.put((24,24,24))
q.put((0,0,0))
while not q.empty():
    item = q.get()
    if cubes[item[0]][item[1]][item[2]] == True:
        continue
    if cubes[item[0]][item[1]][item[2]] == -1:
        continue
    cubes[item[0]][item[1]][item[2]] = -1
    
    if item[0] < 24 and cubes[item[0]+1][item[1]][item[2]] != -1:
        q.put((item[0]+1, item[1], item[2]))
        
    if item[1] < 24 and cubes[item[0]][item[1]+1][item[2]] != -1:
        q.put((item[0], item[1]+1, item[2]))
        
    if item[2] < 24 and cubes[item[0]][item[1]][item[2]+1] != -1:
        q.put((item[0], item[1], item[2]+1))
        
    if item[0] > 0 and cubes[item[0]-1][item[1]][item[2]] != -1:
        q.put((item[0]-1, item[1], item[2]))
        
    if item[1] > 0 and cubes[item[0]][item[1]-1][item[2]] != -1:
        q.put((item[0], item[1]-1, item[2]))
        
    if item[2] > 0 and cubes[item[0]][item[1]][item[2]-1] != -1:
        q.put((item[0], item[1], item[2]-1))

for i in range(25):
    for j in range(25):
        for k in range(25):
            if cubes[i][j][k]==False and cubes[i+1][j][k]==True:
                sides -= 1
            if cubes[i][j][k]==False and cubes[i][j+1][k]==True:
                sides -= 1
            if cubes[i][j][k]==False and cubes[i][j][k+1]==True:
                sides -= 1
            if cubes[i][j][k]==False and cubes[i-1][j][k]==True:
                sides -= 1
            if cubes[i][j][k]==False and cubes[i][j-1][k]==True:
                sides -= 1
            if cubes[i][j][k]==False and cubes[i][j][k-1]==True:
                sides -= 1
            

print("star 2:", sides)