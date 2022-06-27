# OX퀴즈
import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    OX = input()
    score = 0
    staight_o = 0
    for ox in OX:
        if ox == "O":
            staight_o += 1
            score += staight_o
        else:
            staight_o = 0
    
    print(score)

