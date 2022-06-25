N = int(input())

result = []
# card = []
# for n in range(1, N+1):
#     card.append(n)
card = list(n for n in range(1, N+1))

while card:
    result.append(card.pop(0))
    # pop해서 버린 뒤 card에 남은게 0일 수도 있으므로 확인
    if card:
        card.append(card.pop(0))

print(*result)