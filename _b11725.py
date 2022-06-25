# 왜 시간 초과..?

N = int(input())
tree = [0]*(N+1)
li = []

for n in range(N-1):
    a, b = map(int, input().split())
    li += [(a,b)]

i = 2
while li:
    for s in range(len(li)):
        if i in li[s]:
            if i == li[s][0]:
                tree[i] = li[s][1]
            else:
                tree[i] = li[s][0]
            li.pop(s)
            break
    i += 1

tree = tree[2:]
print(*tree, sep='\n')
