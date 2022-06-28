# 오큰수
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

NGE = [-1] * N
stack = []
for i in range(N) :
    while(len(stack) != 0 and A[stack[-1]] < A[i]) :
        NGE[stack[-1]] = A[i]
        stack.pop()
    stack.append(i)
print(*NGE)

'''
시간초과
N = int(input())
A = list(map(int, input().split()))
o_num = []
for n in range(N):
    for a in range(n+1, N+1):
        if a == N:
            o_num += [-1]
            break

        if A[n] < A[a]:
            o_num+= [A[a]]
            break

print(" ".join(map(str, o_num)))
'''