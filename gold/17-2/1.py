'''
dijastra

题目大意：牛从左上角要移动到右下角，每次可以移动到相邻的一个格子，然后每三次移动需要停下来花费额外的时间吃草
问牛到达右下角所花费的最少时间

关注三次可达的点然后跑 dijastra即可
'''

import sys, heapq
sys.stdin = open('visitfj.in', 'r')
sys.stdout = open('visitfj.out', 'w')

N,T = map(int,input().split())
t = [list(map(int,input().split())) for _ in range(N)]

q = [(0,0,0)]   # (min_time_to_xy, x, y)
min_time = [[float('inf')]*N for _ in range(N)]
min_time[0][0] = 0
vis = [[0]*N for _ in range(N)]
while q:
    time,x,y = heapq.heappop(q)
    vis[x][y] = 1
    # 枚举可达范围内的所有点，不一定要用 dfs来搜
    for i in range(-3,4):
        for j in range(-3,4):
            if 0<=x+i<N and 0<=y+j<N and not vis[x+i][y+j]:     # vis 标记过的其最短距离已经确定了，故不再考虑
                # 只关注三次可达的点（含折返的点） —— 因为最优解路径必定是以每 3次作为一个节点的
                if (abs(i)+abs(j) == 1 or abs(i)+abs(j) == 3) and time + 3*T + t[x+i][y+j] < min_time[x+i][y+j]:
                    min_time[x+i][y+j] = time + 3*T + t[x+i][y+j]
                    heapq.heappush(q,(min_time[x+i][y+j],x+i,y+j))

    # 可能有多条路径可以到终点，而且不一定是3次刚好到，所以这里需要抽出来特殊处理一下
    d = abs(x-(N-1)) + abs(y-(N-1))     # 到终点的距离
    if d < 3:
        min_time[N-1][N-1] = min(min_time[N-1][N-1], time + d*T)
    elif d == 3:                        # 第 3次移动恰好到终点，要吃终点位置的草
        min_time[N-1][N-1] = min(min_time[N-1][N-1], time + 3*T + t[N-1][N-1])
print(min_time[N-1][N-1])
