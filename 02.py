from sys import stdin

x, y, aim = (0,0,0)

for line in stdin:
    direction, value = line.split()
    value = int(value)

    if direction == 'up':
        aim-= value
    elif direction == 'down':
        aim+= value
    elif direction == 'forward':
        x+=value
        y+=value*aim
    print(x, y,aim)

print(x, y, aim)
print(x*y)

'''
part1
x, y, aim = (0,0)

for line in stdin:
    direction, value = line.split()
    value = int(value)

    if direction == 'up':
        y-= value
    elif direction == 'down':
        y+= value
    elif direction == 'left':
        x-=value
    elif direction == 'forward':
        x+=value
    print(x, y)

print(x, y)
print(x*y)
'''