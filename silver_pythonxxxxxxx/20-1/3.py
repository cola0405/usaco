from collections import defaultdict
import sys
sys.stdin = open("wormsort.in", "r")
sys.stdout = open("wormsort.out", "w")

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

def reachable(g, src, dest, visit):
    if src == dest:
        return True

    if len(g[src]) == 0 or visit[src] == 1:
        return False
    visit[src] = 1
    for node in g[src]:
        if reachable(g, node, dest, visit):
            return True

    return False


def fine(bound):
    # build graph
    g = defaultdict(list)
    for i in range(bound, m):
        a,b,w = holes[i]
        g[a].append(b)
        g[b].append(a)

    # check reachable
    deal = 0
    for a,b in switch:
        visit = [0]*(n+1)
        if reachable(g,a,b,visit):
            deal += 1
    if deal == len(switch):
        return True
    return False

low = 0
high = m-1
while low<high:
    mid = (low+high+1)//2
    if fine(mid):
        low = mid
    else:
        high = mid-1
print(holes[low][2])