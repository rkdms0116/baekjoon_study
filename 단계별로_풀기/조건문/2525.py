A, B = map(int, input().split())
cookTime = int(input())

cookHour, cookMin = cookTime//60, cookTime%60

if B + cookMin < 60:
    print((A + cookHour)%24, B + cookMin)
else:
    print((A + cookHour + 1)%24, B + cookMin - 60)
