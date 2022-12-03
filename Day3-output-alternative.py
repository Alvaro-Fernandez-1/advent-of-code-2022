lines = None
with open("Day3-input.txt") as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i][:-1]

letters = "abcdefghijklmnopqrstuvwxyz"
letters += letters.upper()

value = 0
for line in lines:
    half1 = line[:len(line)//2]
    half2 = line[len(line)//2:]
    for char in half1:
        if char in half2:
            value += letters.find(char)+1
            break

print("Star 1:", value)

value = 0
for i in range(len(lines)//3):
    line1 = lines[3*i]
    line2 = lines[3*i+1]
    line3 = lines[3*i+2]

    for char in line1:
        if char in line2 and char in line3:
            value += letters.find(char)+1
            break

print("star 2:", value)