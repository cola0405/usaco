# 好像说用并查集优化
from collections import defaultdict
import sys
sys.stdin = open("wormsort.in", "r")
# sys.stdout = open("wormsort.out", "w")

n,m = map(int, input().split())
cows = list(map(int, input().split()))
holes = [tuple(map(int, input().split())) for _ in range(m)]

# the pair need to switch
switch = [(i+1, cows[i]) for i in range(n) if i+1!=cows[i]]
if len(switch) == 0:
    print(-1)
    exit()
# to binary search the bound
holes.sort(key=lambda item: item[2])

# non-recursive
def reachable(g, src, dest):
    if len(g[src]) == 0:
        return False

    visit = [0]*(n+1)
    stack = g[src][::]
    while len(stack)>0:
        if stack[-1] == dest:
            return True
        else:
            top = stack.pop()
            visit[top] = 1
            stack += [node for node in g[top] if visit[node] == 0]
    return False


def fine(bound):
    # build graph
    g = defaultdict(list)
    for i in range(bound, m):
        a,b,w = holes[i]
        g[a].append(b)
        g[b].append(a)
    print(len(g))
    # check reachable
    deal = 0
    for a,b in switch:
        # 这怎么优化
        # 有很多重复的计算
        if reachable(g,a,b):
            deal += 1
    if deal == len(switch):
        return True
    return False

low = 0
high = m-1
while low<high:
    mid = (low+high+1)//2
    print(mid, len(switch))
    if fine(mid):
        low = mid
    else:
        high = mid-1
print(holes[low][2])