# 利用dict来确定对应index优化count统计
def search_right(cur):
    radius = 1
    count = 0
    while True:
        flag = 0
        # 按h推是更好的，高效skip search
        for j in range(cur+1, n):
            if h[cur]+radius >= h[j]:
                count += 1
                flag = 1
            else:
                j -= 1
                break
        if flag == 0:
            break
        cur = j
        radius += 1
    return count


def search_left(cur):
    radius = 1
    count = 0
    while True:
        flag = 0
        for j in range(cur)[::-1]:
            if h[cur] - radius <= h[j]:
                count += 1
                flag = 1
            else:
                j += 1
                break
        if flag == 0:
            break
        radius += 1
        cur = j
    return count

import sys
sys.stdin = open('angry.in', 'r')
sys.stdout = open('angry.out', 'w')

n = int(input())
h = [int(input()) for i in range(n)]
h.sort()
the_index = {h[i]: i for i in range(len(h))}


ans = 1
for start in range(n):
    count = 1
    count += search_left(start)
    count += search_right(start)
    ans = max(count, ans)

print(ans)
