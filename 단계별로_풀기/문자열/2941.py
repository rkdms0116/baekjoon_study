# 크로아티아 알파벳
words = input()

idx = 0
cnt = 0
while idx < len(words):
    if words[idx] == 'c':
        if idx+1 < len(words) and (words[idx+1] == '=' or words[idx+1] == '-'):
            idx += 2
        else:
            idx += 1
    elif words[idx] == 'd':
        if idx+1 < len(words) and words[idx+1] == '-':
            idx += 2
        elif idx+2 < len(words) and words[idx+1] == 'z' and words[idx+2] == '=':
            idx += 3
        else:
            idx += 1
    elif words[idx] == 'l':
        if idx+1 < len(words) and words[idx+1] == 'j':
            idx += 2
        else:
            idx += 1
    elif words[idx] == 'n':
        if idx+1 < len(words) and words[idx+1] == 'j':
            idx += 2
        else:
            idx += 1
    elif words[idx] == 's':
        if idx+1 < len(words) and words[idx+1] == '=':
            idx += 2
        else:
            idx += 1
    elif words[idx] == 'z':
        if idx+1 < len(words) and words[idx+1] == '=':
            idx += 2
        else:
            idx += 1
    else:
        idx += 1
    cnt += 1

print(cnt)