# 평균은 넘겠지
import sys
input = sys.stdin.readline

C = int(input())
for tc in range(C):
    students = list(map(int,input().split()))
    aver_score = sum(students[1:])/students[0]
    
    student_cnt = 0
    for s in range(students[0]):
        if students[s+1] > aver_score:
            student_cnt += 1
    
    print(f"{round(student_cnt/students[0]*100,3):.3f}%")