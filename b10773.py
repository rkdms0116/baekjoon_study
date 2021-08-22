K = int(input())

li = []
for k in range(K):
    li.append(int(input()))

ea = []
for i in range(K):
    if li[i] != 0:
        ea.append(li[i])
    else:
        ea.pop(-1)

print(sum(ea))