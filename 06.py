from sys import stdin

from collections import defaultdict

fish = [int(num) for num in stdin.readline().rstrip().split(',')]
print(fish)

fishes = defaultdict(int)
#fishes[0] = 0
for f in fish:
    fishes[f] += 1

print(fishes)

for _ in range(256):
    print('day', _+1)
    flag = False
    for k, v, in sorted(fishes.items()):
        print(k, v)
        if(k==0):
            flag = True
            print('zero')
            temp6 = fishes[k]
            temp8 = fishes[k]
            fishes.pop(k)
        else:
            print('not zero', k)
            fishes[k-1] = fishes[k]
            fishes.pop(k)
    if flag == True:
        fishes[6] += temp6
        fishes[8] += temp8   
    print(fishes)

sum = 0
for k, v, in fishes.items():
    sum += v
print(sum)

'''

#part 1
fish = [int(num) for num in stdin.readline().rstrip().split(',')]

for _ in range(256):
    for f in range(len(fish)):
        if fish[f] == 0:
            fish[f] = 6
            fish.append(8)
        else:
            fish[f] -= 1
    #print(fish)

    #print(fish)

print(len(fish))
'''