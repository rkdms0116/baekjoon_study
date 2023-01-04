# 블랙잭
from itertools import combinations
# N: 카드의 개수, M: M에 가까운 수를 만들어야 한다.
N, M = map(int, input().split())

cards = list(map(int, input().split()))

ans = 9
card_sum = set()
# card_sum이라는 집합에 모든 경우의 수 대입(중복이 너무 많아서 set)
for i in range(1, N+1):
    for card_li in combinations(cards, 3):
        card_sum.add(sum(card_li))
# M에 가장 가까운 수를 찾기
for c in card_sum:
    if M >= c and ans < c:
        ans = c
print(ans)