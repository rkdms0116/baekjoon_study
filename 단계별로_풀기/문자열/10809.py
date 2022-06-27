# 알파벳 찾기
word = input()
alphabet_list = [-1] * 26
for w in range(len(word)):
    if alphabet_list[ord(word[w])-97] == -1:
        alphabet_list[ord(word[w])-97] = w

print(" ".join(map(str, alphabet_list)))