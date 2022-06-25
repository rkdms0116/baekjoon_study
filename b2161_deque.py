from typing import Deque

N = int(input())

result = []
card = Deque(list(n for n in range(1, N+1)))

while card:
    result.append(card.popleft())
    # pop해서 버린 뒤 card에 남은게 0일 수도 있으므로 확인
    if card:
        card.append(card.popleft())

print(*result)
