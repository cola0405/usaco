from bisect import bisect_left, bisect_right

import sys
sys.stdin = open("haybales.in", "r")
sys.stdout = open("haybales.out", "w")

n,q = map(int, input().split())
cows = list(map(int, input().split()))
cows.sort()

ans = []
for i in range(q):
    start, end = map(int, input().split())
    inx1 = bisect_left(cows, start)
    inx2 = bisect_right(cows, end)
    ans.append(str(inx2-inx1))

# 减少io 可以缩短一定时间
# 3000ms 到1500ms
print("\n".join(ans))


