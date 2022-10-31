# 没啥思路，默认先提交 - 80%

# 0 2 3 4
# 该程序得到的答案 ans:3
# 实际应该是 4
# 3开始爆

# 0 2 3 4
# 不用考虑先右后左（2开始爆，右到3，左到0）
# 因为这种情况，在3开始爆也可以达到！

# 已经炸了


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
    left = i
    r = 1
    while True:
        spot = left
        while left-1 >= 0 and pos[spot]-r <= pos[left-1]:
            left -= 1
        if spot == left:
            break
        r += 1

    right = i
    r = 1
    while True:
        spot = right
        while right+1 < n and pos[spot]+r >= pos[right+1]:
            right += 1
        if spot == right:
            break
        r += 1
    ans = max(ans, right - left + 1)

print(ans)


