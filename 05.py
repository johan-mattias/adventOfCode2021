from sys import stdin
from pprint import pprint
from collections import defaultdict
cord = []
points = []
grid = []
#for _ in range(10):
#    grid.append([0 for _ in range(10)])
for line in stdin:
    pt1, pt2 = line.rstrip().split(' -> ')
    x1, y1 = list(map(int,pt1.split(',')))
    x2, y2 = list(map(int,pt2.split(',')))
    if x1==x2 or y1==y2:
        #print('equal', line)
        cord.append(((x1,y1), (x2,y2)))

        #put smaller point first
        if x1==x2:
            #print(x1, y1, x2, y2)
            if y2 < y1:
                y1, y2 = y2, y1
            for y in range(y1, y2+1):
                points.append((x1, y))
                #print(x1, y)
        elif y1==y2:
            #print(x1, y1, x2, y2)
            if x2 < x1:
                x1, x2 = x2, x1
            for x in range(x1, x2+1):
                points.append((x, y1))
                #print(x, y1)
    else:
        #print('yolo', line)
        #diagonal
        if ((x1 < x2 and y1 < y2) or
                x1 > x2 and y1 > y2):
            #increase x and y
            y_small = min(y1, y2)
            y_big = max(y1, y2)
            x_small = min(x1, x2)
            x_big = max(x1, x2)
            #print('lk at me')
            for x in range(x_small, x_big+1):
                print(x, y_small)
                points.append((x, y_small))
                y_small+=1
            pass
        else:
            if x2<x1:
                #switch
                x1, y1, x2, y2 = x2, y2, x1, y1 
            for x in range(x1, x2+1):
                points.append((x, y1))
                y1-=1
            #going diagonal
'''
for point in points:
    x, y = point
    grid[x][y] += 1

pprint(list(zip(*grid)))
'''
#print(cord)
#print(len(points))


danger_points = defaultdict(int)

#print(points)
#print(len(points))

for point in points:
    danger_points[point]+=1

#pprint(danger_points)
#print(len(danger_points))

foodict = {k: v for k, v in danger_points.items() if v>=2}
pprint(foodict)
print(len(foodict))




    
