data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
last = data[0]
total = 0

for number in data:
    print(last, number)
    if number > last:
        print('increase')
        total += 1
    last = number

print('total', total)