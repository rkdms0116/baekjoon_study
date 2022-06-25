def perm(n, k):
    result = []

    if k == 0:
        return result

    for i in range(n):
        result.append(i)
        perm(n,k-1)
        result.remove(i)



N, M = map(int, input().split())

num_li = []
for n in range(N):
    num_li.append(n+1)

# print(num_li)
for i in range(M):
    for j in range()