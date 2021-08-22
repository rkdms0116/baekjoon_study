card = [i for i in range(1, int(input())+1)]

while len(card) > 1:
    card.pop(0)
    last = card[0]
    card.pop(0)
    card.append(last)

print(*card)