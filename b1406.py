# 시간초과
import queue
import sys
input = sys.stdin.readline

character = list(input().rstrip())
cursor = queue(len(character))

M = int(input())
for _ in range(M):
    command = input().split()

    if command[0] == 'L' and cursor > 0:
        cursor -= 1
    elif command[0] == 'D' and cursor < len(character):
        cursor += 1
    elif command[0] =='B':
        if cursor > 0 :
           character.pop(cursor-1)
           cursor -= 1
    elif command[0] == 'P':
        character.insert(cursor, command[1])
        cursor += 1
print(''.join(character))