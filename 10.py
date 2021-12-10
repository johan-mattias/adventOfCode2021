from sys import stdin

score= 0
auto_score=[]
def switch(char):
    if char == '(':
        return ')'
    elif char == '[':
        return ']'
    elif char == '{':
        return '}'
    elif char == '<':
        return '>'

for line in stdin:
    flag = True
    parse=[]
    auto_temp = 0

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
                flag = False
                break
        if char == ']':
            pop = parse.pop()
            if pop == '[':
                pass
            else:
                print('expected', '[', 'found', pop)
                score+=57
                flag = False
                break
        if char == '}':
            pop = parse.pop()
            if pop == '{':
                pass
            else:
                print('expected', '{', 'found', pop)
                score+=1197
                flag = False
                break
        if char == '>':
            pop = parse.pop()
            if pop == '<':
                pass
            else:
                print('expected', '<', 'found', pop)
                score+=25137
                flag = False
                break
    if(flag):
        print(parse)
        print([switch(char) for char in parse[::-1]])
        for char in parse[::-1]:
            char = switch(char)
            auto_temp *= 5
            if char == ')':
                auto_temp+= 1
            elif char == ']':
                auto_temp+=2
            elif char == '}':
                auto_temp +=3
            elif char == '>':
                auto_temp+= 4
        auto_score.append(auto_temp)

print(sorted(auto_score)[len(auto_score)//2])