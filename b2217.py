n = int(input())

rope_list = []
for _ in range(n):
    rope_list.append(int(input()))
sorted_rope = sorted(rope_list)

total_weight = []
for i in range(n):
    total_weight.append(sorted_rope[i]*(n-i))

print(total_weight)