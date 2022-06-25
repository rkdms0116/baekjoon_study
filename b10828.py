import sys
input = sys.stdin.readline

N = int(input())
stack = []

for n in range(1, N+1):
    command = input().split()
    # print(command)
    # command가 list로 받아옴

    if command[0] == 'push':
        stack.append(command[1])

    elif command[0] == 'pop':
        if stack:
            ans = stack.pop()
            print(ans)
        else:
            print('-1')

    elif command[0] == 'size':
        print(len(stack))

    elif command[0] == 'empty':
        if stack:
            print('0')
        else:
            print('1')

    elif command[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print('-1')

