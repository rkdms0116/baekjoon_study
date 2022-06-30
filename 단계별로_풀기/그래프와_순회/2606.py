# 바이러스
from collections import deque
import sys
input = sys.stdin.readline

computer = int(input())
network = list([] for _ in range(computer + 1))

for _ in range(int(input())):
    c1, c2 = map(int, input().split())
    network[c1].append(c2)
    network[c2].append(c1)

virus = [1]
que = deque([1])
while que:
    q = que.popleft()
    if q not in virus:
        virus.append(q)

    for n in network[q]:
        if n not in virus:
            que.append(n)

print(len(virus)-1)