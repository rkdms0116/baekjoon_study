# 단어의 개수
sentence = input().strip()
cnt = 1
if sentence:
    for s in sentence:
        if s== " ":
            cnt += 1
    print(cnt)
else:
    print(0)