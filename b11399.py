N = int(input())
people = list(map(int, input().split()))

result, sum_time = 0, 0
sort_people = sorted(people)

for i in sort_people:
    result += i
    sum_time += result

print(sum_time)