from sys import stdin
from pprint import pprint

data = []

for line in stdin:
    line = '9'+line.rstrip()+'9'
    data.append([int(char) for char in line])
data.insert(0, [9 for _ in data[0]])
data.append([9 for _ in data[0]])    
#pprint(data)

low_points = []

for row in range(len(data)):
    for col in range(len(data[row])):
        if (data[row][col] < data[row][col-1] and
            data[row][col] < data[row-1][col] and
            data[row][col] < data[row][col+1] and
            data[row][col] < data[row+1][col]):
            low_points.append(data[row][col]+1)
#print(low_points)

print(sum(low_points))