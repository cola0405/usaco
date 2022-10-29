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

ans = 1
for i in range(0, len(pos)):
    r = 1
    count = 1
    right = i
    while i < len(pos):
        while right+1 < len(pos) and pos[i]+r >= pos[right+1]:
            right += 1
            count += 1
        left = i
    while left-1 >= 0 and pos[i]-r <= pos[left-1]:
        left -= 1
        count += 1
    ans = max(ans, count)


print(ans)


