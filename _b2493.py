import sys, time
input = sys.stdin.readline

N = int(input())
laser = list(map(int, input().split()))
# 기준 top 설정
standard = 0
result = [0]

for n in range(len(laser)-1):
    if laser[n] > laser[n+1]:
        pass