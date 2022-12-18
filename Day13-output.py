ls = None
with open("Day13-input.txt") as f:
    ls = list(map(lambda l:l.strip("\n"), f.readlines()))

class Node():
    def __init__(self, data=[], parent=None):
        self.data = data
        self.children = []
        self.parent = parent

    def add(self, obj):
        self.children.append(obj)
    

def parse(l):
    root = Node(data=[])
    pos = 1
    curNode = root
    while pos < len(l)-1:
        if l[pos] == "[":
            curNode.children.append(Node(parent=curNode, data=[]))
            curNode = curNode.children[-1]
            pos += 1
        elif l[pos] == ",":
            pos += 1
            continue
        elif l[pos] == "]":
            curNode.parent.data.append(curNode.data)
            curNode = curNode.parent
            pos += 1
        elif l[pos] in "0123456789":
            newPos = pos
            while l[newPos] in "0123456789":
                newPos+=1
            curNode.data.append(int(l[pos:newPos]))
            pos = newPos
    return root


def compare(a,b):
    if isinstance(a, int) and isinstance(b, int):
        if a==b:
            return -1
        if a<b:
            return 1
        return 0
    if isinstance(a, list) and isinstance(b, list):
        i = 0
        while True:
            if i==len(a)==len(b):
                return -1
            if i==len(a):
                return 1
            if i==len(b):
                return 0
            result = compare(a[i],b[i])
            if result != -1:
                return result
            i+=1
        
    if isinstance(a, int) and isinstance(b, list):
        return compare([a],b)
    if isinstance(a, list) and isinstance(b, int):
        return compare(a,[b])
    
    
    
packets = [[[2]], [[6]]]
v=0
i=0
index = 1
while i < len(ls):
    l = ls[i]
    a = parse(l)
    i+=1
    l = ls[i]
    b = parse(l)
    i+=2
    
    packets.append(a.data)
    packets.append(b.data)
    
    if compare(a.data, b.data) == 1:
        v += index
    index += 1
    

print("Star 1:", v)

i=0
switched = True
while True:
    if i == 0 and not switched:
        break
    if i == 0:   
        switched = False
    
    if compare(packets[i], packets[i+1]) == 0:
        temp = packets[i]
        packets[i] = packets[i+1]
        packets[i+1] = temp
        switched = True
    
    
    i = (i+1) % (len(packets)-1)

print("star 2:", (packets.index([[2]])+1) * (packets.index([[6]])+1))













