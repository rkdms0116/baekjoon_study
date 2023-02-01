from itertools import combinations

L, C = map(int, input().split())
# 암호 알파벳 받아오기
alphabet = sorted(list(map(str, input().split())))
# 모음 list
vw = ['a', 'e', 'i', 'o', 'u']

# L자리로 만들 수 있는 조합 가져오기
pws = combinations(alphabet, L)

# pw 검증
for pw in pws:
    # 모음의 개수 확인
    vw_cnt = 0
    for p in pw:
        if p in vw:
            vw_cnt += 1
    # 모음이 1개 이상, 자음이 2개 이상인 암호만 print
    if vw_cnt > 0 and L-vw_cnt > 1:
        print(''.join(sorted(pw)))