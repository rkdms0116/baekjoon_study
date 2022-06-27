# 최댓값
import sys
input = sys.stdin.readline

max_idx = 0
max_num = 0
for idx in range(9):
    num = int(input())
    if num > max_num:
        max_num = num
        max_idx = idx
print(max_num)
print(max_idx+1)