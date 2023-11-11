import bisect
import sys
sys.stdin = open("helpcross.in", "r")
sys.stdout = open("helpcross.out", "w")

c,n = map(int,input().split())

C = []
for i in range(c):
    C.append(int(input()))
C.sort()

N = []
for i in range(n):
    N.append(tuple(map(int, input().split())))

# 贪的就是end_time，故sort end_time，尽可能先用小gap
# （bisect_left 会重复访问chicken的，不用担心，可以就可以，不可以就下一个）
def by_end_time(item):
    return item[1]

N.sort(key=by_end_time)

ans = 0
for i in range(n):
    # 左边试着框
    inx = bisect.bisect_left(C, N[i][0], 0, len(C))
    if inx < len(C) and C[inx] <= N[i][1]:
        ans += 1
        # lower bound 的方法，是不得不pop
        C.pop(inx)

print(ans)

# 5 4
# 3
# 10
# 13
# 14
# 15
# 0 10
# 2 5
# 4 9
# 8 13


# 5 4
# 3
# 10
# 13
# 14
# 15
# 0 10
# 2 5
# 4 9
# 8 13
 # 3


# 5 4
# 3
# 10
# 13
# 5
# 15
# 3 5
# 4 13
# 5 5
# 8 13
 # 4

 # 36

