# 나머지
import sys
input = sys.stdin.readline

R = []
for i in range(10):
    num = int(input())
    if num % 42 not in R:
        R.append(num%42)

print(len(R))

