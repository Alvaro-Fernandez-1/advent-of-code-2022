lines = None
with open("Day7-input.txt") as f:
    lines = list(map(lambda l:l.strip("\n"), f.readlines()))

class Node(object):
    def __init__(self, data=None, name=None, parent=None, type_=None):
        self.data = data
        self.name = name
        self.children = {}
        self.parent = parent
        self.type = type_

    def addChild(self, obj):
        self.children[obj.name] = obj
    
    def hasChildren(self):
        return self.children != {}
        
    def size(self):
        if self.type == "file":
            return self.data
        v=0
        for c in self.children:
            v+=self.children[c].size()
        return v
    
    def hasName(self, name):
        for i in self.children:
            return self.children[i].data == name
    
    def searchBigDirs(self):
        v=0
        if self.type == "file":
            return 0
        if self.size() <= 100000:
            v+=self.size()
        for c in self.children:
            v+=self.children[c].searchBigDirs()
        return v
    
    def getBiggestDirs(self):
        if self.type == "file":
            return [0]
        sizes = [self.children[x].size() for x in self.children if self.children[x].type == "dir"]
        for i in self.children:
            sizes += self.children[i].getBiggestDirs()
        sizes.sort()
        return sizes


def executeCd(dirName):
    global current
    
    if dirName != "..":
        if not current.hasName(dirName):
            current.addChild(Node(name=dirName, parent=current, type_="dir"))
        current = current.children[dirName]
    else:
        current = current.parent


root=Node()
current=root
for i in range(1,len(lines)):
    line = lines[i].split()
    
    if line[0]=="$" and line[1] == "cd":
        executeCd(line[2])
    elif line[0] == "dir" and current.hasChildren and not line[1] in current.children:
        current.addChild(Node(name=line[1], parent=current, type_="dir"))
    elif line[0][0] in "0123456789":
        current.addChild(Node(data=int(line[0]), name=line[1], type_="file"))
    
print("Star 1:", root.searchBigDirs())


dirs = root.getBiggestDirs()
size = root.size()
for i in dirs:
    if size-i <= 40000000:
        print("star 2:", i)
        break