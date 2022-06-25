import sys
input = sys.stdin.readline

A, B = map(int, input().split())

L = 0
R = 0
# 시간 너무 오바
while A > 0 and B > 0:

    if A == 1 and B == 1:
        break

    if A > B:
        A = A-B
        L += 1
    else:
        B = B-A
        R += 1

print(L, R)
