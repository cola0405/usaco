# 答案肯定是炸在某一个堆
# 枚举，找最大值即可

# 模拟爆炸 -- r不断递增，模拟即可


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


