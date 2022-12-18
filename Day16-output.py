import queue
ls = None
with open("Day16-inputtest.txt") as f:
    ls = list(map(lambda l:l.strip("\n"), f.readlines()))

class Node():
    def __init__(self, flow, valve, children=[]):
        self.flow = flow
        self.valve= valve
        self.children = children
        self.maxIfReleased = []
        self.maxIfNotReleased = []
        
        for i in range(30):
            self.maxIfReleased.append([-1, set()])
            self.maxIfNotReleased.append([-1, set()])


def findMax(root):
    q = queue.Queue()
    q.put(root)
    global nodes
    
    while not q.empty():
        current = q.get()
        for c in current.children:
            changed = False
            
            for i in range(1, 30):
                if current.maxIfNotReleased[i-1][0] > c.maxIfNotReleased[i][0]:
                    c.maxIfNotReleased[i][0] = current.maxIfNotReleased[i-1][0]
                    c.maxIfNotReleased[i][1] = current.maxIfNotReleased[i-1][1].copy()
                    changed = True
                if current.maxIfReleased[i-1][0] > c.maxIfNotReleased[i][0]:
                    c.maxIfNotReleased[i][0] = current.maxIfReleased[i-1][0]
                    c.maxIfNotReleased[i][1] = current.maxIfReleased[i-1][1].copy()
                    changed = True
                
                
                
            for i in range(2, 30):
                if not c.valve in current.maxIfNotReleased[i-2][1] and \
                   current.maxIfNotReleased[i-2][0] != -1 and \
                   current.maxIfNotReleased[i-2][0] + c.flow * (30-i) > c.maxIfReleased[i][0]:
                    c.maxIfReleased[i][0] = current.maxIfNotReleased[i-2][0]
                    c.maxIfReleased[i][1] = current.maxIfNotReleased[i-2][1].copy()
                    c.maxIfReleased[i][1].add(c.valve)
                    changed = True
                    c.maxIfReleased[i][0] += c.flow * (30-i)
                    
                if not c.valve in current.maxIfReleased[i-2][1] and \
                   current.maxIfReleased[i-2][0] != -1 and \
                   current.maxIfReleased[i-2][0] + c.flow * (30-i) > c.maxIfReleased[i][0]:
                    c.maxIfReleased[i][0] = current.maxIfReleased[i-2][0]
                    c.maxIfReleased[i][1] = current.maxIfReleased[i-2][1].copy()
                    c.maxIfReleased[i][1].add(c.valve)
                    changed = True
                    c.maxIfReleased[i][0] += c.flow * (30-i)
            
            if changed:
                q.put(c)
    
    best = 0
    for i in nodes:
        for j in nodes[i].maxIfReleased:
            if j[0] > best:
                best = j[0]
        for j in nodes[i].maxIfNotReleased:
            if j[0] > best:
                best = j[0]
    return best
                
                
nodes = {}
for i in range(len(ls)):
    l = ls[i].split()
    thisValve = l[1]
    flow = int(l[4][5:-1])
    children = list(map(lambda x:x.strip(","), l[9:]))
    
    newNode = Node(flow, thisValve, children)
    nodes[thisValve] = newNode

for n in nodes:
    node = nodes[n]
    node.children = [nodes[x] for x in node.children]

root = nodes["AA"]
root.maxIfNotReleased[0][0] = 0
root.maxIfReleased[0][0] = 0
value = findMax(root)

print("Star 1:", value)

def updateNotReleased(toChange, toCheck, i):
    if toCheck[i-1][0] > toChange[i][0]:
        toChange[i][0] = toCheck[i-1][0]
        toChange[i][1] = toCheck[i-1][1].copy()
        return True
    return False

def updateReleasedOne(toChange, toCheck, i, valve, flow):
    if valve in toCheck[i-1][1]:
        return False
    if toCheck[i-1][0] == -1:
        return False
    if toCheck[i-1][0] + flow * (26-i) > toChange[i][0]:
        toChange[i][0] = toCheck[i-1][0]
        toChange[i][1] = toCheck[i-1][1].copy()
        toChange[i][1].add(valve)
        toChange[i][0] += flow * (26-i)
        return True
    return False

