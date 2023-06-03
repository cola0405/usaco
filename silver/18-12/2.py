# 没办法走遍时间1e9的每一刻，需要优化
# 结合优先队列，key moment无非是eat_ending的时刻或新cow的arrive的时刻

import heapq
import sys
sys.stdin = open("convention2.in", "r")
sys.stdout = open("convention2.out", "w")

class Cow:
    def __init__(self, item):
        self.arrive = item[0]
        self.duration = item[1]
        self.s = item[2]

    def __lt__(self, other):
        if self.s < other.s:
            return True
        return False

n = int(input())
# (arrive_time, duration, seniority)
cows = [tuple(map(int, input().split()))+(i,) for i in range(n)]

# 逆序是为了pop的效率
cows.sort(key=lambda item:item[0], reverse=True)

# 优先队列存储资历最高者
wait = []

# the key moment
cur_time = cows[-1][0]
ans = 0
while len(cows) != 0 or len(wait) != 0:
    # 更新waiting优先队列
    while len(cows)>0 and cows[-1][0]<=cur_time:
        heapq.heappush(wait, Cow(cows.pop()))

    if len(wait)==0:    # skip the meaningless time
        cur_time = cows[-1][0]
        continue

    cow = heapq.heappop(wait)
    ans = max(cur_time - cow.arrive, ans)

    # the time for the end of this round eating
    cur_time += cow.duration

print(ans)