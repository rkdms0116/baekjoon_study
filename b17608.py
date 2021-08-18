N = int(input())

stick = []
for n in range(N):
    stick.append(int(input()))

height = stick[-1]
show = 1

for i in range(N-1,-1,-1):
    if stick[i] > height :
        show += 1
        height = stick[i]

print(show)