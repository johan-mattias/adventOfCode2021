from sys import stdin
from pprint import pprint

data = []
for line in stdin:
    data.append([-1]+[int(char) for char in line.rstrip()]+[-1])

padding = [-1 for _ in data[0]]
data.insert(0, padding)
data.append(padding)

pprint(data)

flashes = 0

def spiral(y, x):
    if data[y+1][x+1] != -1:
        data[y+1][x+1]+=1
        if(data[y+1][x+1] >= 10):
            data[y+1][x+1] = 0
            spiral(y+1,x+1)
    if data[y+1][x] != -1:
        data[y+1][x]+=1
        if(data[y+1][x] >= 10):
            data[y+1][x] = 0
            spiral(y+1,x)
    if data[y+1][x-1] != -1:
        data[y+1][x-1]+=1
        if(data[y+1][x-1] >= 10):
            data[y+1][x-1] = 0
            spiral(y+1,x-1)
    if data[y][x+1] != -1:
        data[y][x+1]+=1
        if(data[y][x+1] >= 10):
            data[y][x+1] = 0
            spiral(y,x+1)
    if data[y][x-1] != -1:
        data[y][x-1]+=1
        if(data[y][x-1] >= 10):
            data[y][x-1] = 0
            spiral(y,x-1)
    if data[y-1][x+1] != -1:
        data[y-1][x+1]+=1
        if(data[y-1][x+1] >= 10):
            data[y-1][x+1] = 0
            spiral(y-1,x+1)
    if data[y-1][x] != -1:
        data[y-1][x]+=1
        if(data[y-1][x] >= 10):
            data[y-1][x] = 0
            spiral(y-1,x)
    if data[y-1][x-1] != -1:
        data[y-1][x-1]+=1
        if(data[y-1][x-1] >= 10):
            data[y-1][x-1] = 0
            spiral(y-1,x-1)

for step in range(1, 3):
    print('step', step)

    for y in range(1,len(data)-1):
        for x in range(1, len(data[y])-1):
            data[y][x]+=1


    for y in range(1,len(data)-1):
        for x in range(1, len(data[y])-1):
            if data[y][x]==10:
                flashes+=1
                spiral(y, x)
                data[y][x]=0

    pprint(data)
print(flashes)