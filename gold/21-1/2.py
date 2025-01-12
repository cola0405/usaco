'''
12 23 35 54
1 2 3 2 5 3 4

最优解: 1 -> 2 -> 3 -> 5 -> 4
可以证明不是单纯看最右
单纯看最左也不行，考虑此测试用例: 1 5 2 3 2 5 3 4
(选左边的5也不好使)

'''

from collections import defaultdict, deque
n,k = map(int, input().split())
b = list(map(int, input().split()))
S = [[int(c) for c in input()] for _ in range(k)]

d = defaultdict(list)       # record the index of each breed
for i in range(n): d[b[i]].append(i)

dis = [1e9 for _ in range(n)]
dis[0] = 0
q = deque([b[0]])  # index of the node
vis = [0] * (k+1)
while q:
    b1 = q.popleft()    # we are going to figure out the optimal way from b1 to b2
    if vis[b1]: continue
    vis[b1] = 1
    for nxt in range(k):
        if S[b1-1][nxt]:    # to fit the 0-index
            b2 = nxt+1
            # two pointers try the pairs to update dis[b2], O(n) -- every group of cow will only check once
            flag = 0
            u,v = 0,0
            while u < len(d[b1]) and v < len(d[b2]):
                if dis[d[b1][u]] + abs(d[b1][u]-d[b2][v]) < dis[d[b2][v]]:
                    dis[d[b2][v]] = dis[d[b1][u]] + abs(d[b1][u]-d[b2][v])
                    flag = 1
                if u == len(d[b1]) or d[b1][u] > d[b2][v]: v += 1
                else: u += 1
            if flag: q.append(b2)
print(dis[-1])
                
'''
4 3
1 3 2 1
010
011
111

ans: 5

8 8
1 2 3 4 5 6 7 8
01000010
00100000
00010000
00001000
00000100
00000001
00000100
00000000

ans: 7


'''