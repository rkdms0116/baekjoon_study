# 단어 공부
word_cnt = dict()
words = input().upper()
for w in words:
    if w in word_cnt:
        word_cnt[w] += 1
    else:
        word_cnt[w] = 1

if list(word_cnt.values()).count(max(word_cnt.values())) > 1:
    print('?')
else:
    new_dict = {value:key for key, value in word_cnt.items()}
    print(new_dict[max(word_cnt.values())])
    # print(new_dict)
