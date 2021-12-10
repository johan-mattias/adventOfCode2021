from sys import stdin

score= 0

valid = []

def comp(char):

for line in stdin:
    flag = True
    parse=[]

    for char in line.rstrip():
        if (char == '(' or char == '[' or
            char == '{' or char == '<'):
            parse.append(char)
        
        if char == ')':
            pop = parse.pop()
            if pop == '(':
                pass
            else:
                print('expected', '(', 'found', pop)
                score+=3
                break
        if char == ']':
            pop = parse.pop()
            if pop == '[':
                pass
            else:
                print('expected', '[', 'found', pop)
                score+=57
                break
        if char == '}':
            pop = parse.pop()
            if pop == '{':
                pass
            else:
                print('expected', '{', 'found', pop)
                score+=1197
                break
        if char == '>':
            pop = parse.pop()
            if pop == '<':
                pass
            else:
                print('expected', '<', 'found', pop)
                score+=25137
                break
print(score)