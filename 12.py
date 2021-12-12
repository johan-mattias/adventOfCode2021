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

pathes = [[]]

def find_next_cave(cave):
    for c1 in range(len(caves[cave])):
        for path in pathes:
            # return a path not in the list
            if not cave in path and not caves[cave][c1] in path:
                return c1


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