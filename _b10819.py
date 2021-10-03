N = int(input())
li = map(int, input().split())

li_up = sorted(li)

new_li = []
for i in range(N//2):
    new_li.append(li_up[i])
    new_li.append(li_up[N-1-i])
if N%2:
    new_li.append(li_up[N//2])

sum = 0
for j in range(N-1):
    sum += abs(new_li[j]-new_li[j+1])

print(sum)