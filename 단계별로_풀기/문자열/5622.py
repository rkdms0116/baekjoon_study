# 다이얼
dial = {
    2 : {'A', 'B', 'C'}, 3 : {'D', 'E', 'F'},
    4 : {'G', 'H', 'I'}, 5 : {'J', 'K', 'L'},
    6 : {'M', 'N', 'O'}, 7 : {'P', 'Q', 'R', 'S'},
    8 : {'T', 'U', 'V'}, 9 : {'W', 'X', 'Y', 'Z'},
}
t = 0
word = input()
for w in word:
    for i in range(2, 10):
        if w in dial[i]:
            t += i+1
            break
print(t)