from sys import stdin
from math import floor, ceil
def calc(param, bits):

    print(bits)
    for index in range(len(bits[0])):
        print(index)
        total = 0
        for num in bits:
            print(num, total)
            if int(num[index]) == param:
                total+=1
        print('index', index, 'total', total)

        print('len', len(bits)//2, 'result', total > len(bits)//2)
        if param == 1:
            if total >= ceil(len(bits)/2):
                print('ones')
                bits = [num for num in bits if int(num[index]) == 1]
            else:
                print('zeros')
                bits = [num for num in bits if int(num[index]) == 0]
        else:
            if total > floor(len(bits)/2):
                print('ones')
                bits = [num for num in bits if int(num[index]) == 1]
            else:
                print('zeros')
                bits = [num for num in bits if int(num[index]) == 0]
        print('filter')

        print(bits)
        if len(bits) == 1:
            print(int(bits[0],2))
            return int(bits[0],2)

bits = []

for num in stdin:
    bits.append(num.rstrip())

o = calc(1, bits.copy())
c = calc(0, bits.copy())

print(o*c)


'''
part 1

#not happy with this
gamma = [0 for _ in range(12)] 

total = 0

for num in stdin:
    total += 1
    print(num)
    bits = [int(char) for char in num.rstrip()]
    print(bits)

    for index in range(len(bits)):
        if bits[index] == 1:
            gamma[index]+=1    

    print(gamma, total)

ga=''
ep=''
for char in gamma:
    if char > total//2:
        ep+='1'
        ga+='0'
    else:
        ep+='0'
        ga+='1'
print(ep, ga)
print(int(ep, 2), int(ga, 2))
print(int(ep, 2)*int(ga, 2))




'''
