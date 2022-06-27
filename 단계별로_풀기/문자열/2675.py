# 문자열 반복
import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    R, S = input().split()
    answer = ""
    for s in S:
        answer += s*int(R)
    print(answer)