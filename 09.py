from sys import stdin
from pprint import pprint
from functools import reduce
data = []

for line in stdin:
    line = '9'+line.rstrip()+'9'
    data.append([int(char) for char in line])
data.insert(0, [9 for _ in data[0]])
data.append([9 for _ in data[0]])    
#pprint(data)

low_points = []

for row in range(len(data)):
    for col in range(len(data[row])):
        if (data[row][col] < data[row][col-1] and
            data[row][col] < data[row-1][col] and
            data[row][col] < data[row][col+1] and
            data[row][col] < data[row+1][col]):
            low_points.append((row,col))
print(low_points)

def spiral(row, col):
    temp = []
    if 9 != data[row][col-1]:
        temp.append((row, col-1))
    if 9 != data[row-1][col]:
        temp.append((row-1, col))
    if 9 != data[row][col+1]:
        temp.append((row, col+1))
    if 9 != data[row+1][col]:
        temp.append((row+1, col))

    return temp

def death_spiral(row, col):
    temp = []
    flag = True
    seen = set()
    new = set(spiral(row, col))
    seen.add((row, col))
    #print('start', row, col)
    #print('new', new)
    while(len(new) >= 1):
        x, y = new.pop()
        #print('pop', x, y)
        t1 = spiral(x, y)
        #print('temp', t1)
        seen.add((x, y))
        for pt in t1:
            if not pt in seen:
                new.add(pt)
        #print('seen', seen)
    return len(seen)

size = []
for row, col in low_points:
    temp = death_spiral(row, col)
    print(row, col, temp)
    size.append(temp)


print(reduce((lambda x, y: x * y), sorted(size)[::-1][0:3]))
