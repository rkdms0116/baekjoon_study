from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

# 입력값
# N : 정점의 개수, M : 간선의 개수, V : 탐색을 시작할 정점의 번호
N, M, V = map(int, input().split())

# 간선을 입력할 node dict
node = {}

# M만큼의 간선을 node에 저장
for _ in range(M):
    A, B = map(int, input().split())
    if A in node:
        node[A].append(B)
    else:
        node[A] = [B]
    if B in node:
        node[B].append(A)
    else:
        node[B] = [A]

# node 안 list 정렬
for n in node:
    node[n].sort()

# dfs 설정
dfs_list = [V]
visit = [True] * N
visit[V-1] = False

def dfs(node, v, visited):
    if v in node:
        for n in node[v]:
            if visited[n-1]:
                dfs_list.append(n)
                visited[n-1] = False
                dfs(node, n, visited)

# bfs 설정
b_visit = [True] * N

def bfs(node, V, visit):
    bfs_list = []
    visit[V-1] = False
    stack = deque([V])
    while stack:
        s = stack.popleft()
        bfs_list.append(s)
        if s in node:    
            for n in node[s]:
                if visit[n-1]:
                    stack.append(n)
                    visit[n-1] = False
    return bfs_list               

dfs(node, V, visit)

print(' '.join(map(str, dfs_list)))
print(' '.join(map(str, bfs(node, V, b_visit))))
