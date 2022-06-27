# 숫자의 개수
import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

ABC = str(A*B*C)
num_cnt = [0] * 10

for i in range(len(ABC)):
    num_cnt[int(ABC[i])] += 1

for n in range(10):
    print(num_cnt[n])

'''
for i in range(10):
    print(d.count(i))
'''