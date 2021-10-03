T = int(input())
result = []

for _ in range(T):
    N = int(input())

    # 성적을 받음
    score = []
    for n in range(N):
        a, b = map(int,input().split())
        score.append([a, b])

    cnt = N-1
    for i in range(N):
        for j in range(i,N):
            if score[i][0] > score[j][0] and score[i][1] > score[j][1]:
                cnt -= 1
                break

    print(cnt)