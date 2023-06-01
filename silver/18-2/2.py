import sys
sys.stdin = open("snowboots.in", "r")
sys.stdout = open("snowboots.out", "w")

n,b = map(int, input().split())
f = list(map(int, input().split()))
boots = [list(map(int, input().split())) for _ in range(b)]
visit = [[0]*b for _ in range(n)]

ans = float('inf')
def dfs(cur, bi):
    global ans
    if cur == n-1:
        return bi
    if visit[cur][bi]:
        return
    visit[cur][bi] = 1
    si,di = boots[bi]
    # try to step forward
    for i in range(cur+1, min(cur+di+1, n)):
        if si >= f[i]:
            res = dfs(i, bi)
            if res and res<ans:
                ans = res
    # switch boot
    for j in range(bi+1, b):
        if boots[j][0] >= f[cur]:
            res = dfs(cur, j)
            if res and res<ans:
                ans = res


dfs(0,0)
print(ans)


