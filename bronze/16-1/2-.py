# 没啥思路，默认先提交 - 80%

# 0 2 3 4
# 该程序得到的答案 ans:3
# 实际应该是 4
# 3开始爆

# 所以这道题还是要穷举


import sys
sys.stdin = open('angry.in', 'r')
sys.stdout = open('angry.out', 'w')

pos = []
n = int(input())
for i in range(n):
    pos.append(int(input()))

pos.sort()

i = 0
r = 1
ans = 1
count = 1
while i < len(pos):
    j = i
    while j+1 < len(pos) and pos[i]+r >= pos[j+1]:
        j += 1
        count += 1
    if j == i:
        ans = max(ans, count)
        r = 1
        count = 1
        i += 1
    else:
        r += 1
        i = j

print(ans)


