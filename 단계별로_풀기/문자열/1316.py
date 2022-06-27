# 그룹 단어 체커
import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
for tc in range(N):
    word = input()
    alphabet = [word[0]]
    for w in word:
        if alphabet[-1] == w:
            pass
        else:
            if w in alphabet:
                break
            else:
                alphabet.append(w)
    else:
        cnt += 1
print(cnt)