from sys import stdin
from collections import defaultdict
from pprint import pprint

code = stdin.readline().rstrip().split()
code.pop()
print(code)

op = {0:6, 1:2, 2:5, 3:5, 4:4,
      5:5, 6:6, 7:3, 8:8, 9:6}

data = {0: ['a', 'b', 'c', 'e', 'f', 'g',],
        1: ['c', 'f',],
        2: ['a', 'c', 'd', 'e', 'g'],
        3: ['a', 'c', 'd', 'f', 'g'],
        4: ['b', 'c', 'd', 'f',],
        5: ['a', 'b', 'd', 'f', 'g'],
        6: ['a', 'b', 'd', 'e', 'f', 'g'],
        7: ['a', 'c', 'f',],
        8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        9: ['a', 'b', 'c', 'd', 'f', 'g'],}

alpha = defaultdict(list)

for value in code:
    for k, v in op.items():
        if len(value) == v:
            print(k, v, value)
            alpha[k].append([char for char in value])

translate = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
    }


for k, v, in alpha.items():
    if len(v) == 1:
        for k1, v1 in data.items():
            if len(v1) == len(v[0]):
                translate[k] = (*alpha[k],data[k])
pprint(alpha)
pprint(translate)

letters = defaultdict(list)
for q, v, in translate.items():
    if v != []:
        k, v = v
        for q1, v1, in translate.items():
            if v1 != []:
                k1, v1 = v1
                k_in = set(k).symmetric_difference(k1)
                v_in = set(v).symmetric_difference(v1)
                print(k_in, v_in)
                if len(k_in) == 1 and len(v_in) == 1:
                    letters[k_in.pop()] = v_in.pop()

print('set letters')
pprint(translate)
print('whole thing')
pprint(letters)

for k1, v1 in letters.items():
    print('letter keys', k1, v1)
    for k, v in translate.items():
        if v != []:
            print('letter values', k, v)
            k2, v2 = v
            print('lists', k2, v2)
            if k1 in k2:
                print('remove key')
                k2.remove(k1)
            if v1 in v2:
                print('remove value')
                v2.remove(v1)
            print('filtered,', k2, v2)
            translate[k] = (k2,v2)
print('filter our lteers')
pprint(translate)

'''
letters = defaultdict(lambda: defaultdict(int))
for k, v, in translate.items():
    print(k, v)
    if v != []:
        t1, t2 = v
        for k1 in t1:
            for v1 in t2:
                letters[k1][v1]+=1

    pprint(letters)
'''