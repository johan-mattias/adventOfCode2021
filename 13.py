from pprint import pprint

dots = []
instructions = []
max_y = 0
max_x = 0
with open('13_in.txt') as file:
    for line in file:
        if line.rstrip() == '':
            pass
        elif ',' in line:
            x, y = [int(char) for char in line.rstrip().split(',')]
            if y > max_y:
                max_y = y
            if x > max_x:
                max_x = x
            dots.append((x, y))
        else:
            instructions.append(line.rstrip().replace('fold along ','').split('='))
            
print(dots)
print(instructions)
print(max_x, max_y)

def print_grid():
    grid = []
    for y in range(max_y+1):
        grid.append([])
        for x in range(max_x+1):
            grid[y].append('.')
    
    for x, y in dots:
        print(x, y)
        grid[y][x] = '#'
    pprint(grid)
        
print_grid()

for axis, value in instructions:
    value = int(value)
    for index in range(len(dots)):
        x, y = dots[index]
        if axis == 'y':
            if y < value:
                pass
            else:
                y = max_y-y
        dots[index] = tuple([x, y])
print(dots)
print_grid()

for x in range():
    pass

print(len(set(dots)))