# 요세푸스 문제 0
from collections import deque

N, K = map(int, input().split())
que = deque([i for i in range(1, N+1)])
ans = []
nk = 0
while que:
    while nk < K:
        if nk == K-1:
            pass