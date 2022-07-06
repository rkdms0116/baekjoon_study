# 트리의 부모 찾기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N = int(input())
# 연결된 node
node = list([] for _ in range(N+1))
# 노드의 부모를 찾는 tree
tree = [-1] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

def dfs(n):
    for i in node[n]:
        if tree[i] == -1:
            tree[i] = n
            dfs(i)

dfs(1)
for t in range(2, N+1):
    print(tree[t])