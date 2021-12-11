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
flashed =[]

def spiral(y0, x0):
    global flashes
    global flashed
    spots = [(1, 1),(1, 0),(1,-1),
             (0,1),(0,0),(0,-1),
             (-1, 1),(-1, 0),(-1,-1)]


    for y1, x1 in spots:
        #print(y1,x1)
        y=y0
        x=x0
        y+=y1
        x+=x1
        #print(y,x)
        if (data[y][x] != -1 and 
            not (y,x) in flashed):
            data[y][x]+=1
            if(data[y][x] >= 10):
                data[y][x] = 0
                flashes+=1
                flashed.append(((y), (x)))
                spiral(y,x)


for step in range(1, 101):
    print('step', step)
    flashed = []
    for y in range(1,len(data)-1):
        for x in range(1, len(data[y])-1):
            data[y][x]+=1
            if data[y][x]==10:
                #print('flash', y, x)
                #flashes+=1
                #flashed.append((y, x))
                spiral(y, x)
                #data[y][x]=0
                #print()

    pprint(data)
print(flashes)