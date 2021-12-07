from sys import stdin
from collections import defaultdict
from pprint import pprint
crabs = [int(num) for num in stdin.readline().rstrip().split(',')]

print(sum(crabs))
print(crabs)
crab_dict = defaultdict(int)
for crab in crabs:
    crab_dict[crab]+=1

def calc(pos):
    fuel = 0
    for k, v in crab_dict.items():
        #print(k, v, pos)
        #print(abs(k-pos)*v)
        fuel+= abs(k-pos)*v
        #print('fuel', fuel)
    print(pos,fuel)
    return fuel

lowest_fuel = calc(0)
lowest_pos = 0
for pos in range(max(crabs)+1):
    fuel = calc(pos)
    if fuel < lowest_fuel:
        lowest_fuel = fuel
        lowest_pos = pos

print('lowest', lowest_pos, lowest_fuel)

#pprint(sorted(crab_dict.items()))