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

def full_reachable(g,src,done):
    if len(g[src]) == 0:
        return

    visit = [0]*(n+1)
    stack = g[src].copy()
    visit[src] = 1
    # dfs 时是可以把中间节点给补全的
    while len(stack)>0:
        top = stack.pop()
        if visit[top] == 1:
            continue
        visit[top] = 1
        if done[top] == 1:  # when g[top] dfs already done
            g[src] = g[src] | g[top]
        else:
            reachable_nodes = {node for node in g[top] if visit[node] == 0}
            stack = stack | reachable_nodes
            g[src] = g[src] | reachable_nodes
            g[top] = g[top] | reachable_nodes
            done[top] = 1

def fine(bound):
    # build a reachable graph
    g = defaultdict(set)
    for i in range(bound, m):
        a,b,w = holes[i]
        g[a].add(b)
        g[b].add(a)

    done = [0]*(n+1)
    for node in g:
        full_reachable(g,node,done)
        done[node] = 1

    print(len(g))
    # check reachable
    deal = 0
    for a,b in switch:
        if b in g[a]:
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