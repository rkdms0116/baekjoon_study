dice = list(map(int, input().split()))
print(set(dice))
if len(set(dice)) == 1:
    price = 10000 + dice[0]*1000
elif len(set(dice)) == 2:
    cnt = []
    for d in dice:
        if d in cnt:
            price = 1000 + d*100
        else:
            cnt.append(d)
else:
    d = max(dice)
    price = d*100

print(price)