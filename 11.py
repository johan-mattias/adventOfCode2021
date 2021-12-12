from sys import stdin
from pprint import pprint
import sys 

filename = '11_in.txt'

data = []

with open(filename) as file:
    for line in file:
        data.append([-1]+[int(char) for char in line.rstrip()]+[-1])

print(data)


padding = [-1 for _ in data[0]]
data.insert(0, padding)
data.append(padding)

pprint(data)

flashed = []
flashes = 0

def flash(y0, x0):
    global flashes
    global flashed
    spots = [(1, 1),(1, 0),(1,-1),
             (0,1),(0,-1),
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

    for y1, x1 in spots:
        #print(y1,x1)
        y=y0
        x=x0
        y+=y1
        x+=x1
        #print(y,x)
        if (data[y][x] != -1 and 
            not (y,x) in flashed):
            if(data[y][x] >= 10):

                data[y][x] = 0
                flashes+=1
                flashed.append(((y), (x)))
                flash(y,x)


for step in range(1, 300):
    print('step', step)
    flashed = []
    for y in range(1,len(data)-1):
        for x in range(1, len(data[y])-1):
            data[y][x]+=1
    for y in range(1,len(data)-1):
        for x in range(1, len(data[y])-1):
            if data[y][x]>=10:
                #print('flash', y, x)
                flashes+=1
                flashed.append((y, x))
                data[y][x]=0
                flash(y, x)
                #print()

    pprint(data)
    print(sum(map(sum, data)))
    if sum(map(sum, data)) == -44:
        print(step)
        exit()
#print(flashes)