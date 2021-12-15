from sys import stdin
from pprint import pprint
import sys 
from collections import defaultdict

filename = '12_in.txt'

caves = defaultdict(list)

with open(filename) as file:
    for line in file:
        k, v = line.rstrip().split('-')
        caves[k].append(v)

pathes = []

def find_next_cave(cave):
    end = True
    for path in pathes:
        for c1 in range(len(caves[cave])):
            # return a path not in the list
            cave_temp = caves[cave][c1]
            if not cave in path or not caves[cave][c1] in path:
                temp = c1
            else:
                end = False

    else:
        return 0
    if(end):
        return temp
flag = True
while(flag):
    path = []
    cave = 'start'
    while(caves[cave] != 'end'):
        path.append(cave)
        if caves[cave] != []:
            next_cave = find_next_cave(cave)
            cave = caves[cave][next_cave]
        else:
            #if path[len(path) == 'end']:
            #TODO filter out deadends after
            pathes.append(path)
            break

pprint(pathes)
        

pprint(caves)