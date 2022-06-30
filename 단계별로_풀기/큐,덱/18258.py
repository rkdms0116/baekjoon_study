# 큐 2
from collections import deque

import sys
input = sys.stdin.readline

N = int(input())
q = deque()
for _ in range(N):
    order = input().split()
    o = order[0]
    if o == "push":
        q.append(int(order[1]))
    
    elif o == "pop":
        print(q.popleft() if q else -1)
    
    elif o == "size":
        print(len(q))
    
    elif o == "empty":
        print(0 if q else 1)
    
    elif o == "front":
        print(q[0] if q else -1)
    
    elif o == "back":
        print(q[-1] if q else -1)
