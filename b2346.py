N = int(input())

# 풍선 list 받아오기
balloon = list(map(int, input().split()))
# index list 만들기
index = [i for i in range(1,N+1)]

# 결과 list
result = []
temp = balloon.pop(0)
result.append(index.pop(0))
idx = 0

while balloon:
    if temp >0:
        idx = (idx + temp -1) % len(balloon)
    else:
        idx = (idx + temp) % len(balloon)
    temp = balloon.pop(idx)
    result.append(index.pop(idx))

print(*result)