# 달팽이는 올라가고 싶다
import math
A, B, V = map(int,input().split())
day = (V-B)/(A-B)
print(math.ceil(day))