ls = None
with open("Day7-input.txt") as f:
    ls = list(map(lambda l:l.strip("\n"), f.readlines()))

class Nd(object):
    def __init__(self, data=None, name=None, parent=None):
        self.data = data
        self.name = name
        self.children = {}
        self.parent = parent

    def add(self, obj, name):
        self.children[name] = obj
        
    def size(self):
        v=0
        for c in self.children:
            v+=self.children[c].size()
        if self.data!=None:
            v+=self.data
        return v
    
    def hasName(self, name):
        for i in self.children:
            if self.children[i].data == name:
                return True
    
    def s(self):
        v=0
        if self.data != None:
            return 0
        if self.size()<=100000:
            v+=self.size()
        for c in self.children:
            v+=self.children[c].s()
        return v
    
    
    def s2(self):
        if self.data != None:
            return [0]
        l=[self.children[x].size() for x in self.children if self.children[x].data == None]
        for i in self.children:
            l+=self.children[i].s2()
        l.sort()
        return l
    
v = 0
rt=Nd()
pos=rt
for i in range(1,len(ls)):
    l = ls[i].split()
    if l[0]=="$":
        l=l[1:]
        if l[0]=="cd" and l[1] != "..":
            l=l[1:]
            if not pos.hasName(l[0]):
                pos.add(Nd(name=l[0], parent=pos), l[0])
            pos=pos.children[l[0]]
        elif l[0]=="cd" and l[1] == "..":
            pos = pos.parent
            
    else:
        if l[0]=="dir":
            if pos.children != {} and l[1] in pos.children:
                pos.children[l[1]] = Nd(name=l[1])
        else:
            pos.add(Nd(data=int(l[0]), name=l[1]), l[1])
    

print("Star 1:", rt.s())

a=rt.s2()
sz=rt.size()
for i in a:
    if sz-i<=40000000:
        print("star 2:", i)
        break