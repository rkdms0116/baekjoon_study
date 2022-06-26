N, X = map(int, input().split())

A = list(map(int, input().split()))
result = ""
for a in A:
    if a < X:
        result += str(a) + " "
print(result[:-1])

'''
a,b = map(int,input().split())
score = [x for x in input().split() if int(x)<b]
print(' '.join(score))
'''