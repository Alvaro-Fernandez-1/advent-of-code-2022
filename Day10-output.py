ls = None
with open("Day10-input.txt") as f:
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


v = 0
x = 1
j=0
for i in range(len(ls)):
    l = ls[i].split()
    if l[0]=="noop":
        j+=1
        
        if j+1 in [20,60,100,140,180,220]:
            v += x * (j+1)
        continue
    j+=1
    
    if j+1 in [20,60,100,140,180,220]:
        v += x * (j+1)
    j+=1
    x += int(l[1])
    
    if j+1 in [20,60,100,140,180,220]:
        v += x * (j+1)
    

print("Star 1:", v)

def draw(i, sprite):
    if abs(sprite-i%40) <= 1:
        return "#"
    return "."
    


x = 1
j=0
display = ""
for i in range(len(ls)):
    l = ls[i].split()
    if l[0]=="noop":
        display += draw(j,x)
        j+=1
        continue
    
    display += draw(j,x)
    j+=1
    
    display += draw(j,x)
    j+=1
    x += int(l[1])
    


print("star 2:")
print(display[:40])
print(display[40:80])
print(display[80:120])
print(display[120:160])
print(display[160:200])
print(display[200:240])










