# 100
# 从左往右贪心
# 把研究对象转化为diff，简化问题 —— 把杀虫剂的效果统一为+-1

n = int(input())
d = list(map(int, input().split()))

diff = [0]
d.insert(0,0)
for i in range(1,n+1):
    diff.append(d[i]-d[i-1])

ans = 0
delta = 0
cur = 0
for i in range(1,n+1):
    if diff[i] == diff[i-1]:
        continue
    cur = 0 - (diff[i] + delta)        # 当前要喷的次数取决于delta和当前diff[i]
    ans += abs(cur)  # 当前需要喷杀虫剂的次数
    delta += cur    # delta 记录了cur后diff整体的变化情况

print(ans)
