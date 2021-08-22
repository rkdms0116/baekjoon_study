N, K = map(int, input().split())

sit = [i for i in range(1,N+1)]
Jose = []

n = K-1
num = n
while sit:
    if num < len(sit):
        Jose.append(sit[num])
        sit.pop(num)
        num += n
    else:
        num -= len(sit)
        try:
            Jose.append(sit[num])
            sit.pop(num)
            num += n
        except IndexError:
            pass

print("<%s>" %(", ".join(Jose)))
