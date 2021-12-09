from sys import stdin
from collections import defaultdict
from pprint import pprint

count = 0
for line in stdin:
    print(line)
    code, digits = line.rstrip().split('|') 
    print(digits)
    digits = digits.split()
    for num in digits:
        print(num)
        if len(num) == 2:
            count += 1
        elif len(num) == 3:
            count += 1
        elif len(num) == 4:
            count += 1
        elif len(num) == 7:
            count += 1
        print(count)
print(count) 
