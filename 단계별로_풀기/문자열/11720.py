# 숫자의 합
import sys
input = sys.stdin.readline

N = int(input())
number = input().rstrip()
result = 0
for n in number:
    result += int(n)

print(result)