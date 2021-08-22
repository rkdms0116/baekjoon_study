N = int(input())
for tc in range(N):
    sentence = list(map(str, input().split()))
    L = len(sentence)
    result = sentence[::-1]
    
    print('Case #{}: '.format(tc+1), end='')
    print(*result)