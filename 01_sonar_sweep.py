from sys import stdin
increases = 0
first = int(stdin.readline())
second = int(stdin.readline())
third = int(stdin.readline())

prev_window = first+second+third

for num in stdin:
    first = second
    second = third
    third =  int(num.rstrip())
    current_window = first+second+third

    if current_window > prev_window:
        increases += 1
    prev_window = current_window

print(increases)
