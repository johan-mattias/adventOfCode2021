from sys import stdin

epsilon = [0,0,0,0,0] 

total = 0

for num in stdin:
    total += 1
    print(num)
    a, b, c, d, e = [int(char) for char in num.rstrip()]
    print(a, b, c, d, e)
    if a == 1:
        epsilon[0]+=1    
    elif b == 1:
        epsilon[1]+=1
    elif c == 1:
        epsilon[2]+=1
    elif d == 1:
        epsilon[3]+=1
    elif e == 1:
        epsilon[4]+=1

print(epsilon, total)

ep=''
for char in epsilon:
    if char > total//2:
        ep+='1'
    else:
        ep+='0'
print(ep)


