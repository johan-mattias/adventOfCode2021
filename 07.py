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
        flag = False
        if k<pos:
            flag = True
            #print('***switch***')
            pos, k = k,pos
        f1= k-pos+1
        f2= list(range(f1))
        f3= sum(f2)
        temp_fuel = f3*v
        #print(f1, f2, f3, temp_fuel)
        #print(sum(list(range(pos, k-1))*v))
        #fuel+= sum(list(range(pos, k-1))*v)
        #print(temp_fuel)
        fuel += temp_fuel
        #print('fuel', fuel)
        if flag:
            #print('***switch back***')

            pos, k = k,pos
    #print(pos,fuel)
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
'''
16->15 1
15->14 2
14- 13 3
13-12 4
12-11 5
11-10 6
10-9 7
9-8 8
8-7 9
7-6 10
6-5 11
'''