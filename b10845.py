import sys
N = int(sys.stdin.readline())

que = []

for i in range(N):
    cmd = sys.stdin.readline().split()   # 한 줄씩 읽어 쪼개 나가는 코드

    if cmd[0] == 'push':
        que.append(cmd[1])               # push X(X는 정수)
    
    elif cmd[0] == 'pop':
        if que == []:
            print('-1')                  # que에 정수가 없다면 -1 출력
        else:
            print(que.pop(0))            # que의 가장 앞의 정수 출력

    elif cmd[0] == 'size':
        print(len(que))                  # que에 들어있는 정수의 개수 출력
    
    elif cmd[0] == 'empty':
        if que == []:
            print('1')
        else:
            print('0')                   # que가 비어있으면 1, 아니면 0 출력
        
    elif cmd[0] == 'front':
        if que == []:
            print('-1')
        else:
            print(que[0])                # que의 가장 앞에 있는 정수 출력, 비어있을 경우 -1 출력
    
    elif cmd[0] == 'back':
        if que == []:
            print('-1')
        else:
            print(que[-1])               # que의 가장 뒤에 있는 정수 출력, 비어있을 경우 -1 출력