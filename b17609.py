# 시간 초과 발생
import sys
input = sys.stdin.readline

T = int(input()) 

for t in range(T):
    palin = str(input()) 
    cnt = 0

    while len(palin) > 1:
        if palin[0] == palin[len(palin)-1]:
            palin = palin[1:len(palin)-1]
        elif palin[1] == palin[len(palin)-1]:
            palin = palin[2:len(palin)-1]
            cnt += 1
        elif palin[0] == palin[len(palin)-2]:
            palin = palin[1:len(palin)-2]
            cnt += 1
        else:
            palin = palin[2:len(palin)-2]
            cnt += 2
        
    if cnt > 2:
        cnt = 2
    
    print(cnt)

