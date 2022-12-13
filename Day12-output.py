ls = None
with open("Day12-input.txt") as f:
    ls = list(map(lambda l:l.strip("\n"), f.readlines()))

class Node(object):
    def __init__(self, height=None, distance=0):
        self.height = height
        self.distance = distance
        self.edges = []

    def add(self, obj):
        self.edges.append(obj)

import queue
def djikstra(root, dest, nodes):
    q = queue.Queue()
    q.put(root)
    root.distance = 0
    for node in nodes:
        if node != root:
            node.distance = 99**99
            
    while(not q.empty()):
        currNode = q.get()
        for adj in currNode.edges:
            newDist = currNode.distance + 1
            if newDist < adj.distance:
                adj.distance = newDist
                q.put(adj)
    
    return dest.distance

heights = "abcdefghijklmnopqrstuvwxyzSE"
start = None
end = None
for i in range(len(ls)):
    temp = []
    for j in range(len(ls[i])):
        temp.append(ls[i][j])
    ls[i] = temp
    ls[i] = list(map(lambda x:heights.index(x), ls[i]))
    for j in range(len(ls[i])):
        if ls[i][j] == 26:
            start = (j,i)
            ls[i][j] = 0
        if ls[i][j] == 27:
            end = (j,i)
            ls[i][j] = 25

nodes = []
for i in range(len(ls)):
    for j in range(len(ls[i])):
        thisNode = Node(ls[i][j])
        nodes.append(thisNode)
        ls[i][j] = thisNode
        if (j,i) == start:
            start = thisNode
        if (j,i) == end:
            end = thisNode
        
for i in range(len(ls)):
    for j in range(len(ls[i])):
        if i != 0 and ls[i-1][j].height - ls[i][j].height <= 1:
            ls[i][j].edges.append(ls[i-1][j])
        if j != 0 and ls[i][j-1].height - ls[i][j].height <= 1:
            ls[i][j].edges.append(ls[i][j-1])
        if i != len(ls)-1 and ls[i+1][j].height - ls[i][j].height <= 1:
            ls[i][j].edges.append(ls[i+1][j])
        if j != len(ls[i])-1 and ls[i][j+1].height - ls[i][j].height <= 1:
            ls[i][j].edges.append(ls[i][j+1])
        

distance = djikstra(start, end, nodes)

print("Star 1:", distance)

for i in range(len(ls)):
    for j in range(len(ls[i])):
        ls[i][j].edges = []

for i in range(len(ls)):
    for j in range(len(ls[i])):
        if i != 0 and ls[i][j].height - ls[i-1][j].height <= 1:
            ls[i][j].edges.append(ls[i-1][j])
        if j != 0 and ls[i][j].height - ls[i][j-1].height <= 1:
            ls[i][j].edges.append(ls[i][j-1])
        if i != len(ls)-1 and ls[i][j].height - ls[i+1][j].height <= 1:
            ls[i][j].edges.append(ls[i+1][j])
        if j != len(ls[i])-1 and ls[i][j].height - ls[i][j+1].height <= 1:
            ls[i][j].edges.append(ls[i][j+1])

distance = djikstra(end, start, nodes)
lowest = 99**99
for i in ls:
    for j in i:
        if j.height == 0 and j.distance < lowest:
            lowest = j.distance

print("star 2:", lowest)


