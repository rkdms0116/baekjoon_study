N = int(input())

m_idx = 0
li = [0]*1001
for n in range(N):
    a, b = map(int, input().split())
    li[a]=b
    # 최댓값의 index 저장
    if li[m_idx] < b:
        m_idx=a

# 최댓값의 개수 확인
idx_li = []
for i in range(1001):
    if li[i]==li[m_idx]:
        idx_li.append(i)

dim = 0
if len(idx_li) == 1:
    m_height=0
    for i in range(m_idx+1):
        if li[i] > m_height:
            m_height = li[i]
        dim += m_height
    m_height=0
    for j in range(1000,m_idx,-1):
        if li[j] > m_height:
            m_height = li[j]
        dim += m_height

# 최댓값이 2개 이상
else:
    m_height=0
    for i in range(idx_li[0]+1):
        if li[i] > m_height:
            m_height = li[i]
        dim += m_height
    m_height=0
    for j in range(1000,idx_li[-1],-1):
        if li[j] > m_height:
            m_height = li[j]
        dim += m_height
    dim += li[idx_li[0]]*(idx_li[-1]-idx_li[0])

print(dim)