def findMaxWithElephant(root):
    q = queue.Queue()
    q.put(root)
    global nodes
    
    counter = 1
    while not q.empty():
        if counter % 10000 == 0:
            print(counter)
        counter += 1
        current = q.get()
        for c in current.children:
            changed = False
            
            #not released
            for i in range(1, 26):
                change = c.maxIfNotReleased
                changed |= updateNotReleased(change, current.maxIfReleased2, i)
                changed |= updateNotReleased(change, current.maxIfReleased1, i)
                changed |= updateNotReleased(change, current.maxIfReleasedBoth, i)
                changed |= updateNotReleased(change, current.maxIfNotReleased, i)
                
            #released both
            for i in range(1, 26):
                change = c.maxIfReleasedBoth
                check = current.maxIfNotReleased
                if current.valve != c.valve:
                    break
                if c.valve[0] == c.valve[1]:
                    break
                if c.valve[0] in check[i-1][1]:
                    continue
                if c.valve[1] in check[i-1][1]:
                    continue
                if check[i-1][0] == -1:
                    continue
                if check[i-1][0] + (c.flow[0] + c.flow[1]) * (26-i) > change[i][0]:
                    change[i][0] = check[i-1][0]
                    change[i][1] = check[i-1][1].copy()
                    change[i][1].add(c.valve[0])
                    change[i][1].add(c.valve[1])
                    change[i][0] += (c.flow[0] + c.flow[1]) * (26-i)
                    changed = True
                    
            #released 1
            for i in range(1, 26):
                if current.valve[0] != c.valve[0]:
                    break
                changed |= updateReleasedOne(c.maxIfReleased1, current.maxIfReleased2, i, c.valve[0], c.flow[0])
                changed |= updateReleasedOne(c.maxIfReleased1, current.maxIfNotReleased, i, c.valve[0], c.flow[0])
                
            #released 2
            for i in range(1, 26):
                if current.valve[1] != c.valve[1]:
                    break
                changed |= updateReleasedOne(c.maxIfReleased2, current.maxIfReleased1, i, c.valve[1], c.flow[1])
                changed |= updateReleasedOne(c.maxIfReleased2, current.maxIfNotReleased, i, c.valve[1], c.flow[1])
                    
            
            if changed:
                q.put(c)
    
    best = 0
    for i in nodes:
        for j in nodes[i].maxIfReleased1:
            if j[0] > best:
                best = j[0]
        for j in nodes[i].maxIfReleased2:
            if j[0] > best:
                best = j[0]
        for j in nodes[i].maxIfReleasedBoth:
            if j[0] > best:
                best = j[0]
        for j in nodes[i].maxIfNotReleased:
            if j[0] > best:
                best = j[0]
    return best

class Node2():
    def __init__(self, flow, valve, children=[]):
        self.flow = flow
        self.valve= valve
        self.children = children
        self.maxIfReleased1 = []
        self.maxIfReleased2 = []
        self.maxIfReleasedBoth = []
        self.maxIfNotReleased = []
        
        for i in range(26):
            self.maxIfReleased1.append([-1, set()])
            self.maxIfReleased2.append([-1, set()])
            self.maxIfReleasedBoth.append([-1, set()])
            self.maxIfNotReleased.append([-1, set()])

newNodes = {}
for n1 in nodes:
    for n2 in nodes:
        node1 = nodes[n1]
        node2 = nodes[n2]
        children = []
        for i in node1.children + [node1]:
            for j in node2.children + [node2]:
                children.append((i.valve, j.valve))
        a = Node2((node1.flow, node2.flow), (n1, n2), children)
        newNodes[(n1, n2)] = a
        
nodes = newNodes
for n in nodes:
    node = nodes[n]
    node.children = [nodes[x] for x in node.children]

root = nodes[("AA", "AA")]
root.maxIfNotReleased[0][0] = 0
root.maxIfReleased1[0][0] = 0
root.maxIfReleased2[0][0] = 0
root.maxIfReleasedBoth[0][0] = 0
value = findMaxWithElephant(root)

print("star 2:", value)